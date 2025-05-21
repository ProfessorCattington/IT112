#!/bin/bash

echo "Database migration command"
python manage.py migrate
echo "running server..."
python manage.py runserver 0.0.0.0:8000