import streamlit as st
from streamlit_chat import message
import requests
import openai

openai.api_key = "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"

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def chat(user_text):
    messages = st.session_state['messages']
    user_turn = {"role": "user", "content": user_text}
    messages.append(user_turn)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    messages.append(assistant_turn)

st.title("초간단 챗봇 서비스")

row1 = st.container()
row2 = st.container()

with row2:
    input_text = st.text_input("Me", value="", placeholder='질문을 입력해 주세요')
    if input_text:
        chat(input_text)

with row1:
    for i, msg_obj in enumerate(st.session_state['messages']):
        msg = msg_obj['content']
        is_user = msg_obj['role'] == "user"
        message(msg, is_user=is_user, key=f"chat_{i}")
