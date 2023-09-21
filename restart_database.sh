#!/bin/bash

if [ -f "./db.sqlite3" ]; then
    echo "Removing existing db.sqlite3..."
    rm ./db.sqlite3
else
    echo "No db.sqlite3 found. Skipping removal."
fi

echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

echo "Importing coupons..."
python manage.py import_coupons

echo "Script completed."