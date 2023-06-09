#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver host.docker.internal:8000