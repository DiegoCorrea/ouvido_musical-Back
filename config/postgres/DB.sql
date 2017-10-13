CREATE DATABASE ouvidoMusicalSmaller;
CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';
ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';
ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';
ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalSmaller TO ouvidoMusicalAPI;

CREATE DATABASE ouvidoMusicalBigger;
CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';
ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';
ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';
ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ouvidoMusicalBigger TO ouvidoMusicalAPI;
