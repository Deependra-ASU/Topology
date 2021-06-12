from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
	net = Mininet(controller=RemoteController )
	info('Adding controller\n')
	c1 = net.addController('c1',port=6633)
	c2 = net.addController('c2',port=6655)
	
	info('Adding host\n')
	h1 = net.addHost('h1')
	h2 = net.addHost('h2')
	h3 = net.addHost('h3')
	h4 = net.addHost('h4')
	
	info('Adding Switches\n')
	s1 = net.addSwitch('s1', cls=OVSSwitch)
	
	info('Creating Links\n')
	net.addLink(c1,s1)
	net.addLink(c2,s1)
	net.addLink(h1,s1)
	net.addLink(h2,s1)
	net.addLink(h3,s1)
	net.addLink(h4,s1)
	
	net.get('s1').start([c1,c2])
        
	info( '*** Starting network\n')
	net.start()
	
	info( '*** Running CLI\n' )
	CLI( net )
	
	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()



	
