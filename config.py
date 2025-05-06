from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    API_ID = os.getenv('API_ID', 'your_api_id')
    API_HASH = os.getenv('API_HASH', 'your_api_hash')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///messages.db')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'