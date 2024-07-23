"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.conf import settings
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--&uh0uu53v75ivw!j_qr@-zijn)b=xxm6_w-^awpun_^rd!c^_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['localhost', "biznes-armiya-api.uz", '*']

ALLOWED_HOSTS = ['localhost', "biznes-armiya-api.uz", "biznes-armiya.uz",'*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'channels',
    'users',
    'armiya',
    'corsheaders',
    'drf_spectacular',
    'ckeditor',
    'chat',
    'storages',
]
# ASGI_APPLICATION = 'core.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('127.0.0.1', 6379)],  # Make sure Redis is running on this host and port
#         },
#     },
# }

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

ROOT_URLCONF = 'core.urls'
SPECTACULAR_SETTINGS = {
    'TITLE': 'BiznesArmiya API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

import os
# Static files (CSS, JavaScript, Images)
# https://docsos.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'
#STATIC_ROOT = BASE_DIR / 'static'
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Media files (Uploaded content)
MEDIA_URL = 'https://biznes-armiya-api.uz/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# CKEditor Settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'
CORS_ALLOW_ALL_ORIGINS = False  # Установим False, чтобы указать конкретные домены

CORS_ALLOWED_ORIGINS = [
    "http://biznes-armiya.uz",
    "https://biznes-armiya.uz",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "https://biznes-armiya.uz",  # Укажите ваш фронтенд домен
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
    "X-CSRFToken",
]

# Опционально: указание заголовков, которые нужно вернуть в ответе на запросы
CORS_EXPOSE_HEADERS = [
    'Access-Control-Allow-Origin',
]
CSRF_TRUSTED_ORIGINS = [
    'https://biznes-armiya-api.uz',
    'https://www.biznes-armiya-api.uz',
]

# Опционально: указание заголовков, которые нужно вернуть в ответе на запросы
CORS_EXPOSE_HEADERS = [
    'Access-Control-Allow-Origin',
]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'server2.ahost.uz'  # Example: 'smtp.ahost.com'
EMAIL_PORT = 587       # Example: 587 or 465
EMAIL_USE_TLS = True                     # Use TLS if required (typically port 587)
EMAIL_USE_SSL = False                    # Use SSL if required (typically port 465)
EMAIL_HOST_USER = 'info@biznes-armiya.uz'
EMAIL_HOST_PASSWORD = 'AS2zzCfKCCHMG9n'
DEFAULT_FROM_EMAIL = 'info@biznes-armiya.uz'


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = 'biznesbucket'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
S3_STATIC_DIR = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{S3_STATIC_DIR}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIR = [BASE_DIR / 'static',]
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
