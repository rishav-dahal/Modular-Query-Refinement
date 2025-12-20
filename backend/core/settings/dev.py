from .base import *
from dotenv import load_dotenv
import os
import json

load_dotenv(ROOT_DIR / ".env.dev")

print("Loading development settings...")

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env.dev")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}

# CORS settings for development
CORS_ALLOWED_ORIGINS = json.loads(os.environ.get("CORS_ALLOWED_ORIGINS", "[\"http://localhost:3000\", \"http://localhost:3001\", \"http://localhost:3002\", \"http://127.0.0.1:3000\"]"))
CORS_ALLOW_CREDENTIALS = os.environ.get("CORS_ALLOW_CREDENTIALS", "True") == "True"
CORS_ALLOW_ALL_ORIGINS = os.environ.get("CORS_ALLOW_ALL_ORIGINS", "False") == "True"
CORS_ALLOW_HEADERS = json.loads(os.environ.get("CORS_ALLOW_HEADERS", "[\"accept\", \"accept-encoding\", \"authorization\", \"content-type\", \"dnt\", \"origin\", \"user-agent\", \"x-csrftoken\", \"x-requested-with\"]"))
CORS_ALLOW_METHODS = json.loads(os.environ.get("CORS_ALLOW_METHODS", "[\"DELETE\", \"GET\", \"OPTIONS\", \"PATCH\", \"POST\", \"PUT\"]"))