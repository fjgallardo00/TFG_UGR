# Utilizar una imagen base de Ubuntu
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    apt-utils \
    sudo

RUN sudo apt-get install -y mininet iproute2 iputils-ping make traceroute iperf3

WORKDIR /home/app
