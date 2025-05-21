# streamlit.py
# Streamlit UI for AlgoAssist - An Intelligent DSA Learning Companion

import sys
import os
import streamlit as st

# Make sure we can import from the 'app' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.chatbot import answer_query  # This handles the logic of answering user queries

# Basic setup for the page appearance
st.set_page_config(
    page_title="AlgoAssist",    # What shows on the browser tab
    page_icon="🤖",             # A fun little robot icon
    layout="centered"           # Keep everything centered for better UX
)

# A bit of custom CSS to make the page look nice
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #4CAF50;
    }
    .subheader {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Main title and subtitle right at the top
st.markdown("<h1 class='main-header'>AlgoAssist 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Your intelligent DSA learning companion</p>", unsafe_allow_html=True)

# If it's the user's first time here, we start a fresh chat
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Loop through and show previous messages (both user and assistant)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# On the left: a list of clickable sample questions to get started quickly
with st.sidebar:
    st.header("Sample Questions")
    sample_questions = [
        "What is the time complexity of quicksort?",
        "Explain binary search trees",
        "How does a hash table work?",
        "Difference between BFS and DFS",
        "Explain dynamic programming"
    ]

    # If user clicks one, we simulate sending it as their question
    for question in sample_questions:
        if st.button(question):
            st.session_state.messages.append({"role": "user", "content": question})
            with st.spinner("Thinking..."):
                answer = answer_query(question)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()  # Refresh to update the chat interface with new messages

# Main input box where the user types their custom query
query = st.chat_input("Ask about Data Structures & Algorithms")

if query:
    # Store the user’s question in chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Show the question in the chat bubble
    with st.chat_message("user"):
        st.write(query)

    # Generate the answer and show it
    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            answer = answer_query(query)
            st.write(answer)

    # Save the assistant's reply to chat history too
    st.session_state.messages.append({"role": "assistant", "content": answer})
