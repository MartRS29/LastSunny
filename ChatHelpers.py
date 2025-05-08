import streamlit as st
from response_logic import get_bot_response

def init_chat_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def handle_user_input(input_key="user_input"):
    user_input = st.session_state.get(input_key)
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = get_bot_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        if input_key in st.session_state:
            del st.session_state[input_key]
        return True
    return False

def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
