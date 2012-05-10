#!/usr/bin/env python

'''
get_test_network.py - load a test network and convert it to networkx object
    if the network doesn't exist, automatically download the newman's test networks and uncompress them to the given folder
    see: http://www-personal.umich.edu/~mejn/netdata/
    available networks:
	tiny: karate (|V|=34,|E|=78), adjnoun, dolphins, football, lesmis (|V|=77,|E|=254), polbooks (|V|=105,|E|=441)
	small: celegansneural (|V|=297,|E|=2359), hep-th, netscience (|V|=1589,|E|=2742), polblogs, power
	large: as-22july06, astro-ph, cond-mat-2003, cond-mat-2005, cond-mat

@author: Yu-Ru Lin
@contact: yuruliny@gmail.com
@date: May 10, 2011

'''

import os
from browsefiles import Walk
import networkx

download_url = 'http://www.yurulin.com/download/datasets/newman_netdata.tgz'

def check_data_exist(network_name,datapath=None):
    ifilename = '%s/%s.gml'%(datapath,network_name)
    if os.path.exists(ifilename): return ifilename
    ifilename = '%s/newman_netdata/%s.gml'%(datapath,network_name)
    if os.path.exists(ifilename): return ifilename
    
    newdatapath = '%s/newman_netdata'%datapath
    if not os.path.exists(newdatapath):
	print 'data not exist; download data from server...'
	os.system('mkdir -p %s'%datapath)
	command = 'cd %s; wget %s; tar xvf newman_netdata.tgz'%(datapath,download_url)
	os.system(command)
    datapath = newdatapath
    ifilename = '%s/%s.gml'%(datapath,network_name)
    if os.path.exists(ifilename): return ifilename
    # os.system('cd %s; pwd'%datapath)
    file_pattern = '*.zip'
    files = sorted(Walk(datapath, 1, file_pattern))
    print 'get %d network files from %s' % (len(files),datapath)
    for f in files:
	command = 'unzip -o %s -d "%s"'%(f,datapath)
	print command
	os.system(command)
    print 'finished.'
    ifilename = '%s/%s.gml'%(datapath,network_name)
    if not os.path.exists(ifilename):
	print 'error: network file does not exist -',ifilename
	return None
    return ifilename
def get_network(name = 'karate', datapath = '.', relabel=True):
    ifilename = check_data_exist(name,datapath)
    G = networkx.read_gml(ifilename,relabel=relabel) 
    print 'network',name,'(|V|=%d,|E|=%d)'%(G.number_of_nodes(),G.number_of_edges())
    return G


if __name__ == '__main__':
    # example usage
    G = get_network('karate','../output',relabel=False)
    # print G.nodes()
    # print G.edges()
    
