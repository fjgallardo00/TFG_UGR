# Ordenes para trabajar con docker compose
all: starting

restart: down starting

starting: up exec

up:
	docker compose up -d

down:
	docker compose down

exec:
	docker exec -ti tfg_ugr-mininet-container-1 bash

# Ordenes para trabajar con un contenedor solo
build:
	docker build -t mininet .

run:
	docker run --privileged --network host -it --name prueba-mininet mininet

start:
	docker start -i prueba-mininet

stop:
	docker stop prueba-mininet

delete:
	docker rm prueba-mininet

delete-image:
	docker rmi mininet

ps:
	docker ps -a

copy:
	docker cp app/. prueba-mininet:/home/app

clean: stop delete

img-clean: clean delete-image
