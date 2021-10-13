#!/bin/bash
rm db.sqlite3
rm newMotes/apiMotes/migrations/00*.py
rm newMotes/apiMotes/migrations/__pycache__/*.pyc
rm newMotes/apiMotes/__pycache__/*.pyc
rm newMotes/__pycache__/*.pyc

python manage.py migrate

echo "Inserisci la password per admin:"
python manage.py createsuperuser --email salvosicali@yahoo.it --username admin 

python manage.py makemigrations

python manage.py migrate