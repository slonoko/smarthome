FROM ubuntu:latest
ADD *.py /app/
ADD requirements.txt /app
WORKDIR /app
RUN apt update && apt upgrade
RUN apt install -y python3 python3-pip openjdk-8-jdk maven git wget
RUN pip3 install -r requirements.txt


