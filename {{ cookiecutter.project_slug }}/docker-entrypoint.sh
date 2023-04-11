#!/bin/bash

echo "Waiting for PostgreSQL to start..."
./wait-for-it.sh db:5432

echo "Migrating database..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
