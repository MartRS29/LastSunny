import streamlit as st
from response_logic import get_bot_response

def show_chat_tab():
    # Remove redundant input at the top
    with st.container():
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Chat input (only at the bottom now)
        user_input = st.chat_input("Ask Sunny a question about FPU...")
        
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            response = get_bot_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.screen = "chat"  # 🚨 trigger screen switch!
            st.rerun()
