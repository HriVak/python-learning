import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

# --- ПОСТАВИ API KEY в secrets.toml (в Streamlit Cloud) ---
# client = OpenAI(api_key="YOUR_API_KEY")  # локално
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 AI ChatBot (GPT-4o-mini)")

# Съхраняваме историята
if "messages" not in st.session_state:
    st.session_state.messages = []

# Показване на старите съобщения
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Въвеждане
user_text = st.chat_input("Напиши нещо...")

if user_text:
    # Добавяме потребителя
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )
    with st.chat_message("user"):
        st.write(user_text)

    # Генерираме AI отговор
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.write(bot_reply)
