import subprocess
from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler
import os, glob
from os.path import join
import base64
from Preprocessing.pdf_parser import PDFExtractor
from pathlib import Path
import shutil
from tqdm import tqdm
import hashlib


MODEL_PATH = "Model/ggml-model-q5_k.gguf"
MMPROJ_PATH = "Model/mmproj-model-f16.gguf"
PROMPT = "Describe the image in detail. Extract important text from graphs, diagrams, or tables if they appear in the image, and be specific about it."

chat_handler = Llava15ChatHandler(clip_model_path=MMPROJ_PATH)
llm = Llama(
    model_path=MODEL_PATH,
    chat_handler=chat_handler,
    n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
    n_gpu_layers=9999,
    verbose=False
)

def image_to_base64_data_uri(file_path):
    with open(file_path, "rb") as img_file:
        base64_data = base64.b64encode(img_file.read()).decode('utf-8')
        return f"data:image/png;base64,{base64_data}"

def extract_data(pdf_path, output_path):
    bash_command = f'marker_single "{pdf_path}" "{output_path}" --batch_multiplier 2 --langs English'
    process = subprocess.Popen(
        bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    output, error = process.communicate()

    print("Output:")
    print(output.decode("utf-8"))

    print("Error:")
    print(error.decode("utf-8"))

    return_code = process.returncode
    return return_code == 0



def image_to_caption(image_path):
    data_uri = image_to_base64_data_uri(image_path)
    response=llm.create_chat_completion(
        messages = [
            {"role": "system", "content": "You are an assistant who perfectly describes images."},
            {
                "role": "user",
                "content": [
                    {"type" : "text", "text": f'{PROMPT}'},
                    {"type": "image_url", "image_url": {"url": f'{data_uri}' } }
                ]
            }
        ],
        stop=["<|eot_id|>", '<|end_of_text|>', '<|im_end|>'],
        temperature=0,
        # presence_penalty=0.7,
        # frequency_penalty=0.7,
        # top_p=1,
        # top_k=20,
    )
    response = response['choices'][0]['message']['content'].replace('\n', ' ').strip()
    print('\n', image_path)
    print(response, '\n')
    return response
    

def pipeline(pdf_dir, out_dir): 
    all_files = glob.glob(join(pdf_dir, "*.*"))
    for p in all_files:
        if not p.endswith('.pdf'):
            shutil.copyfile(p, join(out_dir, p.split('/')[-1]))
    pdf_ls = glob.glob(join(pdf_dir, "*.pdf")) 
    header_removed_path = join(pdf_dir, 'header_footer_remove') 
    md_dir = join(header_removed_path, 'markdown') 
    if not os.path.exists(header_removed_path):
        os.makedirs(header_removed_path)
    for pdf_file in pdf_ls:   
        root, file_name = os.path.split(pdf_file) 
        print('# PROCESSING', file_name)
        removed_file_path = join(header_removed_path, file_name) 
        if not Path(removed_file_path).is_file():
            print('### Remove headers and footers', removed_file_path)
            pdf_extractor = PDFExtractor(pdf_file, removed_file_path)
            pdf_extractor.run()
        else:
            print('### Skip removing headers and footers')
        
        base_name = file_name.rstrip('.pdf')
        file_hash = str(int(hashlib.sha1(pdf_file.encode("utf-8")).hexdigest(), 16) % (10 ** 5))
        md_file = join(md_dir, file_hash, base_name, base_name + '.md')
        
        if not Path(md_file).is_file():
            print('### Convert to Markdown', md_file)
            extract_data(removed_file_path, join(md_dir, file_hash)) 
        else:
            print('### Skip converting to Markdown')

        # md_file_caption = join(md_dir, base_name, base_name + '_caption.md')
        md_file_caption = join(out_dir, base_name + '.md')
        if not Path(md_file_caption).is_file():
            print('### Captionize images', md_file_caption)
            content = open(md_file, 'r').read()
            content = content.replace('_Image_', '_image_').replace('.Png]', '.png]').replace('.Png)', '.png)').replace('.png]', f'_{file_hash}.png]')
            image_ls = glob.glob(join(join(md_dir, file_hash), base_name, '*.png'))
            for image_path in image_ls:
                _, img_name = os.path.split(image_path)
                caption = image_to_caption(image_path)
                content = content.replace(f'({img_name})', f'({caption})')
            with open(md_file_caption, 'w') as f:
                f.write(content)
        else:
            print('### Skip image captionization')
        print('### Done!')
     
                 
        