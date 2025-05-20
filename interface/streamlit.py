import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.chatbot import answer_query

# Page configuration
st.set_page_config(
    page_title="AlgoAssist",
    page_icon="🤖",
    layout="centered"
)

# Simple CSS
st.markdown("""
<style>
    .main-header {text-align: center; color: #4CAF50;}
    .subheader {text-align: center; font-size: 1.2em; margin-bottom: 20px;}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown("<h1 class='main-header'>AlgoAssist 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Your intelligent DSA learning companion</p>", unsafe_allow_html=True)

# Initialize chat history if not exists
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Sidebar with sample questions
with st.sidebar:
    st.header("Sample Questions")
    sample_questions = [
        "What is the time complexity of quicksort?",
        "Explain binary search trees",
        "How does a hash table work?",
        "Difference between BFS and DFS",
        "Explain dynamic programming"
    ]
    
    for question in sample_questions:
        if st.button(question):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": question})
            
            # Generate answer
            with st.spinner("Thinking..."):
                answer = answer_query(question)
            
            # Add assistant response to chat
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()

# Chat input
query = st.chat_input("Ask about Data Structures & Algorithms")
if query:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": query})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.write(query)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            answer = answer_query(query)
            st.write(answer)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})