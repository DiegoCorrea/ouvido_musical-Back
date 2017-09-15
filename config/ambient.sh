#!/bin/bash
echo "Bem vindo ao script de ambientação do Ouvido Musical"
echo "São x passos ate a ambientação. Um arquivo de log sera gerado."
sudo apt-get install aptitude
sudo aptitude update > ambientation.log
echo "Preparando para Instação de pacotes"
sudo aptitude install python3-pip python3-dev libpq-dev postgresql postgresql-contrib > ambientation.log
echo "Criando banco"
sudo -u postgres psql < DB.sql > ambientation.log
echo "Instalando virtualenv"
pip install virtualenv > ambientation.log
echo "Instalando virtualenv wrapper"
pip install virtualenvwrapper > ambientation.log
echo "Abrindo Python Env"
source ouvidoMusicalenv/bin/activate > ambientation.log
echo "Instalando Modulo Django para Postgres"
pip install django psycopg2 > ambientation.log
echo "Instalando Django"
pip install Django > ambientation.log
echo "Instalando sparqlwrapper"
pip install sparqlwrapper > ambientation.log
echo "Instalando Cors"
pip install django-cors-headers > ambientation.log
echo "Migrate"
python manage.py migrate > ambientation.log
