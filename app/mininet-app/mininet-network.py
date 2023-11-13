from mininet.topo import Topo
from mininet.node import Node, RemoteController, OVSSwitch
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class NetworkTopo(Topo):
    def build(self, **_opts):
        # self.doble_anillo()
        # self.estrella_extendida()
        self.personalizada()

    def personalizada(self):
        h1 = self.addHost('h1', ip='10.1.0.1/24')
        h2 = self.addHost('h2', ip='10.1.0.2/24')
        h3 = self.addHost('h3', ip='10.1.0.3/24')
        h4 = self.addHost('h4', ip='10.1.0.4/24')
        h5 = self.addHost('h5', ip='10.1.0.5/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s2)
        self.addLink(h5, s7)

        # Path 0
        self.addLink(s1, s2)

        # Path 1
        self.addLink(s1, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s2)

        # Path 2
        self.addLink(s1, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s2)

    def doble_anillo(self):

        h1 = self.addHost('h1', ip='10.1.0.1/24')
        h2 = self.addHost('h2', ip='10.1.0.2/24')
        h3 = self.addHost('h3', ip='10.1.0.3/24')
        h4 = self.addHost('h4', ip='10.1.0.4/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Anillo 1
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)

        # Anillo 2
        self.addLink(h4, s4)
        self.addLink(h3, s4)
        self.addLink(s2, s4)
        self.addLink(s3, s4)

    def estrella_extendida(self):
        h1 = self.addHost('h1', ip='10.1.0.1/24')
        h2 = self.addHost('h2', ip='10.1.0.2/24')
        h3 = self.addHost('h3', ip='10.1.0.3/24')
        h4 = self.addHost('h4', ip='10.1.0.4/24')
        h5 = self.addHost('h5', ip='10.1.0.5/24')
        h6 = self.addHost('h6', ip='10.1.0.6/24')
        h7 = self.addHost('h7', ip='10.1.0.7/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Punta 1
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s2, s1)

        # Punta 2
        self.addLink(s3, h3)
        self.addLink(s3, h4)
        self.addLink(s3, s1)

        # Punta 3
        self.addLink(s4, h5)
        self.addLink(s4, h6)
        self.addLink(s4, s1)

        # Punta 4
        self.addLink(s5, h7)
        self.addLink(s5, s1)


def installFlows(net):
    for sw in net.switches:
        # info('Adding flows to %s... \n' % sw.name)
        for i in range(len(sw.ports)):
            sw.dpctl('add-flow', 'in_port=%s,actions=controller' % i)

        # info(sw.dpctl('dump-flows'))

def infoPorts(net):
    for sw in net.switches:
        info('Port info for %s: ' % sw.name)
        port_info = sw.dpctl("dump-ports")
        info(port_info)
        info('\n')

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController( name, 'ryu-container' ), switch=OVSSwitch)

    net.start()
    installFlows(net)
    # infoPorts(net)
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
