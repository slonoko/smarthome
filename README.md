# Smart Home
This is a setup that provides information regarding the temperature, humidity, dust and noise in a specific room (It is meant for indoor usage).

# Installation Guide

## 1. Utility package deployment

## 2. Data streaming with Kafka

## 3. Sensors polling

## 4. Data processing with Spark

## 5. Exposing results via micro services

## 6. UI integration


eval $(minikube docker-env)
docker run -d -p 5000:5000 --restart=always --name ek registry:2
minikube start --vm-driver="virtualbox" --insecure-registry="ek:5000"

kubectl expose deployment hello-minikube --type=NodePort --port=8080

minikube service ... --url

using ingress:
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: smart-home-ui
spec:
  rules:
    - host: webui.192.168.99.100.nip.io
      http:
        paths:
          - backend:
             serviceName: smart-home-ui
             servicePort: 80