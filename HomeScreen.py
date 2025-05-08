import streamlit as st
import base64
from response_logic import get_bot_response

def show_home_screen(): 

     # Use a Streamlit button for logic
    with st.container():
        back_button_placeholder = st.empty()
    if back_button_placeholder.button("Chat", key="back_chat_button"):
        st.session_state.screen = "chat"
        st.rerun()
    
    # Define image path
    logo_path = "FPU_images/sunbirds.png"
    logo_path1 = "FPU_images/FPU.png"
    logo_path2 = "FPU_images/FresnoPacific.png"
    logo_path3 = "FPU_images/FPU logo.webp"
    logo_path4 = "FPU_images/FPUni.png"

    # Encode image to base64
    with open(logo_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    with open(logo_path1, "rb") as img_file:
        b64_string1 = base64.b64encode(img_file.read()).decode()
    with open(logo_path2, "rb") as img_file:
        b64_string2 = base64.b64encode(img_file.read()).decode()
    with open(logo_path3, "rb") as img_file:
        b64_string3 = base64.b64encode(img_file.read()).decode()
    with open(logo_path4, "rb") as img_file:
        b64_string4 = base64.b64encode(img_file.read()).decode()

    # URLs
    link_url = "https://www.fpusunbirds.com"
    link_url2 = "https://www.fresno.edu/admission"
    link_url3 = "https://www.fresno.edu/undergraduate/programs"
    link_url4 ="https://www.fresno.edu/sites/default/files/documents/campus-safety/campus-map-fresno-main-campus-2025-01-22-no.pdf"

    # Embed in HTML
    st.markdown(
    f"""
    <style>
    .fixed-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background-color: #0b1c5e;
        display: flex;
        justify-content: center; 
        align-items: center;
        padding: 60px 30px 5px 5px;
        gap: 20px;
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
        background: linear-gradient(to bottom, #0b1c5e, rgba(11, 28, 94, 0));
        z-index: 700;
        pointer-events: none;
    }}
    .content-spacer {{
        margin-top: 2px;
    }}
    html, body, .stApp {{
        background-color: #0c2278 !important;
        overflow: hidden !important;
        height: 100vh !important;
    }}
    .block-container {{
        overflow: hidden !important;
        height: 100vh !important;
        padding-top: 200px !important;
        display: flex;
        flex-direction: column;
        justify-content: start;
    }}
    header, footer {{
        background-color: #0b1c5e !important;
    }}
    footer {{
        visibility: hidden;
        height: 0px;
        padding: 0 !important;
        margin: 0 !important;
    }}
    .row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 20px;
        gap: 10px;
    }}
    .clickable-box1, .clickable-box2, .clickable-box3 {{
        background-color: #aebbc2;
        padding: 10px;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 8px #000000;
        text-align: center;
        width: 250px;
        text-decoration: none;
    }}
    .clickable-box1 img, .clickable-box2 img, .clickable-box3 img {{
        height: 100px;
        margin-bottom: 15px;
        border-radius: 8px;
    }}
    .clickable-box1 p, .clickable-box2 p, .clickable-box3 p {{
        font-size: 18px;
        font-weight: bold;
        color: #000000;
        margin: 0.5px 0;
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
        <img src="data:image/png;base64,{b64_string3}" alt="Sunbirds Logo"> 
        <div class="title-block">
            <h1>SUNNY THE SUNBIRD AI</h1>
            <h2>Learn about Fresno Pacific University!</h2>
        </div>
    </div>

    <div class="scroll-gradient"></div>
    <div class="content-spacer"></div>

    <!-- Row 1 -->
    <div class="row">
        <div>
            <a href="{link_url}" class="clickable-box1" target="_blank">
                <img src="data:image/png;base64,{b64_string}" alt="Sunbirds Logo">
                <p>FPU ATHLETICS</p>
                <p>Website Here!</p>
            </a>
        </div>
        <div>
            <a href="{link_url2}" class="clickable-box2" target="_blank">
                <img src="data:image/png;base64,{b64_string1}" alt="Sunbirds Logo">
                <p>APPLY HERE!</p>
            </a>
        </div>
    </div>

    <!-- Row 2 -->
    <div class="row">
        <div>
            <a href="{link_url3}" class="clickable-box3" target="_blank">
                <img src="data:image/png;base64,{b64_string2}" alt="Sunbirds Logo">
                <p>Undergraduate</p>
                <p>Programs Here!</p>
            </a>
        </div>
        <div>
            <a href="{link_url4}" class="clickable-box3" target="_blank">
                <img src="data:image/png;base64,{b64_string4}" alt="Sunbirds Logo">
                <p>FPU Campus</p>
                <p>Map Here!</p>
            </a>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)