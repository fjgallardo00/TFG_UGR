# Utilizar una imagen base de Ubuntu
FROM ubuntu:latest

RUN apt-get update && apt-get install -y apt-utils sudo
RUN sudo apt update
RUN sudo apt-get install -y mininet iproute2 wget iputils-ping make traceroute iperf3 git pip systemctl curl
RUN sudo apt-get install -y tcpdump

WORKDIR /home/app/mininet-app/
