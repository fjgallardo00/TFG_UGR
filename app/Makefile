all: switch start

switch:
	service openvswitch-switch start

start:
	sudo mn --custom ./topology.py --topo tutorialTopology

clean:
	sudo mn -c
