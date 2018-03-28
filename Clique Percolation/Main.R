library(igraph)
library(magrittr)
source("Clique.R")

graph <- make_graph("Zachary")
result <-Clique(g,3)

## Various Community coloring
colors<-rainbow(length(result)+1)
for(i in seq(along=result)){
	V(graph)[ result[[i]] ]$color<-colors[i+1]
}

## Vertices found in Multiple communities changed to red
V(graph)[unlist(result)[ duplicated(unlist(result)) ] ]$color <- "red"

#plot
plot(graph,layout=layout_with_fr,vertex.label=V(graph)$name)

