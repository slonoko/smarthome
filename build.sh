#!/bin/bash
eval $(minikube docker-env)

docker build backend -t localhost:32000/smarthome-api:0.8
docker build db -t localhost:32000/smarthome-db:0.8
docker build frontend -t localhost:32000/smarthome-webui:0.8
docker build spark -t localhost:32000/smarthome-spark:0.8

# docker save smarthome-api > tars/smarthome-api.tar
# docker save smarthome-db > tars/smarthome-db.tar
# docker save smarthome-webui > tars/smarthome-webui.tar
# docker save smarthome-spark > tars/smarthome-spark.tar


docker tag smarthome-api:0.8 localhost:32000/smarthome-api:0.8
docker tag smarthome-db:0.8 localhost:32000/smarthome-db:0.8
docker tag smarthome-webui:0.8 localhost:32000/smarthome-webui:0.8
docker tag smarthome-spark:0.8 localhost:32000/smarthome-spark:0.8

docker push localhost:32000/smarthome-api:0.8
docker push localhost:32000/smarthome-db:0.8
docker push http://localhost:32000/smarthome-webui:0.8
docker push localhost:32000/smarthome-spark:0.8