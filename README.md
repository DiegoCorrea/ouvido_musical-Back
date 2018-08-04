# Ouvido Musical Back End  
## Instalação  
1. Atualização do Ubuntu: `sudo apt update && sudo apt upgrade -y`  
2. Instalação do Pip 3 e Postgres: `sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib build-essential libssl-dev libffi-dev zip`  
3. Instale a Virtual Environment: `sudo pip3 install virtualenv`  

## Configuração  
1. Inicie a Virtual Env: `source venv/bin/activate`  
2. Carregue os arquivos no requirements: ``  
3. Acesse o Python: `python`  
3.1. Importe o nltk: `import nltk`  
3.2. Baixe a base de palavras: `nltk.download('wordnet')`
3.3. Baixe a base de palavras: `nltk.download('wordnet')`    
4. ``  

## O SGBD  
1. `sudo -u postgres psql`  
2. `CREATE DATABASE ouvidoMusical;`  
3. `CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';`  
4. `ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';`  
5. `ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';`  
6. `ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';`  
7. `GRANT ALL PRIVILEGES ON DATABASE ouvidoMusical TO ouvidoMusicalAPI;`  
8. `\q` 

## Migrações do banco  
1. Criando migração do banco: `python manage.py makemigrations`  
2. Aplicando migração ao banco: `python manage.py migrate`  