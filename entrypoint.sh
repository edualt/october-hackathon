#!/bin/sh

# Check if database is up
python manage.py wait_for_db --settings=core.settings.${enviroment}

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations --settings=core.settings.${enviroment}
python manage.py migrate --settings=core.settings.${enviroment}
python manage.py migrate --run-syncdb --settings=core.settings${enviroment}

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:${PORT} --settings=core.settings.${enviroment}