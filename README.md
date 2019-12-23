# Smart Home
This is a setup that provides information regarding the temperature, humidity, dust and noise in a specific room (It is meant for indoor usage).

# Installation Guide

## 1. Utility package deployment

## 2. Data streaming with Kafka

## 3. Sensors polling

## 4. Data processing with Spark

## 5. Exposing results via micro services

## 6. UI integration



docker run -d -p 5000:5000 --restart=always --name ek registry:2
minikube start --vm-driver="virtualbox" --insecure-registry="ek:5000"
eval $(minikube docker-env) && docker build -t smarthome:0.1 .
docker tag smarthome:0.1 ek:5000/smarthome:0.1
docker push ek:5000/smarthome:0.1


minikube service ... --url