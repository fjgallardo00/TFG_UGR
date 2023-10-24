all: install-ryu install-networkx

install-ryu:
	sudo pip install ./ryu/

install-networkx:
	sudo pip install networkx

exe:
	ryu-manager basic_top_learner.py

exe-links:
	ryu-manager basic_top_learner.py --observe-links

exe-verb:
	ryu-manager --verbose basic_top_learner.py

clone:
	git clone https://github.com/faucetsdn/ryu.git
