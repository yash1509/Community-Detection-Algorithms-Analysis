import networkx as nx
import community as com
import matplotlib.pyplot as py
import copy
import sys
import pylab

pylab.show()

def deleteMaxBetweenEdges(G):
	delete = [] 						#Store for saving edges with maximum betweenness which will be removed
	betweenCentral = nx.edge_betweenness_centrality(G)	#Calculate betweeness for each edge in Graph G
	store_max_betweeness= betweenCentral[max(betweenCentral,key=betweenCentral.get)]	#get is used for checking if the key exists in dictionary and returns the value of key
	for findKey,pos in betweenCentral.items():		#Return a copy og yhe dictionary's list of (key,value) pairs.
		if pos==store_max_betweeness:			#Find value matching with max betweeness
			delete.append(findKey)			#Store in delete storage array
	G.remove_edges_from(delete) 				#Delete edges
	listGraph=list(nx.connected_component_subgraphs(G))	#Prepare list of connected components found in the graph
	temp={}							#Temp storage array
	ct=0							#Counter
	
	for g in listGraph:					#Iterate through the list and assign the same name to each node belonging to a specific connected component found 
		ct+=1
		for node in g:
			temp[node]=ct
	if G.number_of_edges() == 0:				#Return result after no edge remains.
		return [list(nx.connected_component_subgraphs(G)),0,G]
	mod = com.modularity(temp,G)				#Return modularity of resulting graph	
	return [list(nx.connected_component_subgraphs(G)),mod,G]#Return result when edges still remain.

if __name__=="__main__":
	foundCommunities=[]					#Store community
	G = nx.read_edgelist(sys.argv[1])			#Read graph from input
	tempGraph=copy.deepcopy(G)				#Deepcopy produces compound objects with copies from original object
	temp={}							#Temp storage
	for node in G:						#Assign each node to a single name community
		temp[node]=0			
	startingModularity=com.modularity(temp,G)		#Calculate inital modularity of the graph
	foundCommunities.append([temp,startingModularity,G]) 	#Store result
	#print "Found :-",foundCommunities
	
	while G.number_of_edges()>0:				#Run until no edge remains
		foundSubGraph = deleteMaxBetweenEdges(G)	#Returns connected components after removing Highest Betweeness Edges
		foundCommunities.append(foundSubGraph)		#Store result
		G=foundSubGraph[-1]				#-1 refers to last element (Count from right instead of left)
	
	for i in foundCommunities:				#Iterate through the sub graphs found and find the highest modularity
		if i[1]>startingModularity:
			t1=i[0]					#Remember the configuration which produced highest modularity
			find=[]
			mod=i[1]				#Store highest modularity found
			
			for g in i[0]:
				find.append(sorted([int(v) for v in g])) # v=vertex, store sorted list of vertex found in the configuration	
	#print find
	for resultingCommunity in find:
		print resultingCommunity			#Print resulting communities found

	temp={}							#Temporary array for storing name assignment
	ct=0							#Use counter to track numbering for node assignment 

	for g in t1:						#Iterate and assign numbering to nodes
		for node in g:
			temp[node]=ct		
		ct+=1

	position=nx.spring_layout(tempGraph)			#Position nodes using Fruchterman-Reingold force directed algorithm [Dictionary of nodes as keys and positions as values]
	colors = ["violet","black","orange","cyan","red","blue","green","yellow","indigo","pink"]	#Community colors
	for i in range(len(t1)):		
		graph=t1[i]		#Subgraph storage in graph variable 
		listncomm = [node for node in graph]	#Node list creation for community assignment and plotting
		nx.draw_networkx_nodes(tempGraph,position,nodelist=listncomm,node_color=colors[i%10],node_size=500,alpha=0.8)	#Plot graph

	nx.draw_networkx_edges(tempGraph,position)		#Plot Edges
	nx.draw_networkx_labels(tempGraph,position,font_size=10)
	py.axis('off')
	py.savefig(sys.argv[2]) 				#Save in outputfile 
		
					
		


