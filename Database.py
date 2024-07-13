# this software is mainly derivated from the example found at the following link https://github.com/rubentak/Langchain/blob/main/notebooks/Langchain_doc_chroma.ipynb

from langchain_community.vectorstores import Chroma
import os
from langchain_community.vectorstores import ElasticsearchStore
import uuid
import Raptor as Raptor
from HFEmbeddings import LlamaCppEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_community import document_loaders
from langchain_core.documents import Document
from elasticsearch.helpers import scan
from elasticsearch import Elasticsearch
import os

llama = LlamaCppEmbeddings(model_path="./Model/gte-Qwen2-7B-instruct.Q5_K.gguf", n_gpu_layers=9999)
llama.client.verbose = False

class ElasticSearch(object):
    def __init__(self, txt_directory='./Database/Public/Files/', index_name='elastic'):

        # init some variables
        self.DirectoryLoader = DirectoryLoader
        self.txt_directory = txt_directory
        self.index_name = index_name
        self.chunk_size = 1000
        self.chunk_overlap = 200
        self.embedding = llama
        self.summaries = ""
        self.results = ""
        self.vectordb = ElasticsearchStore(
            es_api_key=os.environ['ES_API_KEY'],
            index_name=self.index_name,
            es_url=os.environ['ES_URL'],
            embedding=self.embedding)

    def list_all_files(self):
        return list(set([x['_source']['metadata']['source'].rsplit('/', 1)[1] for x in self.get_all_metadata()]))

    def return_documents_as_a_list(self):
        return [Document(page_content=x['_source']['text'], metadata={x['_source']['source']}) for x in
                self.get_all_metadata()]

    def add_a_directory_to_database(self, txt_directory, *args):
        loader = self.DirectoryLoader(path=txt_directory, show_progress=True, use_multithreading=True)
        self.add_a_loader_to_database(loader=loader, *args)

    def add_missing_document_to_database(self, *args):
        filenames_directory = os.listdir(self.txt_directory)
        filenames_database = self.list_all_files()

        for filename in filenames_directory:
            filename = self.txt_directory + filename
            filename_without_path = filename.rsplit('/', 1)[1]
            if filename_without_path in filenames_database:
                print(f"filename {filename_without_path} already in the database")
            else:
                print(f"filename {filename_without_path} not in the database")
                self.add_or_delete_a_document(*args, filepath=filename, method='Add')

    def add_or_delete_a_document(self, *args, filepath, method=None):
        print(filepath)
        if method == 'Add':
            if filepath.endswith('.md'):
                loader = document_loaders.TextLoader(filepath)
            elif filepath.endswith('.csv'):
                loader = document_loaders.CSVLoader(filepath)
            elif filepath.endswith('.html'):
                loader = document_loaders.UnstructuredHTMLLoader(filepath)
            elif filepath.endswith('.json'):
                loader = document_loaders.JSONLoader(filepath)
            else:
                loader = document_loaders.UnstructuredFileLoader(filepath)
            self.add_a_loader_to_database(*args, loader=loader)
        elif method == 'Delete':
            records = self.get_all_metadata()
            ids_to_delete = []
            names = filepath.split("/")
            if len(names) == 2:
                if "pdf" in names[1]:
                    path = "./Database/" + names[0] + "/Files/header_footer_remove/" + names[1]
                    if os.path.exists(path):
                        os.remove(path)
                name = names[1]
                if "pdf" in names[1]:
                    name = name.replace("pdf", "md")
                path_2 = "./Database/" + names[0] + "/preprocessing_outputs/" + name
                if os.path.exists(path_2):
                        os.remove(path_2)
                for r in records:
                    print(r)
                    id = r['_id']
                    if r['_source']['metadata']['source'] == path_2:
                        ids_to_delete.append(id)
    
                if len(ids_to_delete) > 0:
                    print("document has been found and deleted")
                    self.vectordb.delete(ids=ids_to_delete)
                else:
                    print("no document found, nothing has been deleted")
            else:
                print("path is not in correct format")
        else:
            print("none or unknown method given")

    def add_a_loader_to_database(self, *args, loader):
        document = loader.load()
        self.add_a_document_to_database(*args, document=document)

    def process_document_using_Raptor(self, texts):
        leaf_texts = [doc.page_content for doc in texts]
        self.results = Raptor.recursive_embed_cluster_summarize(leaf_texts, level=1, n_levels=3)
        all_texts = leaf_texts.copy()

        for level in sorted(self.results.keys()):
            self.summaries = self.results[level][1]["summaries"].tolist()
            all_texts.extend(self.summaries)
            text = Document(page_content=self.summaries[0], metadata=texts[0].metadata)
            texts.append(text)

        return texts

    def get_all_metadata(self):
        metadata_list = []

        # Define the query to retrieve all documents
        query = {
            "query": {
                "match_all": {}
            }
        }

        # Use scan to handle large result sets efficiently
        for doc in scan(self.vectordb.client, index=self.index_name, query=query):
            metadata_list.append(doc)

        return metadata_list

    def add_a_document_to_database(self, *args, document):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap,
                                                       is_separator_regex=False, separators=["\n\n", '```', '\n'])

        texts = text_splitter.split_documents(document)

        for arg in args:
            print(f"arg {arg} requested")
            if arg == 'Raptor':
                texts = self.process_document_using_Raptor(texts)

        ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, text.page_content)) for text in texts]
        unique_ids = list(set(ids))
        # data = self.vectordb.get()
        data = self.get_all_metadata()

        seen_ids = [doc['_id'] for doc in data]
        unique_texts = []
        unique_ids = []

        for text, id in zip(texts, ids):
            if id not in seen_ids:
                seen_ids.append(id)
                unique_texts.append(text)
                unique_ids.append(id)

        if len(unique_texts) > 0:
            print("adding document to the DB")
            self.vectordb.add_documents(documents=unique_texts, ids=unique_ids)
            print("document added to the DB")


if __name__ == "__main__":
    print("done")

