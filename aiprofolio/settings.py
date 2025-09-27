"""
Django settings for aiprofolio project.
"""

# aiprofolio/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # <-- New Import for Heroku Database

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# 1. SECURE CONFIGURATION (READING FROM .ENV)
# --------------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
# Reads the key from your .env file
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# Reads DEBUG=True from .env for local development
DEBUG = os.getenv("DEBUG", "False") == "True"

# Reads ALLOWED_HOSTS from .env for local development
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(',')


# Application definition

INSTALLED_APPS = [
    # Custom Apps will be added here in Phase 2
    # 'portfolio',
    # 'microsvc',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# --------------------------------------------------------------------------
# 2. MIDDLEWARE (ADDING WHITENOISE FOR STATIC FILES)
# --------------------------------------------------------------------------

MIDDLEWARE = [
    # WhiteNoise must be listed directly after SecurityMiddleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- New Middleware for Static Files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aiprofolio.urls'

# --------------------------------------------------------------------------
# 3. TEMPLATES (Adding Global Templates Directory)
# --------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS must be set to BASE_DIR / "templates" for a global template search
        'DIRS': [BASE_DIR / "templates"], # <-- Modified!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aiprofolio.wsgi.application'


# --------------------------------------------------------------------------
# 4. DATABASE (CONFIGURED FOR LOCAL SQLite & PRODUCTION PostgreSQL)
# --------------------------------------------------------------------------

# Check if a DATABASE_URL environment variable is set (used by Heroku)
if os.getenv("DATABASE_URL"):
    # Use dj-database-url to parse the Heroku Postgres URL
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    # Use SQLite for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# ... (standard settings unchanged) ...

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# ... (standard settings unchanged) ...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --------------------------------------------------------------------------
# 5. STATIC FILES (REQUIRED FOR WHITE NOISE)
# --------------------------------------------------------------------------

# The URL to use when referring to static files (CSS, JS, images)
STATIC_URL = '/static/'

# The directory where Django will collect all static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra directories to look for static files (e.g., global assets)
STATICFILES_DIRS = [
    BASE_DIR / "static", # <-- We will put global CSS/JS here
]

# Tell WhiteNoise to compress static files (best practice for speed)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'