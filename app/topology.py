from mininet.topo import Topo

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

    self.addLink(s1, s2)


# the topologies accessible to the mn tool's `--topo` flag
# note: if using the Dockerfile, this must be the same as in the Dockerfile
topos = { 'tutorialTopology': ( lambda: TutorialTopology() ) }
