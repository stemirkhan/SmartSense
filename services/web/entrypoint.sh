#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

flask db upgrade

python3 create_db.py

gunicorn --bind 0.0.0.0:5000 wsgi:app

exec "$@"
