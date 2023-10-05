from mininet.topo import Topo
from mininet.link import TCLink
from mininet.node import Node

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

    def to_cmd(self, message):
        self.cmd(message)


class TutorialTopologyOld( Topo ):

  def build( self ):
    # add a host to the network
    h1 = self.addHost( 'h1' )

    # add a switch to the network
    s1 = self.addSwitch( 's1' )

    # add a link between the host `h1` and the `s1` switch
    self.addLink( h1, s1 )

class TutorialTopology(Topo):

  def build(self):


    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')

    for i in range(1,6):
      new_host = self.addHost('h'+str(i))
      self.addLink(new_host, s1)

    for i in range(6,11):
      new_host = self.addHost('h'+str(i))
      self.addLink(new_host, s2)

    self.addLink(s1, s2, cls=TCLink, bw=50, delay='30ms', loss=10)

class RealTopology(Topo):

  def build(self):

    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')
    h4 = self.addHost('h4')
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')

    self.addLink(h1, s1, cls=TCLink, bw=100)
    self.addLink(h2, s1, cls=TCLink, delay='75ms')
    self.addLink(h3, s1, cls=TCLink, loss=5)
    self.addLink(h4, s2)
    self.addLink(s1, s2)

class Prueba(Topo):
  def build(self, **_opts):
        # Add 2 routers in two different subnets
        # r1 = self.addHost('r1', cls=LinuxRouter, ip='10.1.0.1/24')
        # r2 = self.addHost('r2', cls=LinuxRouter, ip='10.2.0.1/24')
        # r3 = self.addHost('r3', cls=LinuxRouter, ip='10.3.0.0/24')
        # r4 = self.addHost('r4', cls=LinuxRouter, ip='10.4.0.0/24')
        # r5 = self.addHost('r5', cls=LinuxRouter, ip='10.5.0.0/24')
        # r6 = self.addHost('r6', cls=LinuxRouter, ip='10.6.0.0/24')

        r1 = self.addHost('r1', cls=LinuxRouter)
        r1.cmd('ip link add name r1-eth1 type dummy')
        r1.cmd('ip addr add 192.168.56.1/24 dev r1-eth1')

        r2 = self.addHost('r2', cls=LinuxRouter)
        r3 = self.addHost('r3', cls=LinuxRouter)
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
        self.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth2', params1={'ip': '192.168.56.1/24'}, params2={'ip': '10.100.0.2/24'})
        # self.addLink(r1, r3, intfName1='r1-eth3', intfName2='r3-eth2', params1={'ip': '10.200.0.1/24'}, params2={'ip': '10.200.0.2/24'})

        # Adding hosts specifying the default route
        # d1 = self.addHost(name='d1', ip='10.0.0.251/24', defaultRoute='via 10.1.0.1')
        # d2 = self.addHost(name='d2', ip='10.1.0.252/24', defaultRoute='via 10.2.0.1')

        # # Add host-switch links
        # self.addLink(d1, s1)
        # self.addLink(d2, s2)

        a = 0


topos = { 
  'tutorialTopology': ( lambda: TutorialTopology() ),
  'tutorialTopologyOld': (lambda: TutorialTopologyOld()),
  'realTopology': (lambda: RealTopology()),
  'prueba': (lambda: Prueba())
}
