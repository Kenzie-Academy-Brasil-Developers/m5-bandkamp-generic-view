#!/usr/bin/env bash
# exit on error
set -o errexit

# pip install -r requirements.txt
# python.exe -m pip install --upgrade pip
# python -m venv venv
# source venv/Scripts/activate
# python manage.py migrate
python manage.py runserver
