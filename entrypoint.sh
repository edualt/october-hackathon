#!/bin/sh

# Check if database is up
python manage.py wait_for_db --settings=core.settings.local

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations --settings=core.settings.local
python manage.py migrate --settings=core.settings.local

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000 --settings=core.settings.local