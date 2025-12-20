from .base import *
import os
from dotenv import load_dotenv
import json

# Load prod environment variables from .env.prod
load_dotenv(ROOT_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env.prod")

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
if ALLOWED_HOSTS == [""]:
    raise ValueError("ALLOWED_HOSTS must be set in .env.prod")

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# CORS settings for production
CORS_ALLOWED_ORIGINS = json.loads(os.environ.get("CORS_ALLOWED_ORIGINS", "[\"http://localhost:3000\", \"http://localhost:3001\", \"http://localhost:3002\", \"http://127.0.0.1:3000\"]"))
CORS_ALLOW_CREDENTIALS = os.environ.get("CORS_ALLOW_CREDENTIALS", "True") == "True"
CORS_ALLOW_ALL_ORIGINS = os.environ.get("CORS_ALLOW_ALL_ORIGINS", "False") == "True"
CORS_ALLOW_HEADERS = json.loads(os.environ.get("CORS_ALLOW_HEADERS", "[\"accept\", \"accept-encoding\", \"authorization\", \"content-type\", \"dnt\", \"origin\", \"user-agent\", \"x-csrftoken\", \"x-requested-with\"]"))
CORS_ALLOW_METHODS = json.loads(os.environ.get("CORS_ALLOW_METHODS", "[\"DELETE\", \"GET\", \"OPTIONS\", \"PATCH\", \"POST\", \"PUT\"]"))