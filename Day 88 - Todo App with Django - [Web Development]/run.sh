#!/bin/bash

echo "==> ==> Running Database Migration..."

python manage.py makemigrations

python manage.py migrate

echo "==> Running up Server..."

python manage.py runserver