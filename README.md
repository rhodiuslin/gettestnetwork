gettestnetwork
==============
A small python scripy that gets a test network from those collected by Mark Newman (http://www-personal.umich.edu/~mejn/netdata/).

Example
=======
The following script returns the "karate" network. If the network file does not exist, the script tries to download the network dataset and uncompress it into the folder you specify (e.g., '../output') for the first time.

    from get_test_network import get_network

    G = get_network('karate','../output')
    print 'network size:','(|V|=%d,|E|=%d)'%(G.number_of_nodes(),G.number_of_edges())

Requirements
============

[python][] 2.x and [networkx][] 

[python]:     http://python.org/
[networkx]:   http://networkx.lanl.gov
