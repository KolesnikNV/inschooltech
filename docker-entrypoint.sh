#!/bin/bash
set -x
python manage.py makemigrations
python manage.py migrate
python core/generate_test_data.py
python manage.py collectstatic --noinput
gunicorn labs.wsgi:application --bind 0.0.0.0:8000