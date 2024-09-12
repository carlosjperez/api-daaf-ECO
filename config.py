import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SWAGGER = {
        'title': 'Simple Flask API',
        'uiversion': 3,
        'openapi': '3.0.2'
    }
