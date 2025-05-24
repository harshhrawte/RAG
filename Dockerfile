FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV VECTOR_DB_PATH=/app/chroma_db

WORKDIR /app

# Install system dependencies first
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# ✅ Install CPU-compatible PyTorch manually
RUN pip install torch==2.1.0+cpu torchvision==0.16.0+cpu torchaudio==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "interface/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
