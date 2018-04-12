import numpy
import sys
import scipy
import networkx as nx
from collections import defaultdict
import math

graph=open('egonet.txt','r')
e=set()				#Edge Storage
n=set()				#Node Storage
for edge in graph:
	u,v=edge.split()
	u,v = int(u),int(v)
	e.add((u,v))
	e.add((v,u))
	n.add(u)
	n.add(v)

G=nx.Graph()
for i in e:
	G.add_edge(i[0],i[1])

nodesCount=nx.number_of_nodes(G)
edgesCount=nx.number_of_edges(G)
componentCount=nx.number_connected_components(G)
biggestComponent=list(nx.connected_component_subgraphs(G))[0]
nodeCountofbiggestComponent=nx.number_of_nodes(biggestComponent)

print "No. of Nodes:", nodesCount
print "No. of Edges:", edgesCount
print "No. of Connected Components:", componentCount
print "Number of nodes in largest component:", nodeCountofbiggestComponent


comm=list(nx.k_clique_communities(G, 4))
commCount=len(comm)
commList=[]
for k in comm:
    commList.append(list(k))

print "No. of communities:", commCount
print "Found Communities :"
for p,l in enumerate(commList):
    print str(p+1) + ":", l



