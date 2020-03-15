#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER galleryapi WITH LOGIN PASSWORD 'galleryapi';
    CREATE DATABASE galleryapi;
    GRANT ALL PRIVILEGES ON DATABASE galleryapi TO galleryapi;
EOSQL
