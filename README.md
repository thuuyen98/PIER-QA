
# PIER-QA App

### Configure ElasticSearch

1. Create a deployment at: https://cloud.elastic.co/deployments
2. Click on the deployment, select **Open Kibana** to open the deployment dashboard
3. Create indices: On the left panel, choose **Content** tab under Search section. Create 3 indices: `public_db`, `private_db`, `raptor_db`
4. Create API Keys: On the left panel, choose **Stack management** tab under Management section then select **API Keys** tab under Security section. Select **Create API Keys** button.
   Note: You might need to configure roles for the user associated with the API key in order to access to the database using API keys. Go to the **Users** tab under the same Security section, click on the user and set appropriate privileges for the user, e.g., `superuser`.

### Installation
* With pre-built docker image (recommended)

  ```
    docker run --gpus '"all"' --rm -it anhnv125/rag:latest
    git clone https://github.com/thuuyen98/PIER-QA.git /workspace
    cd /workspace/PIER-QA
  ```
  
* With pip

  ```
    git clone https://github.com/thuuyen98/PIER-QA.git
    cd PIER-QA
    pip install torch==2.3.1 --index_url https://download.pytorch.org/whl/cu118
    CMAKE_ARGS="-DLLAMA_CUDA=on" FORCE_CMAKE=1 pip install -r requirements.txt
    cd marker
    pip uninstall marker-pdf && pip install -e .
  ```
### Deploy an open-source model with llama.cpp (not require if only use OpenAI models)
1. Clone [llama.cpp](https://github.com/ggerganov/llama.cpp) and follow its installation instruction
2. Download a GGUF model. For example, to download our **Llama3-70B-RAG** (Q4_K_M quantized):
    ```
   HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download WendyHoang/Llama3-70B-RAG --local-dir path/to/store/model --include '*Q4_K_M*gguf'
   ```
3. Host the model with llama.cpp.
    ```
   cd llama.cpp
   ./llama-server --model path/to/store/model/ggml-model-Q4_K_M.gguf -ngl 9999 -t 4 -c 8192 -fa -np 1 -cb
   ```
   The recommended VRAM for Q4_K_M 70B model is 48GB. Try decreasing context length (-c param) if it doesn't fit. 

   By default, the OpenAI-compatible server endpoint is http://localhost:8080/v1
### Configure environment variables

  ```
    export ES_URL='elastic_search_url' # can be found in kibana page url, which is in format https://[ES_URL]/app/home#/
    export ES_API_KEY='elastic_search_api_key' # elasticsearch user API key obtained from the above step.
    export OPENAI_API_BASE='custom_llm_endpoint' # endpoint of a custom OpenAI-compatible server endpoint such as llama.cpp or vllm if using open-source models. For example: http://localhost:8080/v1
    export OPENAI_API_KEY='api_key' # OpenAI api key or api key to the custom endpoint if set.
  ```

### Run the app

 ```
 streamlit run streamlit_app.py
 ```

## Purpose
This work is based on https://github.com/0xMatthieu/Simple_RAG_app/
The aim is to provide a simple app implementing a RAG function on specific document. It provides a simple database abstraction layer combined with an simple chat agent to perform RAG
## Structure
```
├── src
│   ├── .streamlit
│   │── Model   
│   │── Preprocessing      
│   │── Database
│   │   ├── Private
│   │   │   ├── preprocessing_output
│   │   │   ├── Files
│   │   │   │   ├──header_footer_remove
│   │   │   │   │   ├──markdown
│   │   ├── Public
│   │   │   ├── preprocessing_output
│   │   │   ├── Files
│   │   │   │   ├──header_footer_remove
│   │   │   │   │   ├──markdown
│   │   ├── Raptor
│   │   │   ├── preprocessing_output
│   │   │   ├── Files
│   │   │   │   ├──header_footer_remove
│   │   │   │   │   ├──markdown
```
## Adding a new document
New document can be added using the following methods
- Adding the document to \Files folder
- Calling the function `add_missing_document_to_database` or using the button *Add missing files to DB* in the streamlit UI
Note: adding new document might take a lot of time due to the preprocessing

## Working with multiple database
Defaut option is using only data from public database
Data from private database and RAPTOR database can be also used

## working with retrieval agent or tool agent
The POC offers the possibility to use both a retrieval agent or a tool agent. 
It is possible to switch using the Use agent checkbox in App LLM parameteres expander
Differences are the following:
- retrieval agent can only perform RAG on given document. It returns good quality answer.
- tool agent is able to determine and use different tools and provide a custom answer. It can currently use the retrieval agent / a tool to do math / its own knowledge database. Answer quality seems to be a little bit lower on retrieval (way of improvement)
