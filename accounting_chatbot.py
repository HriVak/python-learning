# accounting_chatbot.py — Джи Енд Ви Акаунтинг помощник
import streamlit as st
from openai import OpenAI

# Взима ключа от Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Джи Енд Ви Акаунтинг", page_icon="")

st.markdown("""
<div style="text-align:center;padding:30px;background:linear-gradient(90deg,#1E3A8A,#1E88E5);color:white;border-radius:15px;">
    <h1>Джи Енд Ви Акаунтинг</h1>
    <p style="font-size:20px;">Счетоводен и ТРЗ помощник</p>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Здравейте! Аз съм помощникът на Джи Енд Ви Акаунтинг. С какво мога да ви помогна днес?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if question := st.chat_input("Напишете въпроса си тук..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    with st.chat_message("assistant"):
        with st.spinner("Мисля..."):
            chat = client.chat.completions.create(
                model="gpt-4o-mini",  # Евтин и бърз модел, перфектен за български
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                temperature=0.3,
                max_tokens=250
            )
            response = chat.choices[0].message.content
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
