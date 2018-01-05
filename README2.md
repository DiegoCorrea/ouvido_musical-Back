### Executando  
1. `source ouvidoMusicalenv/bin/activate`  
2. `python3.6 manage.py runserver`  

### Terminal Django/Projeto  
1. `python3.6 manage.py shell_plus`  

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
