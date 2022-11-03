# django-wishlist
Simple wishlist with email feedback

# Deployment

## Env variables

    SECRET_KEY          : String
    ALLOWED_HOSTS       : ',' separated list

    DEBUG               : Boolean
    DEVELOPMENT_MODE    : Boolean

    EMAIL_HOST          : String
    EMAIL_PORT          : String
    EMAIL_HOST_USER     : String
    EMAIL_HOST_PASSWORD : String
    EMAIL_USE_SSL       : Boolean

    DATABASE_URL        : String

## Run command

    gunicorn --worker-tmp-dir /dev/shm django_wishlist.wsgi:application

# DEV

## Basic django / dev commands

### Generate requirements.txt with poetry

    poetry export -f requirements.txt --output requirements.txt
    poetry export -f requirements.txt --output requirements.txt --without-hashes

### Database Management

    python manage.py makemigrations
    python manage.py migrate

### Create Root User

    python manage.py createsuperuser

### Run dev server

    python manage.py runserver
