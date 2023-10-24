all: switch python

switch:
	service openvswitch-switch start

exe:
	sudo mn --custom ./network.py --topo NetworkTopo --controller=remote,ryu-container

python:
	python3 mininet-network.py

start:
	sudo mn --custom ./topology.py --topo tutorialTopology

clean:
	sudo mn -c
