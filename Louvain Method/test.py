import community
import networkx as nx
import matplotlib.pyplot as py

G = nx.karate_club_graph()
#G = nx.erdos_renyi_graph(30, 0.05)

#Best partition computing
part = community.best_partition(G)

#Plot the graph
getsize = float(len(set(part.values()))) 	#Find (un-duplicated nodes) length size of parition
position = nx.spring_layout(G)			#Position nodes using Fruchterman-Reingold force directed algorithm
temp = 0
for community in set(part.values()):
	temp = temp+1				#Color differentiation
	nodelist = [nodes for nodes in part.keys() if part[nodes] == community]	#Cycle through the keys(nodes) and generate the list of nodes belonging to a partition (Compare the value of partition to which a node belongs to best partition function result then assign & draw)
	nx.draw_networkx_nodes(G, position, nodelist, node_size=20, node_color = str(temp/getsize)) #print list of nodes found above
nx.draw_networkx_edges(G, position, alpha=0.4)	#print edges
py.show()

