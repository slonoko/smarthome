#!/bin/bash
eval $(minikube docker-env)

docker build backend -t smarthome-api:0.8
docker build db -t smarthome-db:0.8
docker build frontend -t smarthome-webui:0.8
docker build spark -t smarthome-spark:0.8

docker tag smarthome-api:0.8 cx:5000/smarthome-api:0.8
docker tag smarthome-db:0.8 cx:5000/smarthome-db:0.8
docker tag smarthome-webui:0.8 cx:5000/smarthome-webui:0.8
docker tag smarthome-spark:0.8 cx:5000/smarthome-spark:0.8

docker push cx:5000/smarthome-api:0.8
docker push cx:5000/smarthome-db:0.8
docker push cx:5000/smarthome-webui:0.8
docker push cx:5000/smarthome-spark:0.8