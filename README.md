# MESOC REST API

## Setup

1\. Create virtual environment and install dependencies.

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2\. After setting up the virtual environment, run migrations to create database and all of the relevant tables. 
```py
python manage.py migrate
```

Migrations will create city, language and the following user records:
```
dev@mesoc.dev devtest123
mulder@mesoc.dev devtest123
scully@mesoc.dev devtest123
```

3\. Run server locally
```sh
python manage.py runserver [port]
```

## Configuration

Default configration values defined in `mesoc_api/settings.py`

```py
# email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'noreply'
EMAIL_HOST_PASSWORD = 'test'
DEFAULT_FROM_EMAIL = 'noreply@mesoc.dev'
FEEDBACK_EMAIL = 'info@mesoc-project.eu'

# verification, age given in days
VERIFICATION_BASE_URL = 'http://localhost:8000/account/verification'
PASSWORD_RESET_BASE_URL = 'http://localhost:8000/account/password_reset'

VERIFICATION_MAX_AGE = 14
PASSWORD_RESET_MAX_AGE = 14

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'

# cors
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "https://example.org",
#     "https://sub.example.org",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000"
# ]

# Other
FILE_MAX_SIZE = 31457280  # 30 MiB
FILE_ALLOWED_MIME_TYPES = ('text/plain', 'application/pdf')
FILE_ALLOWED_EXTENSIONS = ('txt', 'pdf')

```
