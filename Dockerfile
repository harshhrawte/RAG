FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV VECTOR_DB_PATH=/app/chroma_db

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Copy and install requirements
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy your app code
COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "interface/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
