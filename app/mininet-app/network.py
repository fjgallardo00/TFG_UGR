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
        # r1 = self.addHost('r1', cls=LinuxRouter, ip='10.1.0.1/24')
        # r2 = self.addHost('r2', cls=LinuxRouter, ip='10.2.0.1/24')
        # r3 = self.addHost('r3', cls=LinuxRouter, ip='10.3.0.1/24')
        # r4 = self.addHost('r4', cls=LinuxRouter, ip='10.4.0.1/24')
        # r5 = self.addHost('r5', cls=LinuxRouter, ip='10.5.0.1/24')
        # r6 = self.addHost('r6', cls=LinuxRouter, ip='10.6.0.1/24')

        r1 = self.addHost('r1', cls=LinuxRouter)
        r2 = self.addHost('r2', cls=LinuxRouter)
        r3 = self.addHost('r3', cls=LinuxRouter)
        r4 = self.addHost('r4', cls=LinuxRouter)
        r5 = self.addHost('r5', cls=LinuxRouter)
        r6 = self.addHost('r6', cls=LinuxRouter)

        # Add 2 switches
        # s1 = self.addSwitch('s1')
        # s2 = self.addSwitch('s2')

        # Add host-switch links in the same subnet
        # self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.1.0.1/24'})
        # self.addLink(s2, r2, intfName2='r2-eth1', params2={'ip': '10.2.0.1/24'})

        # Add router-router link in a new subnet for the router-router connection
        self.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth2', params1={'ip': '10.1.0.1/24'}, params2={'ip': '10.1.0.2/24'})
        self.addLink(r1, r3, intfName1='r1-eth2', intfName2='r3-eth1', params1={'ip': '10.3.0.2/24'}, params2={'ip': '10.3.0.1/24'})

        self.addLink(r2, r3, intfName1='r2-eth1', intfName2='r3-eth2', params1={'ip': '10.2.0.1/24'}, params2={'ip': '10.2.0.2/24'})

        self.addLink(r2, r4, intfName1='r2-eth3', intfName2='r4-eth1', params1={'ip': '10.4.0.2/24'}, params2={'ip': '10.4.0.1/24'})
        self.addLink(r3, r5, intfName1='r3-eth3', intfName2='r5-eth1', params1={'ip': '10.5.0.2/24'}, params2={'ip': '10.5.0.1/24'})

        self.addLink(r4, r5, intfName1='r4-eth2', intfName2='r5-eth2', params1={'ip': '10.6.0.1/24'}, params2={'ip': '10.6.0.2/24'})

        self.addLink(r6, r4, intfName1='r6-eth1', intfName2='r4-eth3', params1={'ip': '10.7.0.1/24'}, params2={'ip': '10.7.0.2/24'})
        self.addLink(r6, r5, intfName1='r6-eth2', intfName2='r5-eth3', params1={'ip': '10.8.0.1/24'}, params2={'ip': '10.8.0.2/24'})



        # self.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController( name, 'ryu-container' ), switch=OVSSwitch)

    # Add routing for reaching networks that aren't directly connected


    net['r1'].cmd("ip addr del 10.0.0.1/8 dev r1-eth1")
    net['r1'].cmd("ip addr add 10.1.0.1/24 dev r1-eth1")
    net['r2'].cmd("ip addr del 10.0.0.2/8 dev r2-eth2")
    net['r2'].cmd("ip addr add 10.1.0.2/24 dev r2-eth2")
    net['r3'].cmd("ip addr del 10.0.0.3/8 dev r3-eth1")
    net['r3'].cmd("ip addr add 10.3.0.1/24 dev r3-eth1")
    net['r4'].cmd("ip addr del 10.0.0.4/8 dev r4-eth1")
    net['r4'].cmd("ip addr add 10.4.0.1/24 dev r4-eth1")
    net['r5'].cmd("ip addr del 10.0.0.5/8 dev r5-eth1")
    net['r5'].cmd("ip addr add 10.5.0.1/24 dev r5-eth1")
    net['r6'].cmd("ip addr del 10.0.0.6/8 dev r6-eth1")
    net['r6'].cmd("ip addr add 10.7.0.1/24 dev r6-eth1")

    # ip route add <subnet that i want to connect> via <next step> dev <own router interface>
    net['r1'].cmd("ip route add 10.2.0.0/24 via 10.1.0.2 dev r1-eth1")

    net['r2'].cmd("ip route add 10.2.0.0/24 via 10.1.0.1 dev r2-eth1")

    net['r3'].cmd("ip route add 10.1.0.0/24 via 10.2.0.1 dev r3-eth2")

    net.start()
    CLI(net)
    net.stop()

topos = {
  'NetworkTopo': ( lambda: NetworkTopo() )
}


if __name__ == '__main__':
    setLogLevel('info')
    run()
