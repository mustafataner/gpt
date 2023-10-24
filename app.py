import os
import streamlit as st
from langchain.chat_models import ChatOpenAI

# API anahtarını al
apikey = os.environ.get("OPENAI_API_KEY")

st.title("Kaçak Zeka'ya Hoş Geldiniz!")
st.caption('bu proje :blue[mustafa taner]  tarafından yazılmıştır   :sunglasses:')
st.balloons()
prompt = st.text_input('Bana istediğin soruyu sorabilirsin :) ')

# LLM nesnesini başlat
llm = ChatOpenAI(temperature=0.92, model_name='gpt-3.5-turbo')

# Sohbet geçmişini (conversation history) tutan bir liste oluştur
conversation_history = []

if st.button('Sor'):
    if prompt:
        # Yeni mesajı sohbet geçmişine ekle
        conversation_history.append({"role": "user", "content": prompt})
        
        # Modeli bu sohbet geçmişiyle çağır
        response = llm(conversation_history)
        
        # Modelin verdiği yanıtı sohbet geçmişine ve ekrana ekle
        answer = response['choices'][0]['message']['content']
        conversation_history.append({"role": "assistant", "content": answer})
        
        st.write(answer)
    else:
        st.write("Lütfen bir soru girin.")
