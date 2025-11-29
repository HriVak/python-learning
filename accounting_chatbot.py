accounting_chatbot.py — Джи Енд Ви Акаунтинг помощник
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Взима ключа от secrets (скрит и безопасен)
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.3,
    groq_api_key=st.secrets["GROQ_API_KEY"]
)

template = """
Ти си Джи Енд Ви Акаунтинг — професионален счетоводител и ТРЗ специалист в България.
Отговаряй само на български, кратко, точно и любезно.
Използвай данни за 2025–2026 г.

Въпрос: {question}

Отговор:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

st.set_page_config(page_title="Джи Енд Ви Акаунтинг – помощник", page_icon="")

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
            response = chain.invoke({"question": question})
        st.write(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})
