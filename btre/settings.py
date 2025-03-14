import os
from pathlib import Path
import dj_database_url  # type: ignore
from dotenv import load_dotenv  # type: ignore
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Load environment variables
load_dotenv()

# Fix BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent  # Uses Path() correctly

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG based on environment variable
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Defaults to False if not set

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    # External apps
    'pages.apps.PagesConfig',
    'whitenoise.runserver_nostatic',  # ✅ Whitenoise for static files
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
      'cloudinary',
    'cloudinary_storage',
     'ckeditor',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',  # ✅ Added for {% static %}
            ],
        },
    },
]

WSGI_APPLICATION = 'btre.wsgi.application'

# Database
DATABASES ={
    'default':dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Static files (CSS, JavaScript, Images)
# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WhiteNoise static files storage
if not DEBUG:  # ✅ Only use WhiteNoise in production
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

    
    
# WHITENOISE_MANIFEST_STRICT = False
   

# Media files

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Cloudinary Configuration from Environment Variables
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    
}

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)




#Upload path for ckeditor

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 700,
        'extraPlugins': 'uploadimage',  # Allow image upload
    }
}

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Import local settings if available
try:
    from .local_settings import *
except ImportError:
    print("No local settings found. Looks like you are in production.")
