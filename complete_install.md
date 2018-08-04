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
Caso precise de maiores informações acesse o link: `https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04`  
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
4. `django-admin.py startproject venv .`  

### Iniciando Servidor
1. Acessando o env: `source venv/bin/activate`  
2. Rodando Servidor: `python manage.py runserver`  
3. Acessando Terminal: `python manage.py shell_plus`  

1. Criando migração do banco: `python manage.py makemigrations`  
2. Aplicando migração ao banco: `python manage.py migrate`  
3. Carregando base de dados:  
  3.1. Download da base: `https://drive.google.com/open?id=0B567DI6g5hwwN0pwTXlWUENFdUE`  
  3.2. Coloque o arquivo baixado em: `scripts/seed/`  
  3.3. Carregando base pequena: `python manage.py shell < ./scripts/seed/smallSeedScript.py`  
  3.4. Carregando base grande: `python manage.py shell < ./scripts/seed/bigSeedScript.py`  
4. Rodando o calculo de similaridade:  
  4.1. Abra o terminal do Django: `python manage.py shell`  
  4.2. Digite no terminal do Django e espere o calculo terminar: `import similarity`  
  4.3. Saia do terminal digitando: `exit()`  
5. Iniciando servidor: `python manage.py runserver`  


### Links API JSON  
1. Pagina inicial: `http://127.0.0.1:8000/api/v1/`  
2. Usuarios: `http://127.0.0.1:8000/api/v1/users/`  
  2.1. Um Usuario: `http://127.0.0.1:8000/api/v1/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/`  
  2.2. Musicas que o usuario ouviu:   `http://127.0.0.1:8000/api/v1/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/`  
  2.3. A Musica que o usuario ouviu:   `http://127.0.0.1:8000/api/v1/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/`  
  2.3. A Musica que o usuario ouviu:   `http://127.0.0.1:8000/api/v1/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/SOVEUVC12A6310EAF1/`  
  2.4. As musicas recomendadas para o usuario:   `http://127.0.0.1:8000/api/v1/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/recommendations/`  
3. Musicas: `http://127.0.0.1:8000/api/v1/songs/`  
  3.1. Uma Musica: `http://127.0.0.1:8000/api/v1/songs/SOAKIMP12A8C130995/`  
  3.2. Usuarios ouviu a Musica: `http://127.0.0.1:8000/api/v1/songs/SOAKIMP12A8C130995/hearby/`  
  3.3. Usuario ouviu a Musica:   `http://127.0.0.1:8000/api/v1/songs/SOAKIMP12A8C130995/hearby/b80344d063b5ccb3212f76538f3d9e43d87dca9e`  

### Front  
`cd templates`  
1. npm install  
2. npm run dev  
