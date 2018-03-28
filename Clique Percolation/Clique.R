Clique<-function(graph,k)
{
	cliq<-cliques(graph,min=k,max=k)
	#No of edges> 
	ed<-c()
	for(i in seq_along(cliq))
	{
		for(j in seq_along(cliq))
		{
			if(length(unique(c(cliq[[i]],cliq[[j]])))==k+1)	#Circle through two unique cliques and compare them to form community
			{
				ed<- c(ed,c(i,j))		#connect edges
			}
		}
	}
	#Graph creation
	cliq.graph<-make_empty_graph(n=length(cliq)) %>% add_edges(ed)	#Graph based on length and addition of edges
	cliq.graph<-simplify(cliq.graph)	#simplify the graph for graph creation and plotting
	V(cliq.graph)$name<-seq_len(vcount(cliq.graph))	#Assign names to node
 	
	composition<-decompose.graph(cliq.graph)	#Remove irregularities
	lapply(composition, function(x)	
	{
		unique(unlist(cliq[V(x)$name]))		#Using lapply, apply function x on composition to generate a list of unique vector x
	})
}

