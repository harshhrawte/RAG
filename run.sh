#!/bin/bash
echo "Building Chroma DB..."
python app/chroma_data_pipeline.py
echo "Starting Streamlit app..."
streamlit run interface/streamlit.py
