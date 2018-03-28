from random import choice
from collections import Counter
from copy import deepcopy

graph={} 

def MinimumCut(graph):
	while len(graph)>2:
		random_vertex = choice(graph.keys())		#Choose Random vertex 
		temp=graph[random_vertex]	
		#print temp
		vertex=temp.most_common(1)[0][0]
		spvertex=graph[vertex] 				#Most common vertex
		#print spvertex		
		del graph[vertex]				#delete vertex to show property of merging
		del spvertex[random_vertex]			#delete self loops
		del temp[vertex] 				#delete self loops
		temp.update(spvertex)				#Merge second and first vertex
		for i in spvertex:
			vertexi=graph[i]
			vertexi[random_vertex] += vertexi[vertex]
			del vertexi[vertex]
	return graph.itervalues().next().most_common(1)[0][1]

with open('input2.txt','r') as graphInput:
	for line in graphInput:
		val = [int(x) for x in line.split()]
		graph[val[0]] = Counter(val[1:])

res = [MinimumCut(deepcopy(graph)) for x in range(100)]
print min(res), res

