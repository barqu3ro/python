from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext
from langchain import OpenAI
import gradio as gr
import os

os.environ["OPENAI_API_KEY"] = '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'

def construct_index(directory_path):
    num_outputs = 512

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    docs = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

index = construct_index("docs")
iface.launch(share=True)


# from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
# from langchain import OpenAI6
# import gradio as gr
# import sys
# import os

# os.environ["OPENAI_API_KEY"] = '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'

# def construct_index(directory_path):
#     max_input_size = 4096
#     num_outputs = 512
#     max_chunk_overlap = 20
#     chunk_size_limit = 600

#     prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

#     documents = SimpleDirectoryReader(directory_path).load_data()

#     index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

#     index.save_to_disk('index.json')

#     return index

# def chatbot(input_text):
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     response = index.query(input_text, response_mode="compact")
#     return response.response

# iface = gr.Interface(fn=chatbot,
#                      inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
#                      outputs="text",
#                      title="My AI Chatbot")

# index = construct_index("docs")
# iface.launch(share=True)