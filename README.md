# Ouvido Musical  
Sistema de Recomendação em Musica  

### Instalação  
1. `sudo apt update`  
2. `sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`  
3. `sudo apt install python-pip`  
4. `sudo pip3 install -U pip`  
5. `sudo pip3 install virtualenv`  
6. `sudo pip3 install virtualenvwrapper`    
7. `sudo pip3 install Django`    
8. `sudo pip3 install sparqlwrapper`  
9. `sudo pip3 install django-cors-headers`  
10. `sudo pip3 install Ipython`  
11. `sudo pip3 install django-extensions`  
11. `sudo pip3 install sklearn`  
11. `sudo pip3 install scipy`  
11. `sudo pip3 install numpy`  
11. `sudo pip3 install nltk`  
11. `sudo pip3 install pandas`  
11. `sudo pip3 install matplotlib`  
11. `sudo pip3 install tornado`  
# nltk.download('wordnet') # first-time use only

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
1. `virtualenv ouvidoMusicalenv`  
2. `source ouvidoMusicalenv/bin/activate`  
Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).  
3. `pip3 install django psycopg2`  
4. `django-admin.py startproject ouvidoMusicalenv .`  

### Iniciando Servidor
1. Acessando o env: `source ouvidoMusicalenv/bin/activate`  
2. Rodando Servidor: `python manage.py runserver`  
3. Acessando Terminal: `python manage.py shell_plus`  

1. Criando migração do banco: `python manage.py makemigrations recommendations`  
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
