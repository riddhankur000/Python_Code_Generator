import streamlit as st
from dotenv import load_dotenv
import os
import json

load_dotenv()       #loading all the environment variables

url = "Gradio_Deployment_url"

def build_llama2_prompt(messages):
  start_prompt = '<s>[INST] '
  end_prompt = ' [/INST]'
  conversation=[]
  for index,message in enumerate(messages):
    if message["role"]=="system" and index==0:
      conversation.append(f"<<SYS>>\n{message['content']}\n<</SYS>>\n")
    elif message["role"]=="user":
      conversation.append(f"{message['content']}")
    else:
      conversation.append(f"{message['content']}</s>")
  prompt=start_prompt+"".join(conversation)+end_prompt
  return prompt

    

#Initialize Our Streamlit App

st.set_page_config(page_title="Image info Generation")

st.header("PYTHON CODE GENERATOR")
input_text = st.text_input("Which Python Code you want to Generate")
instruction = st.text_input("Enter Input for your Code to get Output")


submit = st.button("TGenerate")

if submit:
    messages=[{"role":"system","content":input_text}]
    messages.append({"role":"user","content":instruction})
    input=build_llama2_prompt(messages)
    input_data = {"query": input}

    input_data_json= json.dumps(input_data)
    print(input_data_json)
    # result = client.predict(input_data_json, api_name="/predict")

    # st.write(result["output"])
