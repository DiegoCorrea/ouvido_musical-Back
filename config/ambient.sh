#!/bin/bash
echo "Bem vindo ao script de ambientação do Ouvido Musical"
echo "São x passos ate a ambientação. Um arquivo de log sera gerado."
sudo apt update > ambientation.log
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib > ambientation.log
sudo -u postgres psql < DB.sql > ambientation.log
source ouvidoMusicalenv/bin/activate > ambientation.log
pip install django psycopg2 > ambientation.log
pip install virtualenv > ambientation.log
pip install virtualenvwrapper > ambientation.log
pip install Django > ambientation.log
pip install sparqlwrapper > ambientation.log
pip install django-cors-headers > ambientation.log
python manage.py migrate > ambientation.log
python manage.py runserver
