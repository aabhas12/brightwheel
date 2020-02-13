#!/bin/sh

# install dependencies
cd /code
pipenv install --dev

# run migrations
#pipenv run python manage.exe.py migrate

# start dev server for use w/ remote debugger
pipenv run python manage.py runserver 0.0.0.0:8000