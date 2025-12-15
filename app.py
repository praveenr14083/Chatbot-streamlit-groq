import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def groq_api(messages):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=1024,
    )
    return response.choices[0].message.content


if "history" not in st.session_state:
    st.session_state.history = []


for msg in st.session_state.history:
    st.chat_message(msg["role"]).write(msg["content"])


user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = groq_api(st.session_state.history)

    st.session_state.history.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
