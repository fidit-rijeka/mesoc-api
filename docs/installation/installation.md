# Installation

This section explains how to set up and deploy the Toolkit on development or production environment. Installation steps assume you will be using virtual Python environment rather than the system installation which is a standard approach, but it is not strictly necessary.

Before moving on, please review following conventions used in the installation instructions below.

* When listing shell commands to execute, those requiring ordinary user permissions are prefixed with `$` while commands requiring superuser permissions are prefixed with `#`.
* `>>>` prefix implies commands are executed in Python interpreter rather than OS shell.
* File paths which are not absolute are relative to the project directory, i.e. the directory containing `manage.py` file.


## Setting up virtual environment

Navigate to the directory where you want to create virtual environment, e.g. project directory and run:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

This will create `venv` directory in the project directory which contains Python virtual environment. To make sure the shell invokes proper Python interpreter, environment needs to be activated by sourcing `venv/bin/activate` file. After activating the environment it is necessary to install Python dependencies listed in `requirements.txt` file.

```{hint}
If you don't have MySQL database installed and want to use SQLite instead, remove `mysqlclient` package from the `requirements.txt` file as it won't be needed and likely won't install anyway.
```

## Installing NLP dependencies

Toolkit's text processing capabilities depend on specific corpora and ML models which need to be installed. First, download `spacy` `en_core_web_sm` pipeline:

```sh
$ python -m spacy download en_core_web_sm
```

Next step is to download NLTK corpora and models. Run Python interpreter:

```sh
$ python
```

then import `nltk` library and download the necessary dependencies:

```py
>>> import nltk
>>> nltk.download(['stopwords', 'punkt', 'omw-1.4', 'wordnet'])
```

```{hint}
You can control the path where NLTK downloads data by modifying `NLTK_DATA` environment variable.
```

## Running the application

Before running the application, it is necessary to specify the configuration file using `DJANGO_SETTINGS_MODULE` environment variable. `meosc_api/settings_dev.py` is optimised for development environment, but for production `mesoc_api/settings_production.py` should be used instead. The variable must contain path to the configuration file relative to the working directory with `.` acting as a separator. Assuming we are running development server from the project directory, `DJANGO_SETTINGS_MODULE` should be defined as:

```sh
$ DJANGO_SETTINGS_MODULE=mesoc_api.settings_dev
```

If `NLTK_DATA` environment variable was modified in the previous step, it should be correctly defined here as well.

Run migrations to set up database tables, and then load necessary data:

```sh
$ python manage.py migrate
$ python manage.py load core/fixtures/location.json
$ python manage.py load core/fixtures/repositorydocument.json
```

## Running background tasks

Documents are processed in the background by Celery worker processes. Application uses Redis on port 6379 as a message transport by default, but this can be configured in `settings.py` by changing `CELERY_BROKER_URL`.
At least 1 task should be run when starting the application, otherwise documents won't be processed. To start a worker task, run the following command from the virtual environment:

```sh
$ celery worker -A mesoc_api worker -l ERROR
```

This will start a worker process with `ERROR` logging level configured. See [Celery workers documentation](https://docs.celeryq.dev/en/v5.0.2/userguide/workers.html) for more information.

## Development environment

Development server can be run with the default configuration located in `mesoc_api/settings_dev.py`. Available configuration options are listed in [configuration options](../configuration_options.md) section.

If you need test users, you can load `user.json` fixture:

```sh
$ python manage.py load core/fixtures/user.json
```

This will create users with following credentials:

| Email                | Password   | API Key / Token                           | Can use export API
|----------------------|------------|------------|-------------------
| dev@mesoc.dev        | devtest123 | c4eeccb224c0cf14ba8bc42dedd64b1a7e8940b0  | Yes
| mulder@mesoc.dev     | devtest123 | f21ba013506b8b3479dbca59d9b84cb743305ef1  | No
| scully@mesoc.dev     | devtest123 | 2b46b5edde25ba9054bb28d3a55fae4047cfdcdb  | No
| repository@localhost | devtest123 | 4efda293b6becbfa61d29b5b7c819ebe2991e5c1  | Yes


Finally, to start the server on port 8000 simply run:

```sh
$ python manage.py runserver
```

```{hint}
You can specify development port by adding port number after `runserver` argument.
```

## Production environment

The recommended approach for serving the API is to use Nginx HTTP server in combination with uWSGI. In addition, setting up production environment requires additional application configuration such as database configuration, external service keys, logging and other. 

### Nginx

### uWSGI

### Application configuration

Reasonable defaults are already configured in `mesoc_api/settings_production.py`, but additional fine-tuning is needed. For a full list of configuration values and their explanation, see [configuration options](../configuration_options.md). 

Start by generating new `SECRET_KEY` used for cryptographic signing. First start Django Python shell:

```sh
$ DJANGO_SETTINGS_MODULE='mesoc_api.settings_dev' python manage.py shell
```

then generate and output new key to terminal:

```py
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

Next configure `ALLOWED_HOSTS` to include hosts from which the API is served. Assuming host is `api.example.org`, `ALLOWED_HOSTS` should be configured as:

```py
ALLOWED_HOSTS = ['api.example.org']
```

Additionally, configure `CORS_ALLOWED_ORIGINS` to allow requests from the frontend host. For example, if frontend application is served on `frontend.example.org` via HTTPS, then the setting should be configured as:

```py
CORS_ALLOWED_ORIGINS = ['https://frontend.example.org']
```

#### Database

Officially, only MySQL database is supported, although [others](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASE-ENGINE) will most likely work. The following is an example configuration of MySQL database running on `localhost:3306`:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf'
        },
        'USER': 'db-user',
        'PASSWORD': 'db-password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'db-name'
    }
}
```

Alternatively, instead of network sockets, connection to the database can be made using UNIX domain sockets if the engine supports it and they are available on the system.

```py
DATABASES = {
    'default': {
        # rest of configuration
        'HOST': '/var/run/mysql'
    }
}
```

Make sure to create the database and the corresponding user with sufficient privileges, e.g.:

```sql
CREATE DATABASE db-name;

CREATE USER 'db-user'@'localhost' IDENTIFIED BY 'db-password';

GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE ON db-name.* TO 'db-user'@'localhost';
```

#### E-mail configuration

By default, the API uses Mailgun service (via [Anymail](https://anymail.dev/en/v8.2/)) for sending verification, password reset and other email. Other backends can be configured by modifying `EMAIL_BACKEND` setting, see [Django documentation](https://docs.djangoproject.com/en/3.1/topics/email/#obtaining-an-instance-of-an-email-backend) for available backends.

In any case, `DEFAULT_FROM_EMAIL` and `CORE_FEEDBACK_EMAIL` should be specified, e.g.:

```py
DEFAULT_FROM_EMAIL = 'noreply@example.org'
CORE_FEEDBACK_EMAIL = 'info@example.org'
```

If using Mailgun, it is necessary to specify Mailgun API key:

```py
ANYMAIL = {
    # rest of configuration
    'MAILGUN_API_KEY': 'mailgun-api-key',
}
```

Links to verification, password reset, and document pages sent via email should be configured as well:

```py
CORE_VERIFICATION_BASE_URL = 'https://frontend.example.org/verification'
CORE_PASSWORD_RESET_BASE_URL = 'https://frontend.example.org/password_reset'
CORE_PROCESSING_SUCCESS_URL = 'https://frontend.example.org/my-documents'
CORE_PROCESSING_FAIL_URL = 'https://frontend.example.org/upload-document'
```

#### Logging

By default, the API will use `WARNING` log level unless specified otherwise via `DJANGO_LOG_LEVEL` environment variable or in the settings file itself. At the very least, path to logging file should be specified in `LOGGING['handlers']['file']`:

```py
LOGGING = {
    # rest of logging configuration
    'handlers': {
        'file': {
            # rest of file handler configuration
            'filename': '/var/log/mesoc/mesoc_api.log'
        },
    }
}
```

```{important}
Make sure the directory containing log files exists and can be written to by the user running the application, e.g. `www-data` for Nginx.
```

CORE_GOOGLE_CLOUD_CREDENTIALS

CORE_GOOGLE_GEO_API_KEY

CORE_REPOSITORY_PREVIEW_URL