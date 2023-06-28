build:
	docker build -t mininet .

run:
	docker run -it --name prueba-mininet mininet

stop:
	docker stop prueba-mininet

delete:
	docker rm prueba-mininet

ps:
	docker ps -a

clean: stop delete