#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create database pi;
    create user sa with encrypted password 'sa';
    grant all privileges on database pi to sa;

    \c pi
    
    CREATE TABLE dust (
        enddate timestamp without time zone,
        value double precision,
        voltage double precision,
        density double precision,
        startdate timestamp without time zone,
        id bigserial PRIMARY KEY
    );

    CREATE TABLE temperature (
        temperature double precision,
        humidity double precision,
        "timestamp" timestamp without time zone,
        id bigserial PRIMARY KEY
    );

    GRANT SELECT,UPDATE,DELETE,INSERT ON ALL TABLES IN SCHEMA public TO sa; 
    grant all on sequence temperature_id_seq to sa;
    grant all on sequence dust_id_seq to sa;
EOSQL