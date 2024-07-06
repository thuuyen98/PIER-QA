import subprocess

LLAVA_EXEC_PATH = "/Users/uyenhoang/Project/llama.cpp/build/bin/llava-cli"
MODEL_PATH = "/Users/uyenhoang/Downloads/ggml-model-q5_k.gguf"
MMPROJ_PATH = "/Users/uyenhoang/Downloads/mmproj-model-f16.gguf"

PROMPT = "Describe the image in detail. Be specific about graphs, such as bar plots."

TEMP = 0.1 #  a lower temperature value like 0.1 is recommended for better quality.

def image_to_text(image_path, text_path):
    bash_command = f'{LLAVA_EXEC_PATH} -m {MODEL_PATH} --mmproj {MMPROJ_PATH} --temp {TEMP} -p "{PROMPT}"'

    bash_command_cur = f'{bash_command} --image "{image_path}" > "{text_path}"'

    process = subprocess.Popen(
        bash_command_cur, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    output, error = process.communicate()

    print("Output:")
    print(output.decode("utf-8"))

    print("Error:")
    print(error.decode("utf-8"))

    return_code = process.returncode
    return return_code == 0

image_to_text("/Users/uyenhoang/Downloads/Data/testpdf/0_image_1.png", "/Users/uyenhoang/Downloads/Data/summarization.txt")


#bin/llava-cli -m ../Users/uyenhoang/Downloads/ggml-model-q5_k.gguf --mmproj ../Users/uyenhoang/Downloads/mmproj-model-f16.gguf --temp 0.1
# -p "Describe the image in detail. Be specific about graphs, such as bar plots." --image "/Users/uyenhoang/Downloads/Data/testpdf/0_image_1.png” > “/Users/uyenhoang/Downloads/Data"