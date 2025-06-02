FROM python:3.10.16

ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV VECTOR_DB_PATH=/app/chroma_db

WORKDIR /app

# --- Install system dependencies ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# --- Upgrade pip and clear cache ---
RUN pip install --upgrade pip && pip cache purge

# --- Copy requirements file and install all dependencies (including torch) ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy your application code ---
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "interface/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
