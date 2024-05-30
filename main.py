import  os
from constant import openai_key
from langchain.llms.openai import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

st.title('LangChain Demo')
input_text=st.text_input("Search any topic")

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))