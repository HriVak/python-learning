import streamlit as st
from datetime import datetime
from openai import OpenAI

# --------------------------
# ПОСТАВИ ТВОЯ API KEY ТУК:
# client = OpenAI(api_key="YOUR_KEY_HERE")
# --------------------------

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# --- Custom CSS (балончета) ---
st.markdown("""
<style>
.user-bubble {
    background-color: #DCF8C6;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 8px 0;
    width: fit-content;
    float: right;
    max-width: 80%;
    clear: both;
}

.bot-bubble {
    background-color: #F1F0F0;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 8px 0;
    width: fit-content;
    float: left;
    max-width: 80%;
    clear: both;
}

.timestamp {
    font-size: 10px;
    color: #888;
    clear: both;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Реален AI Чатбот (GPT-4o-mini)")

# История на чатове
if "messages" not in st.session_state:
    st.session_state.messages = []

# Показване на старите
for msg in st.session_state.messages:
    bubble = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(
        f"<div class='{bubble}'>{msg['content']}</div>"
        f"<div class='timestamp'>{msg['time']}</div>",
        unsafe_allow_html=True,
    )

# Въвеждане
user_text = st.chat_input("Напиши нещо...")

if user_text:
    now = datetime.now().strftime("%H:%M")

    # Добавяме потребителя
    st.session_state.messages.append({
        "role": "user",
        "content": user_text,
        "time": now
    })

    # ----- AI ОТГОВОР -----
    response = client.chat.completions.create(
        model="gpt-4o-mini",       # реален GPT модел
        messages=[{"role": "user", "content": user_text}]
    )

    bot_reply = response.choices[0].message.content
    # ----------------------

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply,
        "time": now
    })

    st.experimental_rerun()
