import os
import sys
# Add root directory to sys.path so we can import config.py from root folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import HF_TOKEN

def build_chroma_db(pdf_paths, persist_dir="chroma_db"):
    docs = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_dir)
    vectordb.persist()
    print(f"Chroma DB built with {len(texts)} chunks.")


if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_paths = [os.path.join(project_root, "data", "DSA BOOK.pdf")]
    build_chroma_db(pdf_paths)
