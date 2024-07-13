
# this software is manly derivated from the example found at this link https://github.com/rubentak/Langchain/blob/main/notebooks/Langchain_doc_chroma.ipynb

from langchain_openai import ChatOpenAI, OpenAI
from langchain.chains import RetrievalQA

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.agents import Tool, AgentExecutor, initialize_agent, create_structured_chat_agent
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMMathChain

# RAG prompt
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from langchain.tools.base import StructuredTool
from langchain_core.pydantic_v1 import BaseModel, Field

from langchain.retrievers import MergerRetriever

import streamlit as st
import re
from Database import ElasticSearch
from langchain import HuggingFaceHub
from langchain_huggingface import HuggingFacePipeline
from transformers import BitsAndBytesConfig
from langchain_community.llms import VLLM, LlamaCpp
from langchain_openai import ChatOpenAI


"""
try:
    from traceloop.sdk import Traceloop
    Traceloop.init(app_name="chroma_app",api_key=st.secrets['llmetry_api_key'], disable_batch=True)
except ImportError:
    print("Traceloop not available")
"""


import os

class ChatController(object):
    def __init__(self):
        self._create_chat_agent()
        self.init_qa_function()
        self.retrieved_context = ""
        
    def _create_chat_agent(self):
        self.use_private_data = False
        self.model = "RAG-Llama3-70B"
        self.retriever_output_number = 15 #default value is 15
        self.vectordb = ElasticSearch(txt_directory = './Database/Public/preprocessing_outputs/', index_name='public_db')
        self.vectordb_private = ElasticSearch(txt_directory = './Database/Private/preprocessing_outputs/', index_name='private_db')
        self.vectordb_raptor = ElasticSearch(txt_directory = './Database/Raptor/preprocessing_outputs/', index_name='raptor_db')
        self.agent_prompt = """Assistant is a large language model trained by OpenAI.

            Respond to the human as helpfully and accurately as possible. You have access to the following tools:

            {tools}

            Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).
            Valid "action" values: "Final Answer" or {tool_names}

            Provide only ONE action per $JSON_BLOB, as shown:

            ```
            {{
              "action": $TOOL_NAME,
              "action_input": $INPUT
            }}
            ```

            Follow this format:

            Question: input question to answer
            Thought: consider previous and subsequent steps
            Action:
            ```
            $JSON_BLOB
            ```
            Observation: action result
            ... (repeat Thought/Action/Observation N times)
            Thought: I know what to respond
            Action:
            ```
            {{
              "action": "Final Answer",
              "action_input": "Final response to human"
            }}

            Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly and use your own knowledge if appropriate. 
            Format is Action:```$JSON_BLOB```then Observation 
            """

        self.rag_prompt = None
        self.use_agent = False
        self.message_history = []
        self.rag_chain = None
        self.use_Raptor = False
        self.update_llm = ""
    
    def init_qa_function(self):
        
        # retriever function can be test with this kind of example: docs = retriever.get_relevant_documents("How to use TTC 500 external RAM")
        retriever = self.vectordb.vectordb.as_retriever(search_kwargs={"k": self.retriever_output_number})
        retriever_private = self.vectordb_private.vectordb.as_retriever(search_kwargs={"k": self.retriever_output_number})
        retriever_raptor = self.vectordb_raptor.vectordb.as_retriever(search_kwargs={"k": self.retriever_output_number})
        
        #Set up the turbo LLM
        # turbo_llm = ChatOpenAI(
        #     openai_api_key = self.api_key,
        #     temperature=0,
        #     model_name=self.llm_model
        #     #max_tokens = 4096 - 500
        # )
        #turbo_llm = self.model
        #turbo_llm = ChatOpenAI(model_name=self.model, openai_api_key='no-key', openai_api_base='http://localhost:8864/v1', temperature=0, stop=['<|eot_id|>', '<|end_of_text|>'], max_tokens=1000)
        if 'gpt' in self.model.lower():
            turbo_llm = ChatOpenAI(model_name=self.model, openai_api_key=os.environ['OPENAI_API_KEY'], temperature=0, max_tokens=1000)
        else:
            turbo_llm = ChatOpenAI(model_name=self.model, openai_api_key=os.environ['OPENAI_API_KEY'], openai_api_base=os.environ['OPENAI_API_BASE'], temperature=0, stop=['<|eot_id|>', '<|end_of_text|>'], max_tokens=1000)
            

        # PROMPT = PromptTemplate(
        #     template=self.retrieval_prompt, input_variables=["context", "question"]
        # )
        PROMPT = ChatPromptTemplate.from_messages([
            ("system", """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. The context is in markdown format in which image cations are formatted as [image_id.png](image_caption), for example [0_image_1_1234.png](This is an image); and tables are formatted as [table_id] json_content [/table_id], for example [table_0][{{0: 'header_0', 1: 'header_1'}}, {{0: 'value_0_0', 1: 'value_0_1'}}, {{0: 'value_1_0', 1: 'value_1_1'}}][/table_0].
Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
If you refer to any images or tables, you must refer their tags, for example: [0_image_1_1234.png], [table_0]."""),
            ("human", "Context: {context}\nQuestion: {question}"),
        ])


        chain_type_kwargs = {"verbose": True, "prompt": PROMPT}

        def format_docs(docs):
            context = " <chunk_seperator> ".join(doc.page_content for doc in docs)
            self.retrieved_context = context
            
            return context
            
        self.rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | PROMPT
            | turbo_llm
            | StrOutputParser()
        )
        
        if self.use_private_data == True:
            # We just pass a list of retrievers.
            retriever = MergerRetriever(retrievers=[retriever, retriever_private])
        if self.use_Raptor == True:
            retriever = retriever_raptor
            

          
        # Create the chain to answer questions
        qa_chain = RetrievalQA.from_chain_type(llm=turbo_llm,
                                          chain_type="stuff",
                                          retriever=retriever,
                                          chain_type_kwargs=chain_type_kwargs,
                                          return_source_documents=False,
                                          verbose=True)
                                            

        math_chain = LLMMathChain.from_llm(llm=turbo_llm)

        class Document_inputs(BaseModel):
            """Inputs to the document tool."""

            input: str = Field(
                description="query to look up in tool"
            )


        Document_tool = StructuredTool(
            name="Document tool",
            func=self.rag_chain.invoke,
            description="Use this tool when you need to answer question about technical products.",
            args_schema=Document_inputs
        )

        tools = [
            Document_tool, 
            
            # Tool(
            #     name="math chain",
            #     func=math_chain.run,
            #     description="useful when you need to do some math calculation."
            # ),
        ]
        
        prompt = hub.pull("hwchase17/structured-chat-agent")
        
        prompt.messages[0].prompt.template = self.agent_prompt
        agent = create_structured_chat_agent(
            llm=turbo_llm,
            tools=tools,
            prompt=prompt
        )
        
        
        self.chat_agent = AgentExecutor(
            agent=agent, tools=tools,
            verbose=True, 
            #memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True),
            handle_parsing_errors=True
        )
        
        if self.use_agent == False:
            # self.chat_agent = qa_chain
            self.chat_agent = self.rag_chain



    # wrapper function
    def update_llm_model(self, text):
        print(f"update {text}")
        self.update_llm = self.update_llm + " / " + text

    # function needed to bypass streamlit limitation
    def do_update(self):
        if self.update_llm_model != "":
            self.init_qa_function()
            self.update_llm = ""
            print(f"------------------------------")
            #print(self.chat_agent)
            print(self.model)
            print(self.use_agent)
            print(self.retriever_output_number)

    
    def ask(self, query = ""):
        
        if self.use_agent == False:
            llm_response = self.chat_agent.invoke(query)
            print(llm_response)
            # llm_response = llm_response['result']
        else:
            llm_response = self.chat_agent.invoke({"input": query})['output']
            print(llm_response)

        
        return llm_response
        
        
if __name__ == "__main__":
    chat = ChatController()
    chat.use_agent = True
    chat.use_Raptor = True
    # chat.retriever_output_number=10
    chat.vectordb_raptor.add_missing_document_to_database()
    #chat.init_qa_function()
    print("done")
    # raptor test
    """
    leaf_texts = chat.vectordb.return_documents_as_a_list()
    results = Raptor.recursive_embed_cluster_summarize(leaf_texts, level=1, n_levels=3)
    # Initialize all_texts with leaf_texts
    all_texts = leaf_texts.copy()

    # Iterate through the results to extract summaries from each level and add them to all_texts
    for level in sorted(results.keys()):
        # Extract summaries from the current level's DataFrame
        summaries = results[level][1]["summaries"].tolist()
        # Extend all_texts with the summaries from the current level
        all_texts.extend(summaries)

    
    from langchain_community.vectorstores import Chroma
    import ChromaDB
    chroma_db_directory = './Database/Raptor/Chroma_DB/'
    vectorstore = Chroma.from_texts(texts=all_texts, persist_directory=chroma_db_directory, embedding=ChromaDB.EMBEDDING_MODEL)
    retriever = vectorstore.as_retriever()
    # Prompt
    prompt = hub.pull("rlm/rag-prompt")


    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Set up the turbo LLM
    model = ChatOpenAI(
        openai_api_key = ChromaDB.API_KEY,
        temperature=0,
        model_name="gpt-4-turbo"
    )

    # Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    # Question
    rag_chain.invoke("How to define a RAG chain? Give me a specific code example.")
    """
    #chat.ask("How to use TTC 500 external RAM in C ?")
    #chat.ask("How to init and get data from analog inputs on TTC 500 in C ?")
    #chat.ask('how to use PWM outputs on the TTC500 in C ?')
    #chat.rag_chain.invoke('how to use PWM outputs on the TTC500 in C ?')
    #chat.ask('can you do 5 x 5 + 2 x 2 ?')
    #chat.ask('what combinations can be done with HDA 7000 ?')
    #chat.ask("How to use IO link on HMG 4000 ? Can it be used on HMG 3010 too ?")
    #chat.vectordb.add_or_delete_a_document(filepath = 'PDF_private\\Configurator.xlsx', method = 'Delete')
    #chat.vectordb.add_or_delete_a_document(filepath = 'PDF_private\\2300_PxPanic() and PxAbort().txt', method = 'Delete')
    # chat.vectordb.return_documents_as_a_list()
    chat.vectordb.add_missing_document_to_database()
    chat.ask("How to init and get data from analog inputs on TTC 500 in C ?")
    #chat.ask("What information does the `diag_state` field provide in the diagnostic state machine's context?")
    # chat.ask("Describe collaboration diagram in Driver Safety Configuration ?")
    #chat.vectordb.add_a_directory_to_chroma_database(txt_directory = chat.vectordb.txt_directory)
