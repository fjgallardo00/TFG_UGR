from mininet.topo import Topo
from mininet.link import TCLink

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

topos = { 
  'tutorialTopology': ( lambda: TutorialTopology() ),
  'tutorialTopologyOld': (lambda: TutorialTopologyOld()),
  'realTopology': (lambda: RealTopology())
}
