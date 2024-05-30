import  os
from constant import openai_key
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

st.title('LangChain Demo')
input_text=st.text_input("Search any topic")

#PROMPT TEMPLATES
first_prompt=PromptTemplate(
    input_variables=['topic'],
    template="tell me about{topic}"
) 

#MEMORY

topic_memory=ConversationBufferMemory(input_key='topic',memory_key='description_history')   
llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_prompt,verbose=True,memory=topic_memory)

if input_text:
    st.write(chain.run(input_text))

    with st.expander('topic'): 
        st.info(topic_memory.buffer)