CREATE DATABASE ouvidoMusicalDez;
CREATE DATABASE ouvidoMusicalCem;
CREATE DATABASE ouvidoMusicalMil;
CREATE DATABASE ouvidoMusicalDezMil;
CREATE DATABASE ouvidoMusicalCemMil;
CREATE DATABASE ouvidoMusicalUmMilhao;
CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';
ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';
ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';
ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalDez TO ouvidoMusicalAPI;
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalCem TO ouvidoMusicalAPI;
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalMil TO ouvidoMusicalAPI;
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalDezMil TO ouvidoMusicalAPI;
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalCemMil TO ouvidoMusicalAPI;
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalUmMilhao TO ouvidoMusicalAPI;