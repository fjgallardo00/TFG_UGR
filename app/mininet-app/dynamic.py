from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host
from mininet.link import TCLink
from mininet.cli import CLI

class MyTopology(Topo):
    def build(self):
        h1 = self.addHost('h1', cls=MyHost, ip='10.0.0.1/24', defaultRoute='via 10.0.0.254')
        h2 = self.addHost('h2', cls=MyHost, ip='10.0.0.2/24', defaultRoute='via 10.0.0.254')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

class MyHost(Host):
    def config(self, **params):
        super(MyHost, self).config(**params)
        # Configurar la tabla de enrutamiento si es necesario
        # Ejemplo: self.cmd('route add default gw 10.0.0.254')

def main():
    topo = MyTopology()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    main()
