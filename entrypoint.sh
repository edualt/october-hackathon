#!/bin/sh

# Check if database is up
python manage.py wait_for_db --settings=core.settings.${environment}

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations --settings=core.settings.${environment}
python manage.py migrate --settings=core.settings.${environment}
python manage.py migrate --run-syncdb --settings=core.settings.${environment}

# Start server
echo "Starting server"
gunicorn --env DJANGO_SETTINGS_MODULE=core.settings.${environment} core.wsgi:application --bind