all: switch python

switch:
	service openvswitch-switch start

python:
	python3 network.py

start:
	sudo mn --custom ./topology.py --topo tutorialTopology

clean:
	sudo mn -c
