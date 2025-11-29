import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="Джи Енд Ви Акаунтинг – помощник", page_icon="")

# Взима ключа от secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.markdown("""
<div style="text-align:center;padding:30px;background:linear-gradient(90deg,#1E3A8A,#1E88E5);color:white;border-radius:15px;">
    <h1>Джи Енд Ви Акаунтинг</h1>
    <p style="font-size:20px;">Счетоводен и ТРЗ помощник</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Здравейте! Аз съм помощникът на Джи Енд Ви Акаунтинг. С какво мога да ви помогна днес?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if question := st.chat_input("Напишете въпроса си тук..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    with st.chat_message("assistant"):
        with st.spinner("Мисля..."):
            chat_complete = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                temperature=0.3,
                max_tokens=200
            )
            response = chat_complete.choices[0].message.content
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
