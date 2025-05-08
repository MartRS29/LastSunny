import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from HomeScreen import show_home_screen
from ChatScreen import show_chat_screen
from ChatTab import show_chat_tab 

# -------------------------------
# 0. Initialize UI state
# -------------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if st.session_state.screen == "chat":
    show_chat_screen()
else:
    show_home_screen()

# Show the chat tab permanently
show_chat_tab()

# -------------------------------
# 1. Load environment and configure Gemini API
# -------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# -------------------------------
# 2. Load FAISS Vector Store
# -------------------------------
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

faiss_index = FAISS.load_local(
    "SunnyTheSunbirdAI/Sunny_The_Sunbird_AI/chroma_db_backup",
    embeddings,
    allow_dangerous_deserialization=True
)

# Now `faiss_index` is your document search tool.
# Example use (optional depending on where you use it):
# docs = faiss_index.similarity_search("your query here", k=3)
# chain = load_qa_chain(ChatGoogleGenerativeAI(model="gemini-pro"), chain_type="stuff")
# response = chain.run(input_documents=docs, question="your query here")













   
