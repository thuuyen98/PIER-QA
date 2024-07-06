import re
import json
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import glob
from tqdm import tqdm 
import random
import csv
files = glob.glob("./*.md")
list_chunks = []
data_final = []
instruction = """You are an assistant for question-answering tasks. Use the context that the user gives to answer the question. Treat the context as your internal knowledge, hence do not explicitly mention the "context" in your answer like "Based on the provided context...".If your answer relates to any image description given below, you should refer explicitly to the image ID in your answer with the format [image_id.png].Give a long and detailed answer."""
model = "MaziyarPanahi/Meta-Llama-3-70B-Instruct-GPTQ"
model_kwargs={'stop': ['<|eot_id|>', '<|end_of_text|>', '<|start_header_id|>', '<|end_header_id|>']}
#llm = ChatOpenAI(model_name=model, openai_api_key='BVJD4F99OBYPLI0PTM46PI5VK5D09HUD2B404UT6',model_kwargs=model_kwargs, openai_api_base='https://api.runpod.ai/v2/vllm-svgd8vjj76vhwf/openai/v1/', temperature=0)
turbo_llm = ChatOpenAI(
            openai_api_key = 'sk-proj-Uwz9U5lQUkGeOl2g02hOT3BlbkFJieTKrXeuntuNotXA2Qb8',
            temperature=0,
            model_name="gpt-4o"
            #max_tokens = 4096 - 500
        )
template = """Given the below context, generate 5 questions that cover all information from the context. The questions should be about the content of the given context, do NOT give questions about meta data of the document/context such as document structure, purpose or goal. Only give questions, each question in one line, starting with a number 1, 2, 3, 4, and 5.

Context: {context}"""

system = """You are an assistant for question-answering tasks. 
Use the context that the user gives to answer the question. Treat the context as your internal knowledge, hence do not explicitly mention the "context" in your answer like "Based on the provided context...".
If your answer relates to any image description given below, you should refer explicitly to the image ID in your answer with the format [image_id.png].
Give a long and detailed answer. Always answer in English regardless of the document language."""

# template_answer = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

# You are an assistant for question-answering tasks. 
# Use the context that the user gives to answer the question. Treat the context as your internal knowledge, hence do not explicitly mention the "context" in your answer like "Based on the provided context...".
# If your answer relates to any image description given below, you should refer explicitly to the image ID in your answer with the format [image_id.png].
# Give a long and detailed answer.<|eot_id|><|start_header_id|>user<|end_header_id|>

# Context: {context}

# Question: {question}<|eot_id|>
# <|start_header_id|>assistant<|end_header_id|>

# Answer (long):"""

def table_to_dict_list(table_text):
        # Split table text into lines
        lines = table_text.strip().split('\n')
    
        # Initialize list to hold rows
        rows = []
    
        # Iterate over each line
        for line in lines:
            # Split line into cells, ignoring empty cells
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
    
            # Ensure cells are in key-value pair format
            if len(cells) >= 2:
                row_dict = {}
                for i in range(0, len(cells), 2):
                    key = cells[i].strip(':')  # Remove any trailing colon from keys
                    if i + 1 < len(cells):  # Check if there's a corresponding value
                        value = cells[i + 1].strip()
                        row_dict[key] = value
                rows.append(row_dict)
    
        return rows
    
for f in tqdm(files):
    with open(f, 'r') as file:
        content = file.read()
    # Regex pattern to match tables in markdown
    table_pattern = re.compile(r'(\|.*?\|(?:\n\|[-:]+.*?)+\n(?:\|.*?\|(?:\n|$))+)', re.DOTALL)
    
    # Find all tables
    tables = table_pattern.findall(content)
    # Replace each table with its dictionary representation
    i = 0
    for table in tables:
        table_dict_list = table_to_dict_list(table)
        table_dict_str = str(table_dict_list)
        content = content.replace(table, f'<table_{i}>{table_dict_str}</table_{i}>')
        i+= 1
    
    text_splitter = RecursiveCharacterTextSplitter (chunk_size=1000)
    texts = text_splitter.create_documents([content])
    new_chunk = [c.page_content for c in texts]
    list_chunks.extend(new_chunk)
with open("BAHLB1400_21.10.2019_D_E_caption.md", 'r') as file:
    content = file.read()
# Regex pattern to match tables in markdown
table_pattern = re.compile(r'(\|.*?\|(?:\n\|[-:]+.*?)+\n(?:\|.*?\|(?:\n|$))+)', re.DOTALL)

# Find all tables
tables = table_pattern.findall(content)
# Replace each table with its dictionary representation
i = 0
for table in tables:
    table_dict_list = table_to_dict_list(table)
    table_dict_str = str(table_dict_list)
    content = content.replace(table, f'<table_{i}>{table_dict_str}</table_{i}>')
    i+= 1

text_splitter = RecursiveCharacterTextSplitter (chunk_size=5000)
texts = text_splitter.create_documents([content])
with open('./BAHLB1400_21.10.2019_D_E_caption_gpt.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, ['instruction', 'input', 'output'])
    dict_writer.writeheader()
    for text in tqdm(texts):
        chunks = RecursiveCharacterTextSplitter (chunk_size=1000).create_documents([text.page_content])
        new_chunk = [c.page_content for c in chunks]
        random_chunk = random.choices(list_chunks, k=5)
        new_chunk.extend(random_chunk)
        random.shuffle(new_chunk)
        context_input = " <chunk_seperator> ".join(new_chunk)
        response = turbo_llm.invoke([('human', template.format(context=text.page_content))])
        questions = response.content
        l = questions.split("\n")
        list_q = []
        for q in l:
            if "1. " in q or "2. " in q or "3. " in q or "4. " in q or "5. " in q:
                dict_data = {}
                dict_data['instruction'] = instruction
                dict_data['input'] = f'Context: {context_input}\nQuestion: {q[2:]}'
                # dict_data['output'] = llm.invoke(template_answer.format(context=text.page_content, question= q[2:]))
                dict_data['output'] = turbo_llm.invoke([('system', system), ('human', f'Context: {text.page_content}\nQuestion: {q[2:]}')]).content
                data_final.append(dict_data)
                dict_writer.writerow(dict_data)