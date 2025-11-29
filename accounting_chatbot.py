# accounting_chatbot.py — Джи Енд Ви Акаунтинг помощник
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# ——— НАСТРОЙКИ ———
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.3,
    groq_api_key=st.secrets["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"]  # ← ще работи автоматично в Streamlit Cloud
)

template = """
Ти си Джи Енд Ви Акаунтинг — професионален счетоводител и ТРЗ специалист с над 15 години опит в България.
Отговаряй винаги на български език, любезно, кратко и изключително точно.
Използвай актуалните данни за 2025–2026 г.
Ако не си 100 % сигурен — кажи: "Ще проверя с колега и ще ви върна отговор до 1 работен ден."

Въпрос: {question}

Отговор (на български, максимум 3–4 изречения):
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm | st.write

# ——— ДИЗАЙН ———
st.set_page_config(page_title="Джи Енд Ви Акаунтинг – помощник", page_icon="")

# Заглавие с твоето лого/име
st.markdown(
    """
    <div style="text-align: center; padding: 30px; background: linear-gradient(90deg, #1E3A8A, #1E88E5); color: white; border-radius: 15px; margin-bottom: 30px;">
        <h1>Джи Енд Ви Акаунтинг</h1>
        <p style="font-size: 20px; margin: 10px 0;">Счетоводен и ТРЗ помощник</p>
        <p style="font-size: 16px; opacity: 0.9;">Попитайте ме за ДДС • Заплати • Осигуровки • НАП • Трудови договори</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Първо съобщение от помощника
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Здравейте! Аз съм помощникът на Джи Енд Ви Акаунтинг. С какво мога да ви помогна днес?"}
    ]

# История на чата
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Въпрос от потребителя
if question := st.chat_input("Напишете въпроса си тук..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Мисля..."):
            response = chain.invoke({"question": question})
        st.write(response.content)

    st.session_state.messages.append({"role": "assistant", "content": response.content})

# Долен текст
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; color: #666; font-size: 14px;">
        © 2025 Джи Енд Ви Акаунтинг • гр. София • всички права запазени
    </div>
    """,
    unsafe_allow_html=True,
)
