### Executando  
1. Virtual Env: `source ouvidoMusicalenv/bin/activate`  
2. Servidor Django: `python manage.py runserver`  
3. Linux visualizar processadores: `htop`

### Terminal Django/Projeto  
1. `python manage.py shell_plus`  

### Banco de dados   
Para criar os DB, usuarios e garantir privilegios, siga o roteiro a seguir:  
1. Acessar o terminal do postgres, a partir da pasta do projeto: `sudo -u postgres psql`  
2. Executar o script: `\i config/data/createDB.sql;`  
3. Sair do terminal do postgres: `\q`  

### Criando tabelas no banco  
1. `python3.6 manage.py makemigrations`  
2. `python3.6 manage.py migrate`

### Load Data
1. `sudo -u postgres psql ouvido_musical_thousand`  
2. `\i config/data/oneMillionSongs/thousand/loadData.sql;`  
3. `\q`  

### Clean pyc  
1. Limpa todo o cache: `find . -name apps/*.pyc -delete`  
2. Clean migrations: `find . -path "apps/migrations/*.py" -not -name "__init__.py" -delete`

### Pip
1. Reinstalar todos os modulos forçadamente: `pip install --upgrade -r requirements.txt --force-reinstall`  