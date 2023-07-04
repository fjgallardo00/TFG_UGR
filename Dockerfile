# Utilizar una imagen base de Ubuntu
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    apt-utils \
    sudo

RUN sudo apt-get install -y mininet iproute2 iputils-ping make traceroute

WORKDIR /home/app

COPY ./app/ .

# No sé si hay que hacer esto desde aquí o hacerlo con un script al ejecutar el dockerfile
#RUN sudo service openvswitch-switch start