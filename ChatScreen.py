import streamlit as st
from ChatHelpers import init_chat_session, handle_user_input, display_chat_messages
import base64

def show_chat_screen():

    # Use a Streamlit button for logic
    with st.container():
        back_button_placeholder = st.empty()
    if back_button_placeholder.button("Back", key="back_home_button"):
        st.session_state.screen = "home"
        st.rerun()

    # Define image path
    logo_path = "FPU_images/FPU logo.webp"

    # Encode image to base64
    with open(logo_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()

    # Wrapper around the fixed-header that acts as a button
    st.markdown(f"""
        <style>
        html, body, .stApp {{
            background-color: #e67625 !important;
            margin-top: 95px !important;
            padding: 2.5px !important;
            overflow-x: hidden;
            base="dark"
            primaryColor="#e67625"
            backgroundColor="#e67625"
        }}
        header, footer {{
            background-color: #de7112 !important;
        }}
        .fixed-header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background-color: #de7112;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 60px 5px 5px 5px;
            gap: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }}
        .fixed-header img {{
            height: 100px;
            margin-right: 20px;
        }}
        .fixed-header .title-block h1,
        .fixed-header .title-block h2 {{
            color: white;
            font-size: 25px;
            margin: 0;
            padding: 0;
            line-height: 1.2;
        }}
        .fixed-header .title-block {{
            font-size: 25px;
            margin: 0;
            padding: 0;
            line-height: 0.5;
        }}
        .scroll-gradient {{
            position: fixed;
            top: 150px;
            left: 0;
            width: 100%;
            height: 120px;
            background: linear-gradient(to bottom, #de7112, rgba(222, 113, 18, 0));
            z-index: 700;
            pointer-events: none;
        }}
        .back-button {{
            background-color: white;
            color: #c48443;
            border: 2px solid #c48443;
            padding: 5px 5px;
            font-weight: bold;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }}
        .back-button:hover {{
            background-color: #c48443;
            color: white;
        }}
        </style>

        <div class="fixed-header">
            <img src="data:image/png;base64,{b64_string}" alt="Logo"> 
            <div class="title-block">
                <h1>SUNNY THE SUNBIRD AI</h1>
                <h2>Learn about Fresno Pacific University!</h2>
            </div>
        </div>

        <div class="scroll-gradient"></div>

        """, 
        unsafe_allow_html=True
    )
    
    # Display chat content
    with st.container():
        st.markdown('<div class="chat-screen">', unsafe_allow_html=True)

        init_chat_session()

        # Display chat messages after handling input
        display_chat_messages()

        st.markdown('</div>', unsafe_allow_html=True)

    
