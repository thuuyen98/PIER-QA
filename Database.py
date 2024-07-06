# this software is mainly derivated from the example found at the following link https://github.com/rubentak/Langchain/blob/main/notebooks/Langchain_doc_chroma.ipynb

from langchain_community.vectorstores import Chroma
import os
from langchain_community.vectorstores import ElasticsearchStore
import uuid
import Raptor as Raptor
from HFEmbeddings import LlamaCppEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from elasticsearch.helpers import scan

llama = LlamaCppEmbeddings(model_path="./Model/gte-qwen2-7b-instruct-q5_k_m.gguf", n_gpu_layers=9999)
llama.client.verbose = False

# from langchain_community.embeddings import LlamaCppEmbeddings

# streamlit bug fix
# try:
#     __import__('pysqlite3')
#     import sys
#     sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# except:
#     print("pysqlite not available")

# API_KEY = os.environ["API_KEY"]
# EMBEDDING_MODEL = OpenAIEmbeddings(openai_api_key=API_KEY, model="Alibaba-NLP/gte-large-en-v1.5", openai_api_base='https://api.runpod.ai/v2/vkvvh0b2wzexfi/openai/v1', tiktoken_enabled=False, show_progress_bar=True)

# model_name = "Alibaba-NLP/gte-large-en-v1.5"
# model_kwargs = {'device': 'cuda', 'trust_remote_code':True,
#                 # 'model_kwargs': {'torch_dtype': torch.float16}
#                }
# encode_kwargs = {'normalize_embeddings': True, 'batch_size': 1}
# hf_embedding = HFEmbeddings(
#     model_name=model_name,
#     model_kwargs=model_kwargs,
#     encode_kwargs=encode_kwargs,
#     show_progress=True,
# )


# EMBEDDING_MODEL = OpenAIEmbeddings(openai_api_key = API_KEY, model = "text-embedding-3-large")


# embeddings = SentenceTransformerEmbeddings(model_name="Alibaba-NLP/gte-large-en-v1.5")
class ChromaDb(object):
    def __init__(self, txt_directory='./Database/Public/Files/', chroma_db_directory='./Database/Public/Chroma_DB/'):

        # init some variables
        self.DirectoryLoader = DirectoryLoader
        self.FileLoader = TextLoader

        # self.api_key = API_KEY
        self.txt_directory = txt_directory  # use '\\' instead of '/' cause chroma db replaces all '/' which leads some function like delete docu to not work properly
        self.chroma_db_directory = chroma_db_directory
        self.chunk_size = 1000  # this value shall be constant for a database. If it is modified for an already existing database, it will lead to duplicates in the database
        self.chunk_overlap = 200  # this value shall be constant for a database. If it is modified for an already existing database, it will lead to duplicates in the database
        # self.embedding = EMBEDDING_MODEL
        self.embedding = llama
        self.summaries = ""
        self.results = ""
        self.vectordb = Chroma(persist_directory=self.chroma_db_directory, embedding_function=self.embedding)
        # self.vectordb.delete_collection()
        # self.db = ElasticsearchStore.from_documents(docs, self.embedding, es_url="http://localhost:9200", index_name="test-basic",)

    # goal is to loop the DB and get a list with unique source seen
    def list_all_files(self):
        files = self.vectordb.get()['metadatas']
        seen_sources = set()
        unique_data = []

        for item in files:
            if item['source'] not in seen_sources:
                # st.write(item['source'])
                unique_data.append(item)
                filename = item['source'].replace('/', '\\').rsplit('\\', 1)[1]
                seen_sources.add(filename)
        seen_sources = list(seen_sources)
        # print(seen_sources)
        return seen_sources

    # simple wrapper function if a list of text is needed
    def return_documents_as_a_list(self):
        return list(self.vectordb.get()['documents'])

    # this function load all the document in the folder txt_directory, 
    # it will perform a id verification, meaning that if a newest version is added, it will added to the database too
    def add_a_directory_to_database(self, txt_directory, *args):
        # this function will load all the content of folder into a list. 
        # A good example can be found at https://python.langchain.com/docs/integrations/document_loaders/unstructured_file.html
        loader = self.DirectoryLoader(path=txt_directory, show_progress=True, use_multithreading=True)
        self.add_a_loader_to_database(loader=loader, *args)

    # this function will add all missing document to the database, aim is to be faster than loaded the whole directory
    def add_missing_document_to_database(self, *args):
        # this function will load all the content of folder into a list. 
        # A good example can be found at https://python.langchain.com/docs/integrations/document_loaders/unstructured_file.html

        # get a list of all files in the directory
        filenames_directory = os.listdir(self.txt_directory)

        # get a list of all files in the vector database
        filenames_database = set(self.list_all_files())

        # loop directory filename and check if name exists in database
        for filename in filenames_directory:
            # add folder name
            # filename = self.txt_directory.replace('/', '\\') + filename
            filename = self.txt_directory + filename
            filename_without_path = filename.rsplit('/', 1)[
                1]  # keep filename and remove the rest. Split name with delimeter and save the result in a 2 items array
            if filename_without_path in filenames_database:
                print(f"filename {filename_without_path} already in the database")
            else:
                print(f"filename {filename_without_path} not in the database")
                self.add_or_delete_a_document(*args, filepath=filename, method='Add')

    # do no forget the method
    def add_or_delete_a_document(self, *args, filepath, method=None):
        # add method
        print(filepath)
        if method == 'Add':
            loader = self.FileLoader(filepath)
            self.add_a_loader_to_database(*args, loader=loader)
        # delete method
        elif method == 'Delete':

            # get current data

            data = self.vectordb.get()

            # get source of current database
            seen_source = list(data.get('metadatas'))

            # print(seen_source)
            ids_to_delete = []

            for idx in range(len(data['ids'])):
                id = data['ids'][idx]
                # metadata = data['metadatas'][idx]
                # if metadata['source'] == filepath:
                ids_to_delete.append(id)

            if len(ids_to_delete) > 0:
                print("document has been found and deleted")
                self.vectordb.delete(ids=ids_to_delete)
            else:
                print("no document found, nothing has been deleted")
            # Save the db locally to disk
            self.vectordb.persist()

        # else print a warning
        else:
            print("none or unknow method given")

    # simple function to 
    def add_a_loader_to_database(self, *args, loader):
        document = loader.load()
        # print(type(document))
        # print("document:+++++++++++++++++++++++++++")
        # print(document)
        self.add_a_document_to_database(*args, document=document)

    # function to pre process document using RAG Raptor
    def process_document_using_Raptor(self, texts):
        leaf_texts = [doc.page_content for doc in texts]
        self.results = Raptor.recursive_embed_cluster_summarize(leaf_texts, level=1, n_levels=3)
        # Initialize all_texts with leaf_texts
        all_texts = leaf_texts.copy()

        # Iterate through the results to extract summaries from each level and add them to all_texts
        for level in sorted(self.results.keys()):
            # Extract summaries from the current level's DataFrame
            self.summaries = self.results[level][1]["summaries"].tolist()
            # Extend all_texts with the summaries from the current level
            all_texts.extend(self.summaries)
            text = Document(page_content=self.summaries[0], metadata=texts[0].metadata)
            texts.append(text)

        return texts

    # a loader can be a directory, a single file or whatever ...
    # this function will check if the loader (or the file) is already in the database and it only is it is missing, avoid duplicates
    def add_a_document_to_database(self, *args, document):
        # Splitting the text into chunks
        # increase efficiency of embeddings searching function
        # some explanation can be found here https://dev.to/peterabel/what-chunk-size-and-chunk-overlap-should-you-use-4338
        # overlap is to avoid to split data in a middle on an important sentence
        # print("document length: ")
        # print(document)
        # print(len(document))
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap,
                                                       is_separator_regex=False, separators=["\n\n", '```', '\n'])

        # markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")], strip_headers=False)
        # document = markdown_splitter.split_text(document[0].page_content)
        texts = text_splitter.split_documents(document)
        # for text in texts:
        #     print(text.page_content)
        #     print('============================')
        # print(len(texts))
        # print(texts[:2])

        # RAPTOR
        for arg in args:
            print(f"arg {arg} requested")
            if arg == 'Raptor':
                texts = self.process_document_using_Raptor(texts)
                # for text, leaf_text in zip(texts, leaf_texts):
                #    text.page_content = leaf_text

        # generate unique id to add only missing texts
        # found on following link : https://stackoverflow.com/questions/76265631/chromadb-add-single-document-only-if-it-doesnt-exist
        ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, text.page_content)) for text in texts]
        unique_ids = list(set(ids))
        data = self.vectordb.get()

        # get ids of current database
        seen_ids = list(set(data.get('ids')))
        # print("seen_ids")
        # print(seen_ids)
        unique_texts = []
        unique_ids = []  # List to collect unique IDs

        # this line compares ids of text and database
        for text, id in zip(texts, ids):
            if id not in seen_ids:
                seen_ids.append(id)
                unique_texts.append(text)
                unique_ids.append(id)
        # print("seen_ids-NEW")
        # print(seen_ids)
        if len(unique_texts) > 0:
            print("adding document to the DB")
            self.vectordb.add_documents(documents=unique_texts,
                                        ids=unique_ids,
                                        collection_metadata={"hnsw:space": "cosine"})

            # Save the db locally to disk
            self.vectordb.persist()
            print("document added to the DB")




class ElasticSearch(object):
    def __init__(self, txt_directory='./Database/Public/Files/'):

        # init some variables
        self.DirectoryLoader = DirectoryLoader
        self.FileLoader = TextLoader

        self.txt_directory = txt_directory
        self.index_name = 'elastic_db'
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
            loader = self.FileLoader(filepath)
            self.add_a_loader_to_database(*args, loader=loader)
        elif method == 'Delete':
            records = self.get_all_metadata()

            for r in records:
                if r['_source']['metadata']['source'] == filepath:
                    ids_to_delete.append(idx)

            if len(ids_to_delete) > 0:
                print("document has been found and deleted")
                self.vectordb.delete(ids=ids_to_delete)
            else:
                print("no document found, nothing has been deleted")
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
# filename BAHLB1400_21.10.2019_D_E.md not in the database

# filename EN_HFT_Protokollbeschreibung_VFL CANopen_2021-10-25_D.md not in the database

# filename HY-TTC_500_IO_Driver_Manual_V3.4.1.md not in the database
