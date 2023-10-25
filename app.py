import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper



#os.environ['OPENAI_API_KEY']=apikey   
apikey = os.environ.get("OPENAI_API_KEY")
st.title("Kaçak Zeka'ya Hoş Geldiniz!")
st.caption('bu proje :blue[mustafa taner]  tarafından yazılmıştır   :sunglasses:')
st.balloons()
prompt=st.text_input('Bana istediğin soruyu sorabilirsin :) ')
if st.button('Sor'):
    if prompt:
        llm = OpenAI(temperature=0.2, model_name='gpt-3.5-turbo')
        response = llm(prompt)
        st.write(response)
    else:
        st.write("Lütfen bir soru girin.")
