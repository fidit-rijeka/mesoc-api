"""
Django settings for mesoc_api project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1(9g@&*=vk@bapc77qy1e*28zhj%j*p-90ud*m6elj%g(w1nl-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'core.apps.CoreConfig',
    'anymail'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mesoc_api.urls'

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

WSGI_APPLICATION = 'mesoc_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'core.User'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

EMAIL_HOST_USER = 'noreply'
EMAIL_HOST_PASSWORD = 'test'
DEFAULT_FROM_EMAIL = 'noreply@mail.mesoc.dev'
FEEDBACK_EMAIL = 'info@mesoc-project.eu'

# ANYMAIL = {
#     'IGNORE_RECIPIENT_STATUS': True,
#
#     'MAILGUN_API_KEY': '<api_key>',
#     'MAILGUN_API_URL': 'https://api.eu.mailgun.net/v3',
# }

# Verification and password reset
CORE_API_BASE_URL = 'http://localhost:8000'
CORE_VERIFICATION_BASE_URL = 'https://app.mesoc.dev/verification/verification'
CORE_PASSWORD_RESET_BASE_URL = 'https://app.mesoc.dev/verification/password_reset'
CORE_PROCESSING_SUCCESS_URL = 'https://app.mesoc.dev/my-documents'
CORE_PROCESSING_FAIL_URL = 'https://app.mesoc.dev/upload-document'

VERIFICATION_MAX_AGE = 14
PASSWORD_RESET_MAX_AGE = 14

# Celery

CELERY_BROKER_URL = 'redis://localhost:6379'

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'core.authentication.BearerTokenAuthentication'
    ],

    'DEFAULT_METADATA_CLASS': None
}

# CORS

CORS_ALLOW_ALL_ORIGINS = True

# File upload

FILE_MAX_SIZE = 31457280  # 30 MiB
FILE_ALLOWED_MIME_TYPES = ('text/plain', 'application/pdf')
FILE_ALLOWED_EXTENSIONS = ('txt', 'pdf')

# NLP

CORE_NUM_KEYWORDS = 30
CORE_MIN_SENTENCE_LENGTH = 15

CORE_YAKE_CANDIDATE_NGRAM = 4
CORE_YAKE_CANDIDATE_WINDOW_SIZE = 18
CORE_YAKE_THRESHOLD = 0.95

CORE_CRP_ROW_MODEL = BASE_DIR / 'ml_models' / 'rf_row.pickle'
CORE_CRP_COLUMN_MODEL = BASE_DIR / 'ml_models' / 'rf_column.pickle'
CORE_CRP_TFIDF_VECTORIZER = BASE_DIR / 'ml_models' / 'tfidf_vectorizer.pickle'

CORE_CRP_COLUMN_THRESHOLD = 0.1
CORE_CRP_ROW_THRESHOLD = 0.1

# Repository settings

CORE_CELL_SIMILARITY_THRESHOLD = 0.0

REPOSITORY_DOCUMENT_PREVIEW_URL = 'http://mesoc-doc.uniri.hr'
