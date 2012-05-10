gettestnetwork
==============
A small python scripy that gets a test network from those collected by Mark Newman (http://www-personal.umich.edu/~mejn/netdata/).

Example
=======
Get the "karate" network. If the file does not exist, the script will download the network dataset and uncompress it to the given folder (e.g., '../output') for the first time.
<pre>
from get_test_network import get_network

G = get_network('karate','../output')
print 'network size:','(|V|=%d,|E|=%d)'%(G.number_of_nodes(),G.number_of_edges())
</pre>
