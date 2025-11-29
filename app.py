import streamlit as st

st.set_page_config(page_title="Чатбот", page_icon="🤖")

st.title("🤖 Моят Streamlit чатбот")

# Пазим историята на съобщенията
if "messages" not in st.session_state:
    st.session_state.messages = []

# Показване на старите съобщения
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Поле за потребителско съобщение
user_message = st.chat_input("Напиши съобщение...")

if user_message:
    # Добавяме съобщението в историята
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.write(user_message)

    # Отговор от чатбота (тук е твоята логика)
    bot_reply = f"Ти каза: {user_message}"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
