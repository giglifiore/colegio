import os
import dj_database_url
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='changeme')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Puedes agregar tus apps aquí
]

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
