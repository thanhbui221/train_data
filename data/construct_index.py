from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os
MODEL_NAME = "text-davinci-003"
def construct_index(src_path, out_path, MODEL_NAME):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 512

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name=MODEL_NAME, max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader(src_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk(f"{out_path}/index_{MODEL_NAME}.json")

    return index

if __name__ == "__main__":
    import os 
    src_path = os.getcwd() 
    dir_path = src_path + "/clean"
    out_path = src_path
    os.environ["OPENAI_API_KEY"] = input("Input key")
    index = construct_index(src_path, out_path, MODEL_NAME)