#!/bin/bash
echo "Building Chroma DB..."
python app/build_chroma.py
echo "Starting Streamlit app..."
streamlit run frontend/streamlit_app.py
