from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from chromadb import PersistentClient
from config import GROQ_API_KEY, HF_TOKEN  # Import both keys
import streamlit as st

@st.cache_resource  #
def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="Llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        max_retries=3,
        request_timeout=30
    )


def get_retriever(persist_dir="chroma_db"):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    client = PersistentClient(path=persist_dir)
    collection = client.get_collection(name="langchain")
    return collection, embeddings

def create_prompt():
    return ChatPromptTemplate.from_template(
        """You are a highly knowledgeable and helpful assistant specialized in Data Structures and Algorithms.
Use the following context to answer the question.
If the context is not relevant, provide an accurate answer based on your knowledge.

Context:
{context}

Question: {query}
Answer:"""
    )