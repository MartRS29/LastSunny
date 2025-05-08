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
from ChatScreen import show_chat_screen
from ChatTab import show_chat_tab 
import google.generativeai as genai
import chromadb

# Initialize screen state if not already set
if "screen" not in st.session_state:
    st.session_state.screen = "home"  # Start at home screen

# Handle screen transitions based on the screen state
if st.session_state.screen == "chat":
    show_chat_screen()  # Show chat screen
else:
    show_home_screen()  # Show home screen
    
# Show the chat tab permanently at the bottom
show_chat_tab()

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# -------------------------------
# 1. Configure Gemini API Key
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# -------------------------------
# 2. Connect to ChromaDB
# -------------------------------
client = chromadb.PersistentClient(path="chroma_db_backup")
collection = client.get_collection(name="fpu_website_embedding")
