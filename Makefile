# Ordenes para trabajar con docker compose
all: up

restart: down up

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --remove-orphans

exec-mininet:
	docker exec -ti tfg_ugr-mininet-container-1 bash

exec-ryu:
	docker exec -ti tfg_ugr-ryu-container-1 bash

ps:
	docker ps -a

restart-systemctl:
	sudo systemctl restart docker.service docker.socket
