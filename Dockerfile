FROM python:3.10-slim

WORKDIR /app

# Use a more reliable Debian mirror and retry installation with fix-missing
RUN apt-get update && \
    apt-get install -y --fix-missing build-essential libffi-dev && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false

CMD ["streamlit", "run", "app/chatbot.py"]
