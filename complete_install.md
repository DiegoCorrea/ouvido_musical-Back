# Ouvido Musical  
Sistema de Recomendação em Musica  

### Instalação  
1. `sudo apt update`  
2. `sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib build-essential libssl-dev libffi-dev zip`        
3. `sudo pip3 install -U pip`  
4. `sudo pip3 install virtualenv`    
5. `sudo pip3 install Django django-cors-headers Ipython django-extensions sklearn scipy numpy nltk pandas matplotlib psycopg2 psycopg2-binary`       
6. Acesse o Python: `python`  
6.1. Importe o nltk: `import nltk`  
6.2. Baixe a base de palavras: `nltk.download('wordnet')`    

### Configurando o Banco  
1. `sudo -u postgres psql`  
2. `CREATE DATABASE ouvidoMusical;`  
3. `CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';`  
4. `ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';`  
5. `ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';`  
6. `ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';`  
7. `GRANT ALL PRIVILEGES ON DATABASE ouvidoMusical TO ouvidoMusicalAPI;`  
8. `\q`  

### Configuração  

Caso não exista a pasta:  
1. `virtualenv venv`  
2. `source venv/bin/activate`    

### Iniciando Servidor
1. Acessando o env: `source venv/bin/activate`  
2. Rodando Servidor: `python manage.py runserver`  
3. Acessando Terminal: `python manage.py shell_plus`  
