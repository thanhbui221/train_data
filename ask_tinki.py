from llama_index import GPTSimpleVectorIndex
import os

def ask_tinki():
    src_path = os.getcwd() + "/data/index.json"
    index = GPTSimpleVectorIndex.load_from_disk(src_path)
    query = input("What do you want to ask Tinki?")
    response = index.query(query, response_mode="compact")
    print(f"Tinki says: {response.response}")
    

if __name__ == "__main__":
    print("Welcome!!!")
    os.environ["OPENAI_API_KEY"] = input("OPEN_API_KEY")
    while True:
        ask_tinki()
        