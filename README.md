# Smart Home

This is a setup that provides information regarding the temperature, humidity, dust and noise in a specific room (It is meant for indoor usage).

For this setup, I need 2 hosts, the raspberryPi and another PC/Server. Running kafka, spark and postgres on the raspberry is bit too much ...

1. **Raspberry Pi**: I deployed the `publisher` and `kafka`
2. **Server**: I deployed `spark`, `backend` (APIs) and `frontend`. And because ... well why not, everything runs in a [Minikube](https://github.com/kubernetes/minikube) cluster.

*I might eventually migrate my api backend to serverless functions running under* [Kubeless](http://kubeless.io/)

## Product Architecture

![Solution architecture](https://git.codextension.io/elie/smarthome/-/wikis/uploads/6ff551d9759422ea542a0c4099075971/Total_view.svg)

## 1. Data streaming with Kafka

1. Download [Apache Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/2.4.0/kafka_2.11-2.4.0.tgz) (*scala version 2.11*), and extract the archive anywhere you want `(ex: under home dir)`
2. Set the kafka home environment variable as follows:

  ```bash
  export KAFKA_HOME=<full_path>/kafka_2.11-2.3.1
  ```

3. Allow kafka to expose it's IP address to other devices by setting `advertised.host.name` in **server.properties** and `metadata.broker.list` in **producer.properties** to public IP address and `host.name` to 0.0.0.0
4. Goto the `kafka` folder and run the following command:

  ```bash
  sh kafka_start.sh
  ```

## 2. Sensors polling

1. Goto the `publisher` folder, and install the dependencies

  ```python
  pip3 install -r requirements.txt
  ```

2. Set the environment variable `CX_KAFKA_URL` as follows:

  ```bash
  export CX_KAFKA_URL="<kafka_server_ip>:9092"
  ```

3. Start the publisher

  ```bash
  nohup python3 sensors_init.py > sensors.log &
  ```

## 3. Data processing with Spark

### Configure Spark

1. Download [Apache Spark](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz) (*scala version 2.11*), and extract the archive anywhere you want `(ex: under home dir)`
2. Set the spark home environment variable as follows:

  ```bash
  export SPARK_HOME=<full_path>/spark-2.4.4-bin-hadoop2.7
  ```

### Start Spark runner

1. Goto the `spark` folder, and install the dependencies

  ```python
  pip3 install -r requirements.txt
  ```

2. Set the environment variables as follows (*replace the ip and user/pwd with yours*):

  ```bash
  export CX_KAFKA_URL="localhost:9092"
  export CX_DB_URL="jdbc:postgresql://localhost:5432/pi"
  export CX_DB_DRIVER="org.postgresql.Driver"
  export CX_DB_USER="sa"
  export CX_DB_PWD="sa"
  ```

3. Start the spark bootstrapper

  ```bash
  nohup python3 spark_init.py >/dev/null 2>&1 &
  ```

## 4. Installing Minikube, Docker and Kubeless

### Minikube

```bash
minikube start --vm-driver="kvm2" --insecure-registry="ek:5000" --memory="4000mb"
eval $(minikube docker-env)
docker run -d -p 5000:5000 --restart=always --name ek registry:2

kubectl create ns kubeless
kubectl label namespace kubeless istio-injection=enabled
kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.5/kubeless-v1.0.5.yaml
kubectl create -f https://raw.githubusercontent.com/kubeless/kubeless-ui/master/k8s.yaml

kubectl create ns smart-home
kubectl label namespace smart-home istio-injection=enabled

kubectl expose deployment hello-minikube --type=NodePort --port=8080

minikube service ... --url
```

### Docker

```bash
docker run -d -p 5000:5000 --restart always --name registry registry:2

docker build backend -t smarthome-api:0.8
docker build db -t smarthome-db:0.8
docker build frontend -t smarthome-webui:0.8

docker tag smarthome-api:0.8 localhost:5000/smarthome-api:0.8
docker tag smarthome-db:0.8 localhost:5000/smarthome-db:0.8
docker tag smarthome-webui:0.8 localhost:5000/smarthome-webui:0.8

docker push ek:5000/smarthome-api:0.8
docker push ek:5000/smarthome-db:0.8
docker push ek:5000/smarthome-webui:0.8
```

### Kubeless

Navigate to the `backless` folder.

first make sure, to install [Kubeless](https://kubeless.io/) along with the `Serverless` nodejs plugin.

once done, run the following from command line:

```bash
serverless deploy
```

## 5. Deployment Postgres Database

Navigate to the `config\apps` folder.

run the following in the command line:

```bash
kubectl apply -f db.all.yml
```

## 6. Exposing results via micro services

Navigate to the `config\apps` folder.

run the following in the command line:

```bash
kubectl apply -f backend.all.yml
```

## 7. UI integration

Navigate to the `config\apps` folder.

run the following in the command line:

```bash
kubectl apply -f frontend.all.yml
```


## Miscellaneous

```yml
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
```

```bash
curl --location --request POST 'http://smart-home.info/temperature/range' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "from_date":"2020-01-02",
    "to_date":"2020-01-04"
}'
```

```bash
kubectl label namespace default istio-injection=enabled
```

```bash
kubectl proxy --address='0.0.0.0' --disable-filter=true
```