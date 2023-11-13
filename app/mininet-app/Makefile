all: switch python

switch:
	service openvswitch-switch start

python:
	python3 mininet-network.py

clean:
	sudo mn -c
