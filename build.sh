#!/bin/bash
#eval $(minikube docker-env)

docker build backend -t smarthome-api:0.8
docker build db -t smarthome-db:0.8
docker build frontend -t smarthome-webui:0.8
docker build spark -t smarthome-spark:0.8

docker save smarthome-api > tars/smarthome-api.tar
docker save smarthome-db > tars/smarthome-db.tar
docker save smarthome-webui > tars/smarthome-webui.tar
docker save smarthome-spark > tars/smarthome-spark.tar


# docker tag smarthome-api:0.8 192.168.178.55:32000/smarthome-api:0.8
# docker tag smarthome-db:0.8 192.168.178.55:32000/smarthome-db:0.8
# docker tag smarthome-webui:0.8 192.168.178.55:32000/smarthome-webui:0.8
# docker tag smarthome-spark:0.8 192.168.178.55:32000/smarthome-spark:0.8

# docker push 192.168.178.55:32000/smarthome-api:0.8
# docker push 192.168.178.55:32000/smarthome-db:0.8
# docker push http://192.168.178.55:32000/smarthome-webui:0.8
# docker push 192.168.178.55:32000/smarthome-spark:0.8