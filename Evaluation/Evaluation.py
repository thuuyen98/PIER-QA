from langchain.embeddings import SentenceTransformerEmbeddings
from HFEmbeddings import HFEmbeddings
import torch
import  torch.nn.functional as F
import csv
from Data_management import ChatController 
from pathlib import Path
from ast import literal_eval
import re
from tabulate import tabulate

model_name = "Alibaba-NLP/gte-large-en-v1.5"
model_kwargs = {'device': 'cuda', 'trust_remote_code':True}
encode_kwargs = {'normalize_embeddings': False}
model = HFEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
) 
def evaluation(thred, predictions, answers):
    list_predictions = []
    list_answers = []
    for p in predictions:
        embedding_1 = model.embed_query(p)
        list_predictions.append(embedding_1)
    for a in answers:
        embedding_2 = model.embed_query(a)
        list_answers.append(embedding_2)
    predictions_ts = torch.tensor(list_predictions)
    answer_ts = torch.tensor(list_answers)
    a = F.cosine_similarity(predictions_ts, answer_ts)
    print("total: ", len(predictions))
    print("prediction:")
    print(a)
    print(a.mean())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if thred != 0:
        l = a.tolist()
        s_1 = 0 #0.7
        s_2 = 0 #0.75
        s_3 = 0 #0.8
        s_4 = 0 #0.85
        s_5 = 0 #0.9
        s_6 = 0 #0.92
        s_7 = 0 #0.95
        for x in l:
            if x>= 0.7:
                s_1+=1
            if x>= 0.75:
                s_2+=1
            if x>= 0.8:
                s_3+=1
            if x>= 0.85:
                s_4+=1
            if x>= 0.9:
                s_5+=1
            if x>= 0.92:
                s_6+=1
            if x>= 0.95:
                s_7+=1
        print("accuracy at 0.7: ")
        print(s_1/len(l))
        print("accuracy at 0.7.5: ")
        print(s_2/len(l))
        print("accuracy at 0.8: ")
        print(s_3/len(l))
        print("accuracy at 0.85: ")
        print(s_4/len(l))
        print("accuracy at 0.9: ")
        print(s_5/len(l))
        print("accuracy at 0.92: ")
        print(s_6/len(l))
        print("accuracy at 0.95: ")
        print(s_7/len(l))

def evaluation_image_table(predictions, answers):
    t = 0
    s = 0
    for i, p  in enumerate(predictions):
        pattern = r'\[\d+_image_\d+\.png\]'
        #pattern = r'\[table_\d+\]'
        matches = re.findall(pattern, p)
        s += 1
        for m in matches:
            print("imagesss 1")
            print(m)
            if m in answers[i]:
                print("imagesss 2")
                print(answers[i])
                t += 1
                print(",,,,,,,,")
    print(t/s)
    

def eval_gpt():  
    questions = []
    answers = []
    qa = {}
    with open('image_eval.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if ".png]" not in row[1]:
                a = row[2]
                qa[row[1]] = a
                questions.append(row[1])
    
    chat = ChatController()
    chat.use_agent = False
    predictions = []
    results = {}
    out_file = "pred_image.txt"
    if Path(out_file).is_file():
        results = literal_eval(open(out_file).read())
    for q in questions:
        if q not in results:
            a = chat.ask(q)
            results[q] = a
            with open(out_file, "w") as file:
                file.write(str(results))
    for q, a in results.items():
        print(qa[q])
        answers.append(qa[q])
        predictions.append(a)
    evaluation(1, answers, predictions)


def eval_hydac():
    questions = []
    qa_eval = {}
    qa_hydac = {}
    predictions = []
    answers = []
    with open('eval.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if ".png]" not in row[1]:
               qa_eval[row[1]] = row[2]
               questions.append(row[1])
    with open('Hydac_4.0.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if ".png]" not in row[1]:
               qa_hydac[row[1]] = row[2]
    for q in questions:
        answers.append(qa_hydac[q])
        predictions.append(qa_eval[q])
    evaluation(0.8, answers, predictions)
eval_gpt()