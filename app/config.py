import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
APP_ENV = os.getenv("APP_ENV", "dev")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:8000")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "journal_ai_db")
