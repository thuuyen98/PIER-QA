import streamlit as st
import pandas as pd
from Data_management import ChatController
from importlib.metadata import version
import re
import os
import ast
from tabulate import tabulate
from Preprocessing.data_processor import pipeline

def app_init():
    # Initialize session_state if it doesn't exist
    if 'chat' not in st.session_state:
        st.session_state['chat'] = ChatController()
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    st.session_state['db'] = 'Public'

def library_version_display():
    library_version_expander = st.expander(label='Current library versions used')

    with library_version_expander:
        st.write('streamlit version is ' + version('streamlit'))
        st.write('openai version is ' + version('openai'))
        st.write('langchain version is ' + version('langchain'))
        st.write('langchain_community version is ' + version('langchain_community'))
        
def write_files_trained_on():
    files_trained_on_expander = st.expander(label='App was trained on following files:')
    files = st.session_state.chat.vectordb.list_all_files()
    files_2 = st.session_state.chat.vectordb_private.list_all_files()
    
    with files_trained_on_expander:
        # list all files in directory
        st.write("# public database")
        for filename in files:
            st.write(f"{filename}")
        st.write()
        st.write("# private database")
        for filename in files_2:
            # display the file name in the left column
            st.write(f"{filename}")
        
def app_parameters():
    param_expander = st.expander(label='App llm parameters')
    
    with param_expander:
        # Adding a select button
        st.session_state.chat.model = st.selectbox(
                label = 'Choose a model:',
                options = ('RAG-Llama3-70B','gpt-3.5-turbo', 'gpt-4o'),
                index = 0,
                on_change =st.session_state.chat.update_llm_model, args =("llm model",))
               
        st.write('You selected:', st.session_state.chat.model)
            
        st.session_state.chat.use_agent = st.checkbox(label='Use agent', 
            value=st.session_state.chat.use_agent,
            on_change =st.session_state.chat.update_llm_model, args =("use agent",))
        
        # st.session_state.chat.use_RAG = st.checkbox(label='Use RAG', 
        #     value=st.session_state.chat.use_RAG,
        #     on_change =st.session_state.chat.update_llm_model, args =("use RAG",))

        integer_value = st.number_input(
            label='Number of documents returned by the retriever, default value is 15:',
            min_value=0,  # Minimum value
            max_value=100,  # Maximum value
            value=st.session_state.chat.retriever_output_number,  # Default value from session state
            step=1,  # Step size
            format='%d'  # '%d' as integer
        )
        # Check if the value has changed
        if integer_value != st.session_state.chat.retriever_output_number:
            st.session_state.chat.retriever_output_number = integer_value  # Update the session state
            st.session_state.chat.update_llm_model("retriever output number")
            
        # Retrieval prompt
        #st.session_state.chat.retrieval_prompt = st.text_area("retrieval prompt", st.session_state.chat.retrieval_prompt)

        # Agent prompt
        #st.session_state.chat.agent_prompt = st.text_area("agent prompt", st.session_state.chat.agent_prompt)

        # if st.button('Modify'):
        #     st.session_state.chat.update_llm_model("update prompt")

    st.session_state.chat.do_update() 

def manage_db():
    db_expander = st.expander(label='ElasticSearch management')
    
    with db_expander:

        # test to use more than one DB and a merge retriever function
        st.session_state.chat.use_private_data = st.checkbox(label='Use private database', 
            value=st.session_state.chat.use_private_data,
            on_change =st.session_state.chat.update_llm_model, args =("use private data",))
        
        # test to use Raptor DB
        st.session_state.chat.use_Raptor = st.checkbox(label='Use Raptor', 
            value=st.session_state.chat.use_Raptor,
            on_change =st.session_state.chat.update_llm_model, args =("use raptor",))
        
        # Adding a select button to choose a DB
        selected_db = st.selectbox(
                label = 'Choose a DB:',
                options = ('Public', 'Private', 'Raptor'),
                index = 0)
        
        st.write('You selected the following db:', selected_db)

        if selected_db == 'Public':
            vector_db = st.session_state.chat.vectordb
        elif selected_db == 'Private':
            vector_db = st.session_state.chat.vectordb_private
            st.session_state['db'] = 'Private'
        elif selected_db == 'Raptor':
            vector_db = st.session_state.chat.vectordb_raptor
            st.session_state['db'] = 'Raptor'

        # button to add missing files
        if st.button('Add missing files to DB'):
            pipeline(f'Database/{selected_db}/Files', f'Database/{selected_db}/preprocessing_outputs')  
            vector_db.add_missing_document_to_database()
                
        # Delete a document
        path_to_doc_to_delete = st.text_input("Document to delete (case sensitive)")

        # button to delete a document
        if st.button('Delete document'):
            vector_db.add_or_delete_a_document(filepath = path_to_doc_to_delete, method = 'Delete')

    st.session_state.chat.do_update() 



# This is the title of the app
st.title('Simple RAG App')

# layout and param
app_init()

with st.sidebar:
    library_version_display()
    write_files_trained_on()
    manage_db()
    app_parameters()
    


# User types their message into the text_input
user_input = st.text_input("Type your message here")

def format_table(table):
    res = ast.literal_eval(table)
    tuple_list = [tuple(d.values()) for d in res]
    return '\n\n' + tabulate(tuple_list, headers='firstrow', tablefmt="github") + '\n\n'
if st.button('Send'):
    # Add user's message to chat history
    st.session_state.chat_history.append(f"User: {user_input}")

    # tokenize the new input sentence
    st.session_state.chat.message_history.append({"role": "user", "content": f"{user_input}"})

    # Here, instead of echoing the user's message, you would 
    # call your chatbot function and generate a response
    reply_content = st.session_state.chat.ask(user_input)
    retrieve_table = st.session_state.chat.retrieved_context
    print("retrieve_table")
    print(retrieve_table)
    pattern_open_table = r'table_\d+'
    pattern = r'\[table_\d+\]\[.*?\]\[/table_\d+\]'
    print("reply_content")
    print(reply_content)
    table_opens = re.findall(pattern_open_table, reply_content)
    tables = re.findall(pattern, reply_content)
    print("table_opens")
    print(set(table_opens))
    print("tables")
    print(tables)
    if len(tables) > 0:
        for t in set(tables):
            if len(table_opens) > 0:
                for table in set(table_opens):
                    if table in t:
                        reply_content = reply_content.replace(t, '[' + table + ']')
    if len(table_opens) > 0:
        for table in set(table_opens):
            open_indx = retrieve_table.index('[' + table + ']')
            close_indx = retrieve_table.index('[/' + table + ']')
            reply_content = reply_content.replace('[' + table + ']', '[' + table + ']'+ format_table(retrieve_table[open_indx + len(table) + 2 : close_indx]))
                
        
    print("reply_content")
    print(reply_content)
    
    # append the new reply to the message history
    st.session_state.chat.message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    
    bot_response = f"Assistant: {reply_content}"
    print("bot_response")
    print(bot_response)
    st.session_state.chat_history.append(f"{bot_response}")

public_image_path = "./Database/Public/Files/header_footer_remove/markdown/"
private_image_path = "./Database/Private/Files/header_footer_remove/markdown/"
raptor_image_path = "./Database/Raptor/Files/header_footer_remove/markdown/"
# Assuming that chat history is arranged in question-answer-question-answer...
for i in range(len(st.session_state.chat_history)-1, -1, -2):
    st.markdown(f"<p style='color:green'>Q: {st.session_state.chat_history[i-1]}</p>", unsafe_allow_html=True)
    a = st.session_state.chat_history[i]
    st.markdown(f"A: {a}")
    pattern = r'\[\d+_image_\d+_\d+\.png]'
    # Find all occurrences of the pattern in the text
    matches = re.findall(pattern, a)
    print(matches)
    if len(matches) > 0:
        for match in set(matches):
            result = match.rsplit('_', 1)
            image_id = result[0][1:]
            image_folder = result[-1].split(".")[0]
            dir_list = os.listdir(public_image_path)
            dir_list_private = os.listdir(private_image_path)
            dir_list_raptor = os.listdir(raptor_image_path)
            final_path = None
            if image_folder in dir_list:
                final_path = public_image_path
            elif image_folder in dir_list_private:
                final_path = dir_list_private
            elif image_folder in dir_list_raptor:
                final_path = dir_list_raptor
            if final_path is not None:
                inner_folder = os.listdir(final_path + image_folder)
                st.image(final_path + image_folder + "/" + inner_folder[0] + "/" + image_id +".png", caption = match[1:-1])
 
    
# Button to clear chat history
if st.button('Clear chat history'):
    st.session_state.chat_history = []
    st.session_state.chat.message_history = []

st.write('\n')

