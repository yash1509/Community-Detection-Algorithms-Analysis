try:import urllib.request as urllib
except ImportError: import urllib as ub
import io
import zipfile as zpf
import matplotlib.pyplot as plt
import networkx as nx

link = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

socket = ub.urlopen(link)  		# Get Link
inp = io.BytesIO(socket.read()) 	# Read file inByte
socket.close()

zf = zpf.ZipFile(inp)  			# Invoke object of zipfile
txt = zf.read('football.txt').decode()  # Text file input
gml = zf.read('football.gml').decode()  # Gml file input
gml = gml.split('\n')[1:]		# Erase first line of column names
G = nx.parse_gml(gml)  			# parse gml data

print(txt)

# print degree for each team - number of games
#for n, d in G.degree():
#    print('Degree of Team - %s Number Of Games %d' % (n, d))

setting = {'node_color': 'red','node_size': 60,'line_color': 'black','width': 0.1,}

nx.draw(G, **setting)
plt.show()
