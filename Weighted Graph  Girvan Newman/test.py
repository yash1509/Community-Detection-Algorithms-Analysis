import networkx as nx
import csv
import math
import random as rand
import sys

#Graph Reading Method from the input file
def readGraph(G,file_,delimi_):
	read=csv.reader(open(file_), delimiter=delimi_)
	for line in read:
		if len(line)>2:
			if float(line[2])!=0.0:
				G.add_edge(int(line[0]),int(line[1]),w=float(line[2]))			#u,v,w Style of Input File
		else:
			G.add_edge(int(line[0]),int(line[1]),w=1.0)					#u,v Style of Input File

#Method for computing edge betweeness and detecting splitting of connected component into two
def communityGirvanmodule(G):
	initial_components=nx.number_connected_components(G)
	copytemp=initial_components
	while copytemp<=initial_components:
		betweeness=nx.edge_betweenness_centrality(G, weight='w')
		maxcentrality=max(betweeness.values())
		#Remove highest centrality edges
		for k,v in betweeness.iteritems():
			if float(v)==maxcentrality:
				G.remove_edge(k[0],k[1])
		copytemp=nx.number_connected_components(G)	#Recalculate the number of connected component in the graph

#Method for calculating the modularity of split found
def GNModularity(G,deg_,m_):
	matrix=nx.adj_matrix(G)
	degree={}
	degree=UpdateDegree(matrix, G.nodes())
	componentList= comps = nx.connected_components(G)
	print 'No of communities found in split-ed G: %d' % nx.number_connected_components(G)
	modularity = 0.0
	for i in componentList:
		edge_within_community = 0.0
		random_edge= 0.0
		for j in i:
			edge_within_community+=degree[j]
			random_edge+=deg_[j]			#probability od random edge
		modularity= ( float(edge_within_community) - float(random_edge*random_edge)/float(2*m_) )
	modularity=modularity/float(2*m_)
	return modularity

def UpdateDegree(A, nodes):
	degree_dictionary={}
	n=len(nodes)
	temp = A.sum(axis = 1)
	for i in range(n):
		degree_dictionary[nodes[i]] = temp[i,0]
	return degree_dictionary

#Run Girvan Newman module and maximize modularity
def runGNalgo(G,original_degree,m_):
	maxQ = 0.0
	Q = 0.0
	while True:
		communityGirvanmodule(G)
		Q = GNModularity(G, original_degree, m_)
		print "Modularity of split-ed G: %f" %Q
		if Q>maxQ:
			maxQ=Q
			bestComponent = nx.connected_components(G)
			print "Components:", bestComponent
		if G.number_of_edges()==0:
			break
	if maxQ > 0.0:
        	print "Maximum modularity found (Q): %f" %maxQ
        	print "Graph communities found:", bestComponent
    	else:
        	print "Max modularity (Q): %f" %maxQ

def main(argv):
	graph=argv[1]	
	G = nx.Graph()
	readGraph(G, graph, ',')
    	vertices = G.number_of_nodes()    
	mat = nx.adj_matrix(G)    	#adjacency matrix storage
	m_=0.0 	#weight version storage for tracking no of edges
	for i in range(0,vertices):
		for j in range(0,vertices):
			m_+=mat[i,j]
	m_=m_/2.0
	#Calculate weight degree for every node
	original_degree={}
	original_degree=UpdateDegree(mat,G.nodes())
	#Run the algorithm
	runGNalgo(G,original_degree,m_)

if __name__ == "__main__":
    sys.exit(main(sys.argv))			
