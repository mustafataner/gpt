import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper


apikey = os.environ.get("OPENAI_API_KEY")


st.title("Kaçak Zeka'ya Hoş Geldiniz!")
st.caption('bu proje :blue[mustafa taner]  tarafından yazılmıştır   :sunglasses:')
st.balloons()
prompt = st.text_input('Bana istediğin soruyu sorabilirsin :) ')

# LLM nesnesini başlat
llm = OpenAI(temperature=0.92, model_name='gpt-3.5-turbo')

if st.button('Sor'):
    if prompt:
        # Mesaj formatını doğru bir şekilde ayarla
        response = llm([{"role": "user", "content": prompt}])
        st.write(response['choices'][0]['message']['content'])
    else:
        st.write("Lütfen bir soru girin.")



