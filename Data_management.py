
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
# from langchain_community.llms import GPT4All
#from gpt4all_code import GPT4All
# from Database import ChromaDb
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

#streamlit bug fix
import os

# try:
#     __import__('pysqlite3')
#     import sys
#     sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# except:
#     print("pysqlite not available")


class ChatController(object):
    def __init__(self):
        self._create_chat_agent()
        self.init_qa_function()
        self.retrieved_context = ""
        
    def _create_chat_agent(self):

        # init some variables
        #self.api_key = API_KEY # open ai api key shall be created in openai website
        self.use_private_data = False
        #self.llm_model = "gpt-4o"#"gpt-4o"
        # self.model_kwargs={'stop': ['<|eot_id|>', '<|end_of_text|>']}
        self.model = "../rag/merged/ggml-model-Q6_K_M.gguf"
        # self.model = LlamaCpp(model_path='./Model/qwen2-7b-instruct-q6_k.gguf', n_gpu_layers=999, n_ctx=7000, verbose=True, stop=['<|eot_id|>', "<|end_of_text|>", "<|im_end|>"], rope_freq_base=0, temperature=0, max_tokens=1000)
        # self.model = GPT4All(model='./Model/Llama3-ChatQA-1.5-8B-Q6_K.gguf')
        #self.model = HuggingFaceHub(repo_id='dranger003/SFR-Embedding-Mistral-GGUF', model_kwargs={"temperature":0, "max_length":64})
        # quantization_config = BitsAndBytesConfig(
        #     load_in_4bit=True,
        #     bnb_4bit_quant_type="nf4",
        #     bnb_4bit_compute_dtype="float16",
        #     bnb_4bit_use_double_quant=True
        # )
        # self.model = HuggingFacePipeline.from_model_id(
        #     model_id='Qwen/Qwen2-72B-Instruct',
        #     task="text-generation",
        #     model_kwargs={"quantization_config": quantization_config, "device_map": "auto"},
        #     device=None,
        #     # device_map='auto',
        #     pipeline_kwargs=dict(
        #         max_new_tokens=1024,
        #         do_sample=False,
        #         temperature=0,
        #     ),
        # )
        # self.model = VLLM(
        #     model="Qwen/Qwen2-72B-Instruct-GPTQ-Int4",
        #     trust_remote_code=True,  # mandatory for hf models
        #     max_new_tokens=1000,
        #     tensor_parallel_size=2,
        #     temperature=0,
        #     vllm_kwargs={"max_model_len": 3000, 'quantization': 'gptq', 'gpu_memory_utilization': 1}
        # )
        self.retriever_output_number = 10 #default value is 4
        # self.vectordb = ChromaDb(txt_directory = './Database_new/Public/Files/', chroma_db_directory = './Database_new/Public/ES/')
        # self.vectordb_private = ChromaDb(txt_directory = './Database_new/Private/Files/', chroma_db_directory = './Database_new/Private/ES/')
        # self.vectordb_raptor = ChromaDb(txt_directory = './Database_new/Raptor/Files/', chroma_db_directory = './Database_new/Raptor/ES_old/')
        
        self.vectordb = ElasticSearch(txt_directory = './Database_new/Public/Files/')
        self.vectordb_private = ElasticSearch(txt_directory = './Database_new/Private/Files/')
        self.vectordb_raptor = ElasticSearch(txt_directory = './Database_new/Raptor/Files/')
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
#         self.retrieval_prompt = """You are an assistant for question-answering tasks. 
# Use the following pieces of retrieved context to answer the question. 
# If you don't know the answer, just say that you don't know. 
# Attention: If your answer relates to any image description given below, you should refer to the image ID in your answer. The image id is in format [image_id.png] . For example [0_image_0.png]
# Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.

# Question: {question}

# Context: {context}

# Answer:"""
#         self.retrieval_prompt = """<|im_start|>system
# You are an assistant for question-answering tasks. 
# Use the following pieces of retrieved context to answer the question. The context is in markdown format.
# If you don't know the answer, just say that you don't know. 
# Attention: If your answer relates to any image description given below, you should refer to the image ID in your answer. The image id is in format [image_id.png] . For example [0_image_0.png]
# Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
# Context: {context}<|im_end|>
# <|im_start|>user
# {question}<|im_end|>
# <|im_start|>assistant
# """
        self.retrieval_prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. The context is in markdown format in which image cations are formatted as [image_id.png](image_caption), for example [0_image_1.png](This is an image); and tables are formatted as [table_id] json_content [/table_id], for example [table_0][{{0: 'header_0', 1: 'header_1'}}, {{0: 'value_0_0', 1: 'value_0_1'}}, {{0: 'value_1_0', 1: 'value_1_1'}}][/table_0].
Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
At the end of your answer, include the following sections if applicable, otherwise do not include it:
### Relevant images: list of images ids from the context in the given format that are most related or mentioned to your answer, each id in one line. For example:
[image_0.png]
[image_1.png]

### Relevant tables: list of tables ids from the context in the given format that are most related or mentioned to your answer. Each table in one line. For example:
[table_0]
[table_1]
<|eot_id|><|start_header_id|>user<|end_header_id|>

Context: {context}

Quesion: {question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""



#         self.retrieval_prompt = """
# You are an assistant for question-answering tasks. 
# Use the following pieces of retrieved context to answer the question. The context is in markdown format.
# If you don't know the answer, just say that you don't know. 
# Attention: If your answer relates to any image description given below, you should refer explicitly to the image ID in your answer with the format [image_id.png].
# Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
# Context: {context}

# Question:{question}
# """
#         self.retrieval_prompt = """System: You are an assistant for question-answering tasks. 
# Use the following pieces of retrieved context to answer the question. 
# If you don't know the answer, just say that you don't know. 
# Attention: If your answer relates to any image description given below, you should refer to the image ID in your answer. The image id is in format [image_id.png] . For example [0_image_0.png]
# Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.

# Context:
# {context}

# User: {question}

# Assistant:"""

        self.rag_prompt = None
        self.use_agent = False
        self.message_history = []
        self.rag_chain = None
        self.use_RAG = False
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
        turbo_llm = ChatOpenAI(model_name=self.model, openai_api_key='idjscmdsnc', openai_api_base='https://primary-unbiased-sunbird.ngrok-free.app/v1', temperature=0, stop=['<|eot_id|>', '<|end_of_text|>'], max_tokens=1000)

        PROMPT = PromptTemplate(
            template=self.retrieval_prompt, input_variables=["context", "question"]
        )
#         PROMPT = ChatPromptTemplate.from_messages([
#             ("system", """You are an assistant for question-answering tasks. 
# Use the following pieces of retrieved context to answer the question. The context is in markdown format in which image cations are formatted as [image_id.png](image_caption), for example [0_image_1.png](This is an image); and tables are formatted as [table_id] json_content [/table_id], for example [table_0][{{0: 'header_0', 1: 'header_1'}}, {{0: 'value_0_0', 1: 'value_0_1'}}, {{0: 'value_1_0', 1: 'value_1_1'}}][/table_0].
# Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
# At the end of your answer, include the following sections if applicable:
# ### Relevant images: list of all images ids from the context in the given format that are directly related or mentioned to your answer. Each id in one line. For example:
# [image_0.png]
# [image_1.png]

# ### Relevant tables: list of all tables ids AND their contents from the context in the given format that are directly related or mentioned to your answer. Each table in one line. For example:
# [table_0][{{0: 'header_0', 1: 'header_1'}}, {{0: 'value_0_0', 1: 'value_0_1'}}, {{0: 'value_1_0', 1: 'value_1_1'}}][/table_0]
# [table_1][{{0: 'header_2', 1: 'header_3'}}, {{0: 'value_2_0', 1: 'value_2_1'}}, {{0: 'value_3_0', 1: 'value_3_1'}}][/table_1]"""),
#             ("human", "Context: {context}\nQuestion: {question}"),
#         ])


        chain_type_kwargs = {"verbose": True, "prompt": PROMPT}


        #RAG
        # prompt = hub.pull("rlm/rag-prompt")
        # self.rag_prompt = prompt.messages[0].prompt.template

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
        
        
        # if self.use_private_data == True:
        #     # We just pass a list of retrievers.
        #     retriever = MergerRetriever(retrievers=[retriever, retriever_private])
        # if self.use_Raptor == True:
        #     retriever = retriever_raptor
            
          
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

        if self.use_RAG == True:
            Document_tool = StructuredTool(
                name="Document tool",
                func=self.rag_chain.invoke,
                description="Use this tool when you need to answer question about technical products.",
                args_schema=Document_inputs
            ) 
        else:
            Document_tool = StructuredTool(
                name="Document tool",
                func=qa_chain.invoke,
                description="Use this tool when you need to answer question about technical products.",
                args_schema=Document_inputs
            )

        tools = [
            Document_tool, 
            
            Tool(
                name="math chain",
                func=math_chain.run,
                description="useful when you need to do some math calculation."
            ),
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
            print(self.llm_model)
            print(self.use_agent)
            print(self.retriever_output_number)

    
    def ask(self, query = ""):
        
        if self.use_agent == False:
            llm_response = self.chat_agent.invoke(query)
            print(llm_response)
            # llm_response = llm_response['result']
        else:
            llm_response = self.chat_agent.invoke({"input": query})
            print(llm_response)
            llm_response = llm_response['output']
            #length = len(llm_response.get('chat_history')) - 1
            #llm_response = llm_response.get('chat_history')[length].content
        
        return llm_response
        
        
if __name__ == "__main__":
    chat = ChatController()
    chat.use_agent = False
    #chat.use_Raptor = True
    # chat.vectordb_raptor.add_missing_document_to_chroma_database('Raptor')
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

# s = """[table_7][{0: 'Here are the data structures with brief descriptions: bl_apdb_ APDB structure', 1: '14', 2: '', 3: ''}, {0: 'bl_t_can_id_', 1: 'CAN ID structure', 2: '', 3: '19'}, {0: 'bl_t_date_', 1: 'Date structure', 2: '', 3: '20'}, {0: 'diag_errorcode_ Diagnostic error code structure', 1: '', 2: '21', 3: ''}, {0: 'io_adc_safety_conf_ Safety configuration for the ADC inputs', 1: '', 2: '22', 3: ''}, {0: 'io_can_data_frame_ CAN data frame', 1: '', 2: '23', 3: ''}, {0: 'io_dio_limits_', 1: 'Voltage limits for digital inputs', 2: '', 3: '24'}, {0: 'io_do_safety_conf_ Safety configuration for the digital outputs', 1: '', 2: '25', 3: ''}, {0: 'io_driver_safety_conf_ Driver Safety Configuration', 1: '', 2: '26', 3: ''}, {0: 'io_lin_data_frame_ LIN data frame', 1: '', 2: '28', 3: ''}, {0: 'io_pwd_cnt_conf_ Edge counter configuration for the Universal PWD inputs', 1: '29', 2: '', 3: ''}, {0: 'io_pwd_cplx_conf_ Complex configuration for the Universal PWD inputs', 1: '', 2: '29', 3: ''}, {0: 'io_pwd_cplx_safety_conf_ Safety configuration for the Complex PWD inputs', 1: '', 2: '30', 3: ''}, {0: 'io_pwd_inc_conf_ Incremental configuration for the Universal PWD inputs', 1: '31', 2: '', 3: ''}, {0: 'io_pwd_inc_safety_conf_ Safety configuration for the Incremental or Counter PWD inputs', 1: '.', 2: '32', 3: ''}, {0: 'io_pwd_pulse_samples_ PWD pulse-width data structure', 1: '', 2: '33', 3: ''}, {0: 'io_pwd_universal_safety_conf_ Safety configuration for the Universal PWD inputs', 1: '', 2: '34', 3: ''}, {0: 'io_pwm_current_queue_ PWM current measurement queue', 1: '', 2: '35', 3: ''}, {0: 'io_pwm_safety_conf_ Safety configuration for the PWM outputs', 1: '', 2: '36', 3: ''}][/table_7][table_8][{0: 'Here is a list of all files with brief descriptions: APDB.h The Application Descriptor Block (APDB)', 1: '', 2: '38', 3: ''}, {0: 'DIAG_Constants.h Global defines for IO Driver diagnostic module', 1: '', 2: '41', 3: ''}, {0: 'DIAG_Functions.h Auxiliary functions for watchdog handling and Flash/RAM/CfgFlash correctable errors monitoring', 1: '75', 2: '', 3: ''}, {0: 'IO_ADC.h', 1: 'IO Driver functions for ADC', 2: '', 3: '80'}, {0: 'IO_CAN.h', 1: 'IO Driver functions for CAN communication', 2: '', 3: '95'}, {0: 'IO_DEBUG.h', 1: 'IO Driver functions for DEBUG utilities', 2: '', 3: '111'}, {0: 'IO_DIO.h', 1: 'IO Driver functions for Digital Input/Output', 2: '', 3: '116'}, {0: 'IO_DOWNLOAD.h IO Driver functions for handling Ethernet download requests', 1: '. . .', 2: '130', 3: ''}, {0: 'IO_Driver.h', 1: 'High level interface to IO Driver', 2: '', 3: '133'}, {0: 'IO_EEPROM.h', 1: 'IO Driver functions for external EEPROM/FRAM', 2: '153', 3: ''}, {0: 'IO_Error.h', 1: 'Global error defines for IO driver', 2: '159', 3: ''}, {0: 'IO_FLASH.h', 1: 'IO Driver functions for handling the external flash', 2: '', 3: '183'}, {0: 'IO_LIN.h', 1: 'IO Driver functions for LIN communication', 2: '195', 3: ''}, {0: 'IO_MPU.h', 1: 'IO Driver functions for the Memory Protection Unit (MPU)', 2: '201', 3: ''}, {0: 'IO_Pin.h', 1: 'This header file contains pin definitions for the I/O driver, and aliases for the pins 214', 2: '', 3: ''}, {0: 'IO_POWER.h', 1: 'IO Driver functions for Power IC control', 2: '', 3: '279'}, {0: 'IO_PVG.h', 1: 'IO Driver functions for PVG channels', 2: '', 3: '288'}, {0: 'IO_PWD.h', 1: 'IO Driver functions for timer input channels', 2: '', 3: '294'}][/table_8][table_9][{0: 'IO_PWM.h', 1: 'IO Driver functions for PWM channels', 2: '', 3: '320'}, {0: 'IO_RTC.h', 1: 'RTC functions, provides exact timing functions and services', 2: '. . .', 3: '332'}, {0: 'IO_UART.h', 1: 'IO Driver functions for UART communication', 2: '', 3: '341'}, {0: 'IO_UDP.h', 1: 'IO Driver functions for UDP communication', 2: '', 3: '348'}, {0: 'IO_VOUT.h', 1: 'IO Driver functions for voltage outputs', 2: '', 3: '354'}, {0: 'ptypes_apdb.h', 1: 'APDB target abstraction', 2: '', 3: '359'}, {0: 'ptypes_tms570.h Primitive data types', 1: '', 2: '361', 3: ''}][/table_9]![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)[table_7][{0: 'Here are the data structures with brief descriptions: bl_apdb_ APDB structure', 1: '14', 2: '', 3: ''}, {0: 'bl_t_can_id_', 1: 'CAN ID structure', 2: '', 3: '19'}, {0: 'bl_t_date_', 1: 'Date structure', 2: '', 3: '20'}, {0: 'diag_errorcode_ Diagnostic error code structure', 1: '', 2: '21', 3: ''}, {0: 'io_adc_safety_conf_ Safety configuration for the ADC inputs', 1: '', 2: '22', 3: ''}, {0: 'io_can_data_frame_ CAN data frame', 1: '', 2: '23', 3: ''}, {0: 'io_dio_limits_', 1: 'Voltage limits for digital inputs', 2: '', 3: '24'}, {0: 'io_do_safety_conf_ Safety configuration for the digital outputs', 1: '', 2: '25', 3: ''}, {0: 'io_driver_safety_conf_ Driver Safety Configuration', 1: '', 2: '26', 3: ''}, {0: 'io_lin_data_frame_ LIN data frame', 1: '', 2: '28', 3: ''}, {0: 'io_pwd_cnt_conf_ Edge counter configuration for the Universal PWD inputs', 1: '29', 2: '', 3: ''}, {0: 'io_pwd_cplx_conf_ Complex configuration for the Universal PWD inputs', 1: '', 2: '29', 3: ''}, {0: 'io_pwd_cplx_safety_conf_ Safety configuration for the Complex PWD inputs', 1: '', 2: '30', 3: ''}, {0: 'io_pwd_inc_conf_ Incremental configuration for the Universal PWD inputs', 1: '31', 2: '', 3: ''}, {0: 'io_pwd_inc_safety_conf_ Safety configuration for the Incremental or Counter PWD inputs', 1: '.', 2: '32', 3: ''}, {0: 'io_pwd_pulse_samples_ PWD pulse-width data structure', 1: '', 2: '33', 3: ''}, {0: 'io_pwd_universal_safety_conf_ Safety configuration for the Universal PWD inputs', 1: '', 2: '34', 3: ''}, {0: 'io_pwm_current_queue_ PWM current measurement queue', 1: '', 2: '35', 3: ''}, {0: 'io_pwm_safety_conf_ Safety configuration for the PWM outputs', 1: '', 2: '36', 3: ''}][/table_7][table_8][{0: 'Here is a list of all files with brief descriptions: APDB.h The Application Descriptor Block (APDB)', 1: '', 2: '38', 3: ''}, {0: 'DIAG_Constants.h Global defines for IO Driver diagnostic module', 1: '', 2: '41', 3: ''}, {0: 'DIAG_Functions.h Auxiliary functions for watchdog handling and Flash/RAM/CfgFlash correctable errors monitoring', 1: '75', 2: '', 3: ''}, {0: 'IO_ADC.h', 1: 'IO Driver functions for ADC', 2: '', 3: '80'}, {0: 'IO_CAN.h', 1: 'IO Driver functions for CAN communication', 2: '', 3: '95'}, {0: 'IO_DEBUG.h', 1: 'IO Driver functions for DEBUG utilities', 2: '', 3: '111'}, {0: 'IO_DIO.h', 1: 'IO Driver functions for Digital Input/Output', 2: '', 3: '116'}, {0: 'IO_DOWNLOAD.h IO Driver functions for handling Ethernet download requests', 1: '. . .', 2: '130', 3: ''}, {0: 'IO_Driver.h', 1: 'High level interface to IO Driver', 2: '', 3: '133'}, {0: 'IO_EEPROM.h', 1: 'IO Driver functions for external EEPROM/FRAM', 2: '153', 3: ''}, {0: 'IO_Error.h', 1: 'Global error defines for IO driver', 2: '159', 3: ''}, {0: 'IO_FLASH.h', 1: 'IO Driver functions for handling the external flash', 2: '', 3: '183'}, {0: 'IO_LIN.h', 1: 'IO Driver functions for LIN communication', 2: '195', 3: ''}, {0: 'IO_MPU.h', 1: 'IO Driver functions for the Memory Protection Unit (MPU)', 2: '201', 3: ''}, {0: 'IO_Pin.h', 1: 'This header file contains pin definitions for the I/O driver, and aliases for the pins 214', 2: '', 3: ''}, {0: 'IO_POWER.h', 1: 'IO Driver functions for Power IC control', 2: '', 3: '279'}, {0: 'IO_PVG.h', 1: 'IO Driver functions for PVG channels', 2: '', 3: '288'}, {0: 'IO_PWD.h', 1: 'IO Driver functions for timer input channels', 2: '', 3: '294'}][/table_8][table_9][{0: 'IO_PWM.h', 1: 'IO Driver functions for PWM channels', 2: '', 3: '320'}, {0: 'IO_RTC.h', 1: 'RTC functions, provides exact timing functions and services', 2: '. . .', 3: '332'}, {0: 'IO_UART.h', 1: 'IO Driver functions for UART communication', 2: '', 3: '341'}, {0: 'IO_UDP.h', 1: 'IO Driver functions for UDP communication', 2: '', 3: '348'}, {0: 'IO_VOUT.h', 1: 'IO Driver functions for voltage outputs', 2: '', 3: '354'}, {0: 'ptypes_apdb.h', 1: 'APDB target abstraction', 2: '', 3: '359'}, {0: 'ptypes_tms570.h Primitive data types', 1: '', 2: '361', 3: ''}][/table_9]![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)![20_image_0.png]( The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.)##indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several arrows pointing to various nodes, indicating the flow of information or data within the system. Some key elements include "canupload," "builddate," and "flashdate." In addition to these main elements, there is also a bar graph present in the image, which could be used to represent numerical data or values related to the connections between nodes. The overall structure of the diagram suggests that it depicts a complex system with interconnected components that work together to achieve specific goals or functions.The image displays a diagram with multiple connections between different elements. There are several

# ## 6.5.5 Connection 6.5.5.1 Unidirectional Single Power Stage

# Figure 67 **on this page shows the battery wiring for maximum total load current. This kind of wiring is** used to increase output current capability. It is strongly recommended to support equal distribution of current between the power supply pins. This implies to use **cables of same diameter and same** wire length in parallel. In this example all power supply pins (BAT+ and GND) are connected to cable of maximum diameter supported by the appropriate connector **pin. The cables in parallel are going**
# to a distribution point (for example in the fuse box) and from **there with a bigger diameter all the way** to the battery.

# The return pin of the motor is connected not direct to the ECU ground but to somewhere else, perhaps to the chassis. In this case significant voltage drops may occur between ECU and motor ground connection. This can lead to unexpected fluctuations **in motor voltage and motor current.**

# ![219_image_0.png](The image is a black and white diagram of an electrical circuit with multiple components labeled throughout. There are several wires connecting various parts of the circuit, including batteries, capacitors, and resistors. A green light can be seen in one part of the circuit, possibly indicating a power source or control switch. The diagram is detailed enough to show the connections between each component, providing an understanding of how the electrical system functions.)

# A better solution for achieving less voltage drop in the return path shows the Figure 68 **on the current** page.

# ![220_image_0.png](The image is a detailed diagram of an electrical circuit with various components labeled and connected to each other. There are multiple wires and connections throughout the circuit, including a battery, a motor, and a green button. Some of the key components include a switch, a resistor, and a capacitor.  The diagram is organized in such a way that it provides an overview of the entire electrical system, allowing for easy understanding of how each component works together to create the desired function. The labels on the wires and connections help identify their purpose within the circuit, making it easier to troubleshoot or modify the system as needed.)

# ## 6.5.5.2 Unidirectional Double Power Stage
# """
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import re
# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=500,
#     chunk_overlap=200,
#     # is_separator_regex=True,
#     # separators=["\\n\\n", '!\[/table_\d+\]', '!\[*\.png\]\(*\)', '```', '\\#\\#', '\\n']
# )


# texts = text_splitter.create_documents([s])
# for x in texts:
#     print(x.page_content)
#     print('======================'*3)
