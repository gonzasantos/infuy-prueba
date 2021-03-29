#!/usr/bin/env sh
set -e
while ! nc -z db 5432; do sleep 5; done;
python manage.py migrate

uwsgi --http "0.0.0.0:8000" --module infuy.wsgi
#python manage.py runserver 0:8000