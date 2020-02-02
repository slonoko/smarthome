#!/bin/bash
# docker run --rm -it -p 5432:5432/tcp  -e POSTGRES_PASSWORD=postgres -v "/home/elie/Workspace/smarthome/db/":"/docker-entrypoint-initdb.d/" postgres:12.0-alpine

set -e

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    create database $CX_DB_NAME;
    create user $CX_DB_USER with encrypted password '$CX_DB_PWD';
    grant all privileges on database $CX_DB_NAME to $CX_DB_USER;

    \c $CX_DB_NAME
    
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

    GRANT SELECT,UPDATE,DELETE,INSERT ON ALL TABLES IN SCHEMA public TO $CX_DB_USER; 
    grant all on sequence temperature_id_seq to $CX_DB_USER;
    grant all on sequence dust_id_seq to $CX_DB_USER;
EOSQL