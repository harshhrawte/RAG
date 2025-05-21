# app/__init__.py

import sys
import sqlite3
sys.modules["sqlite3"] = sqlite3

from config import GROQ_API_KEY, HF_TOKEN
from .chroma_data_pipeline import build_chroma_db
from .chatbot import answer_query
