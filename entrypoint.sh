#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations --settings=core.settings.local
python manage.py migrate --settings=core.settings.local

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000 --settings=core.settings.local