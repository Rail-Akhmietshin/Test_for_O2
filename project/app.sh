#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for postgres..."
  sleep 1;
done

echo "PostgreSQL started"


python manage.py migrate
echo "Database created"

python manage.py collectstatic
echo "Static files uploaded"

gunicorn main.wsgi:application --bind 0.0.0.0:8000