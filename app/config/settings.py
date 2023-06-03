# SETTINGS FOR LOCAL DEVELOPMENT

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#)!0wd@d&0ev8bmcpg!^0jbj%5*qyc^8r7)n-7!+eei&*%-cqo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
# to_remove    'django.contrib.admin',
# to_remove   'django.contrib.auth',
# to_remove   'django.contrib.contenttypes',
# to_remove   'django.contrib.sessions',
# to_remove   'django.contrib.messages',
    'django.contrib.staticfiles',
    'data.apps.DataConfig',
    'PlantsPage.apps.PlantsPageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
# to_remove    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
# to_remove    'django.middleware.csrf.CsrfViewMiddleware',
# to_remove    'django.contrib.auth.middleware.AuthenticationMiddleware',
# to_remove    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
# to_remove               'django.contrib.auth.context_processors.auth',
# to_remove               'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_plantdb',
        'USER': 'djangobot',
        'PASSWORD': 'djangopassword',
        'HOST': 'postgres'
    }
}


# to_remove Password validation
# to_remove https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# to_remove AUTH_PASSWORD_VALIDATORS = [
# to_remove   {
# to_remove        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# to_remove    },
# to_remove    {
# to_remove        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# to_remove   },
# to_remove   {
# to_remove       'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# to_remove   },
# to_remove   {
# to_remove       'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# to_remove   },
# to_remove ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'