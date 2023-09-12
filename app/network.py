from mininet.topo import Topo
from mininet.node import Node, RemoteController, OVSSwitch
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    def build(self, **_opts):
        # Add 2 routers in two different subnets
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.1.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.2.0.1/24')
        # r3 = self.addHost('r3', cls=LinuxRouter, ip='10.3.0.0/24')
        # r4 = self.addHost('r4', cls=LinuxRouter, ip='10.4.0.0/24')
        # r5 = self.addHost('r5', cls=LinuxRouter, ip='10.5.0.0/24')
        # r6 = self.addHost('r6', cls=LinuxRouter, ip='10.6.0.0/24')

        # r1 = self.addHost('r1', cls=LinuxRouter)
        # r1.cmd('ip link add name r1-eth1 type dummy')
        # r1.cmd('ip addr add 192.168.56.1/24 dev r1-eth1')

        # r2 = self.addHost('r2', cls=LinuxRouter)
        # r3 = self.addHost('r3', cls=LinuxRouter)
        # r4 = self.addHost('r4', cls=LinuxRouter)
        # r5 = self.addHost('r5', cls=LinuxRouter)
        # r6 = self.addHost('r6', cls=LinuxRouter)

        # Add 2 switches
        # s1 = self.addSwitch('s1')
        # s2 = self.addSwitch('s2')

        # Add host-switch links in the same subnet
        # self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.1.0.1/24'})
        # self.addLink(s2, r2, intfName2='r2-eth1', params2={'ip': '10.2.0.1/24'})

        # Add router-router link in a new subnet for the router-router connection
        self.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth2', params1={'ip': '192.168.56.1/24'}, params2={'ip': '10.100.0.2/24'}) # esto no parece hacer nada
        # self.addLink(r1, r3, intfName1='r1-eth3', intfName2='r3-eth2', params1={'ip': '10.200.0.1/24'}, params2={'ip': '10.200.0.2/24'})

        # self.addLink(r1,r2)

        # Adding hosts specifying the default route
        # d1 = self.addHost(name='d1', ip='10.0.0.251/24', defaultRoute='via 10.1.0.1')
        # d2 = self.addHost(name='d2', ip='10.1.0.252/24', defaultRoute='via 10.2.0.1')

        # # Add host-switch links
        # self.addLink(d1, s1)
        # self.addLink(d2, s2)


        # self.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController( name, ip='127.0.0.1' ), switch=OVSSwitch)

    # Add routing for reaching networks that aren't directly connected
    # info(net['r1'].cmd("ip route add 10.1.0.0/24 via 10.100.0.2 dev r1-eth2"))
    # info(net['r2'].cmd("ip route add 10.0.0.0/24 via 10.100.0.1 dev r2-eth2"))

    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()

