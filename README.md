# Ouvido Musical
Sistema de Recomendação em Musica  

### Instalação  
1. `sudo apt install python-pip`  
2. `sudo pip install -U pip`  
3. `sudo pip install virtualenv`  
4. `sudo pip install virtualenvwrapper`  
5. `sudo pip install Django`  

### Configuração  

1. Criando migração do banco: `python manage.py makemigrations recommendations`  
2. Aplicando migração ao banco: `python manage.py migrate`  
3. Carregando base de dados:  
  3.1. Base pequena:
    3.1.1. Download da base: `aa`  
    3.1.2. Colocoque o arquivo baixado em: `scripts/seed/`
    3.1.3. Carregando a base: `python manage.py shell < ./scripts/seed/smallSeedScript.py`  
  3.2. Base grande:  
    3.2.1. Download da base: `bb`  
    3.2.2. Colocoque o arquivo baixado em: `scripts/seed/`  
    3.2.3. Carregando a base: `python manage.py shell < ./scripts/seed/bigSeedScript.py`  
4. Rodando o calculo de similaridade:
  4.1. Abra o terminal do Django: `python manage.py shell`  
  4.2. Digite no terminal do Django e espere o calculo terminar: `import similarity`  
  4.3. Saia do terminal digitando: `exit()`
5. Iniciando servidor: `python manage.py runserver`  

### Links API JSON  
1. Pagina inicial: `http://127.0.0.1:8000/recommendations/`  
2. Usuarios: `http://127.0.0.1:8000/recommendations/users/`  
  2.1. Um Usuario: `http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/`  
  2.2. Musicas que o usuario ouviu: `http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/`  
  2.3. A Musica que o usuario ouviu: `http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/`  
  2.3. A Musica que o usuario ouviu: `http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/songs/SOVEUVC12A6310EAF1/`  
  2.4. As musicas recomendadas para o usuario: `http://127.0.0.1:8000/recommendations/users/b80344d063b5ccb3212f76538f3d9e43d87dca9e/recommendations/`  
3. Musicas: `http://127.0.0.1:8000/recommendations/songs/`  
  3.1. Uma Musica: `http://127.0.0.1:8000/recommendations/songs/SOAKIMP12A8C130995/`  
  3.2. Usuarios ouviu a Musica: `http://127.0.0.1:8000/recommendations/songs/SOAKIMP12A8C130995/hearby/`  
  3.3. Usuario ouviu a Musica: `http://127.0.0.1:8000/recommendations/songs/SOAKIMP12A8C130995/hearby/b80344d063b5ccb3212f76538f3d9e43d87dca9e`  
