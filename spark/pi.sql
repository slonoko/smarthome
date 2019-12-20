create database pi;
create user sa with encrypted password 'sa';
grant all privileges on database pi to sa;

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