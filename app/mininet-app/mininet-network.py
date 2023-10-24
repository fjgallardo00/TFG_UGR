from mininet.topo import Topo
from mininet.node import Node, RemoteController, OVSSwitch
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class NetworkTopo(Topo):
    def build(self, **_opts):

        sn1 = self.addHost('sn1', ip='10.1.0.1/24')
        sn2 = self.addHost('sn2', ip='10.1.0.2/24')
        sn3 = self.addHost('sn3', ip='10.1.0.3/24')

        dn1 = self.addHost('dn1', ip='10.1.0.4/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        self.addLink(sn1, s1)
        self.addLink(sn2, s1)
        self.addLink(sn3, s1)

        self.addLink(dn1, s2)
        #
        # # Path 0
        self.addLink(s1, s2)
        #
        # # Path 1
        self.addLink(s1, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s2)
        #
        # # Path 2
        self.addLink(s1, s5)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s2)


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
