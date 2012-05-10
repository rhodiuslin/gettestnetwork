gettestnetwork
==============
A small python scripy that gets a test network from those collected by Mark Newman (http://www-personal.umich.edu/~mejn/netdata/).

Example
=======
Get the "karate" network. If the file does not exist, the script will download the network dataset and uncompress it to the given folder (e.g., '../output') for the first time.
    G = get_network('karate','../output')

