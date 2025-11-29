import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI ChatBot", page_icon="🤖")

st.title("🤖 AI ChatBot (GPT-4o-mini)")

# -----------------------------
# Локално: постави своя OpenAI API ключ тук
# Може да го смениш с st.secrets["OPENAI_API_KEY"] за Cloud
API_KEY = "ТВОЯ_API_KEY"  # <- сложи своя ключ
client = OpenAI(api_key=API_KEY)
# -----------------------------

# История на съобщенията
if "messages" not in st.session_state:
    st.session_state.messages = []

# Показваме историята
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Въвеждане на ново съобщение
user_text = st.chat_input("Напиши нещо...")

if user_text:
    # Добавяме потребителския текст
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    # Генерираме AI отговор
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    # Добавяме AI отговора
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
