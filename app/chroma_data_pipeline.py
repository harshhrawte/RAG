# build_chroma.py
# Script to build Chroma vector database from a DSA PDF using HuggingFace embeddings

import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import HF_TOKEN  # Hugging Face token (in case it's needed)

# Add the root directory to sys.path to import config.py and access project files easily
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def build_chroma_db(pdf_paths, persist_dir="chroma_db"):
    """
    Loads PDFs, splits the text, and builds a Chroma vector store
    using HuggingFace sentence embeddings.
    """
    docs = []

    # Load documents from all provided PDF paths
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    # Split documents into manageable chunks for embedding
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = splitter.split_documents(docs)

    # Use HuggingFace transformer model to generate embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create and persist the Chroma vector database
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    vectordb.persist()

    print(f"✅ Chroma DB built successfully with {len(texts)} document chunks.")


# Run this script directly to build the DB
if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # You can add multiple PDFs in this list if needed
    pdf_paths = [os.path.join(project_root, "data", "DSA BOOK.pdf")]

    build_chroma_db(pdf_paths)
