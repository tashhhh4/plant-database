# SETTINGS FOR PRODUCTION SITE

import os
from pathlib import Path

# Web Server Gateway Interface
WSGI_APPLICATION = 'config.wsgi.application'

# Secret
SECRET_KEY = os.environ['SECRET_KEY']

# Pathing
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
BASE_DIR = '/'
ROOT_URLCONF = 'config.urls'

# Debug
DEBUG = False

# Apps
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'data.apps.DataConfig',
    'PlantsPage.apps.PlantsPageConfig',
    'BrokenPage.apps.BrokenPageConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# Static files (CSS, JS, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DBNAME'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'],
        'HOST': os.environ['DBHOST']
    }
}

#Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True