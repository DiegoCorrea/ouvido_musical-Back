# Ouvido Musical Back End  
## Instalação  
1. Atualização do Ubuntu: `sudo apt update && sudo apt upgrade -y`  
2. Instalação do Pip 3 e Postgres: `sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib build-essential libssl-dev libffi-dev zip unzip`  
3. Instale a Virtual Environment: `sudo pip3 install virtualenv`  

## Configuração  
1. Criando a Virtual Env local: `virtualenv venv`  
2. Inicie a Virtual Env: `source venv/bin/activate`  
3. Carregue os arquivos no requirements: `pip install -r requirements.txt`  
4. Acesse o Python: `python`  
4.1. Importe o nltk: `import nltk`  
4.2. Baixe a base de palavras: `nltk.download('wordnet')`  
4.3. Baixe a base de palavras: `nltk.download('wordnet')`  
4.4. `exit()`        
5. Instalando os modulos: `pip install requirements.txt`  

## O Postgres  
1. `sudo -u postgres psql`  
2. `CREATE DATABASE ouvido_musical;`  
3. `CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';`  
4. `ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';`  
5. `ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';`  
6. `ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';`  
7. `GRANT ALL PRIVILEGES ON DATABASE ouvidoMusical TO ouvidoMusicalAPI;`  
8. `\q` 

## Migrações do banco  
1. Criando migração do banco: `python manage.py makemigrations`  
2. Aplicando migração ao banco: `python manage.py migrate`  

## Extraindo o dataset  
1. Descompactar o dataset: `cd datasets/oneMillionSongs/ && unzip original_set.zip && cd ../../`  
2. Abra o terminal do Django: `python manage.py shell_plus`  
3. Importe a função: `from datasets.oneMillionSongs.clean_set import clean_all_files`  
4. Execute a função: `clean_all_files()`  
5. Importe o arquivo: `from datasets.oneMillionSongs.mining import main`  
6. Execute a função: `main()`  
7. `exit()`  

## Importando o set para o Postgres  
1. Entrar no painel do banco: `sudo -u postgres psql ouvido_musical`  
2. Carregar os dados extraidos no banco: `\i datasets/oneMillionSongs/sets/{pasta_do_set}/load.sql;`  
3. `\q`  

