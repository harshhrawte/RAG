# chatbot.py
# Backend logic for AlgoAssist - handles LLM, embeddings, and prompt creation

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from chromadb import PersistentClient
from config import GROQ_API_KEY, HF_TOKEN  # API keys for Groq and Hugging Face
import streamlit as st

# Cache the LLM instance so it doesn't reload every time the app runs
@st.cache_resource
def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="Llama3-8b-8192",  # Using Groq's LLaMA3 model
        temperature=0.5,              # Balanced creativity
        max_tokens=1024,              # Max length of response
        max_retries=3,                # Retry if API fails
        request_timeout=30            # Timeout in seconds
    )

# This sets up the vector DB retriever using Chroma and HuggingFace embeddings
def get_retriever(persist_dir="chroma_db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Connect to Chroma's persistent storage
    client = PersistentClient(path=persist_dir)
    collection = client.get_collection(name="langchain")

    # Return both collection and embeddings so they can be used together
    return collection, embeddings

# This builds the prompt template that guides the assistant's behavior
def create_prompt():
    return ChatPromptTemplate.from_template(
        """You are a helpful assistant specialized in Data Structures and Algorithms.
Use the following context to answer the question.
If the context is not relevant, provide an accurate answer based on your knowledge.

Context:
{context}

Question: {query}
Answer:"""
    )
