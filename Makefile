build:
	docker build -t mininet .

run:
	docker run -it --name prueba-mininet mininet

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

clean: stop delete

img-clean: clean delete-image