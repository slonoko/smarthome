# 1. docker build . -t smarthome-db:0.8
# 2. docker run --name smarthomedb -p 5432:5432 smarthome-db:0.8
FROM postgres:12.0-alpine
COPY pi.sh /docker-entrypoint-initdb.d/
