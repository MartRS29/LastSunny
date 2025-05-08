import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
from HomeScreen import show_home_screen
from ChatTab import show_chat_tab 
import chromadb

# -------------------------------
# 0. Load API Key
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -------------------------------
# 1. Initialize Gemini model
# -------------------------------
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# -------------------------------
# 2. Connect to ChromaDB
# -------------------------------
client = chromadb.PersistentClient(path="chroma_db_backup")
collection = client.get_collection(name="fpu_website_embeddings")

# -------------------------------
# 3. Initialize screen and chat state
# -------------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "home"  # Start at home screen

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # For storing messages

# -------------------------------
# 4. Chat screen logic
# -------------------------------
def show_chat_screen():
    st.title("Chat with Gemini")

    # Display chat history
    for msg in st.session_state.chat_history:
        role = "🧑‍💻" if msg["role"] == "user" else "🤖"
        st.markdown(f"{role} **{msg['role'].capitalize()}:** {msg['content']}")

    user_input = st.text_input("Ask something:", key="chat_input")

    if user_input:
        # Add user's message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Send entire chat history to the model
        response = model.generate_content(st.session_state.chat_history)

        # Add model response to chat history
        st.session_state.chat_history.append({"role": "model", "content": response.text})

        # Rerun to display updated history
        st.experimental_rerun()

# -------------------------------
# 5. Main screen navigation
# -------------------------------
if st.session_state.screen == "chat":
    show_chat_screen()  # Show chat screen
else:
    show_home_screen()  # Show home screen

# Always show chat tab
show_chat_tab()
