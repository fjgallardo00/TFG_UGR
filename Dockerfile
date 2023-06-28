# Utilizar una imagen base de Ubuntu
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    apt-utils \
    sudo

RUN sudo apt-get install -y mininet

COPY ./app/ /home/myapp