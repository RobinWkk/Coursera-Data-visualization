import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#--------------顶点----------------------
vertex = pd.read_table('football.txt')
v = vertex['label'].str.split(' ', expand = True)
v2 = v[3].str.split('"', expand = True)
VERTEX = list(v[2].astype('int'))
print(VERTEX)
#print(list(start))
#v3 = pd.merge(v[2], v2[1])
#---------------边----------------------
edges = pd.read_table('edges.txt')
e = edges['left'].str.split(' ', expand = True)
start = list(e[1].astype('int'))
to = list(e[2].astype('int'))
value = list(e[5].astype('int'))
#print(type(weight))
#print(start)
#print(to)
#print(value)
#------------------------Counting Hubs & Authorities----------------------------
# for i in range(1, 36):
# 	count = start.count(i)
# 	print(i, 'output times:', count)
#
# for i in range(1, 36):
# 	count = to.count(i)
# 	print(i, 'input times:', count)
#----------------------------------------------------------------------
G = nx.DiGraph()
for j in range(0, len(start)):
	G.add_weighted_edges_from([(start[j], to[j], value[j])])
#G.add_nodes_from(v2[2])
#zipped = list(zip(start, to, value))
#print(zipped)
#print(type(e[5]))
#G.add_weighted_edges_from(zipped)
#print(G.nodes())

print(G.edges())
print(G.number_of_edges())
#---------------------------------classifying vertex-----------------------------
hubs = ['NOR', 'DNK', 'ROM', 'ARG', 'YUG', 'HRV']
hubs_auth = ['SCO','NLD', 'AUT', 'BRA']
auth = ['TUR', 'FRA', 'GBR', 'DEU', 'ESP', 'ITA']
all3 = hubs + hubs_auth + auth
print('all3: ', all3)
others = [x for x in list(v2[1]) if x not in all3]
print('others: ', others)
#nx.draw_random
#nx.draw_circular
#nx.draw_random(G, with_labels=True, edge_color = 'b', node_color = 'g', node_size = 700)
#nx.draw(G,pos = nx.random_layout(G), node_color = 'g',edge_color = 'b',with_labels = True, font_size =18, node_size =700)
#nx.draw_networkx_nodes(G, pos = nx.shell_layout(G), nodelist = list(v2[2]), alpha = 0.4, node_color = 'blue', node_shape = 'p', node_size = 700)
#nx.draw_networkx_edges(G,pos=nx.shell_layout(G),edgelist= zipped,width=1,edge_color='b')
#nx.draw_networkx_labels(G,pos=nx.shell_layout(G),font_size=20,font_color='k',font_family='SimHei',alpha=1)
#nx.draw(G, with_labels=True,pos=nx.circular_layout(G), width=[weight for (r, c, v) in G.edges(data=True)])

countries = {k: v for k, v in zip(VERTEX, list(v2[1]))}
#print(type(countries))
G = nx.relabel_nodes(G, countries)
print('Nodes of the graph G:')
print(G.nodes())
print(G.edges())
overlap = False
splines = True
#----------------------顶点不分类------------------------------------
#nx.draw(G, with_labels=True, edge_color = 'b', node_color = 'y', node_size =700, pos=nx.random_layout(G), width= [float(value[w])/5 for w in value], alpha = 0.8)
#---------------------------------------------------------------------
pos=nx.random_layout(G)
scale = 1.5
nx.draw_networkx_edges(G,pos,edgelist=G.edges(), width= [float(value[w])/5 for w in value], edge_color='b')

nx.draw_networkx_nodes(G, pos,nodelist=hubs, alpha = 0.8,node_color='blue',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=auth,alpha = 0.8,node_color='red',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=hubs_auth,alpha = 0.8,node_color='g',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=others,alpha = 0.8,node_color='y',node_size=500)

nx.draw_networkx_labels(G,pos,font_size=14,font_color='k',font_family='SimHei',alpha=1)
plt.axis("off")

plt.savefig('graph_football.png')
plt.show()
#----------------------------放大图片-----------------------
from matplotlib import pylab
def save_graph(graph,file_name):
#initialze Figure
	plt.figure(num=None, figsize=(20, 20), dpi=80)
	plt.axis('off')
fig = plt.figure(1)
pos = nx.random_layout(G)

nx.draw_networkx_edges(G,pos,edgelist=G.edges(), alpha = 0.8, width= [float(value[w])/5 for w in value], edge_color='b')

nx.draw_networkx_nodes(G, pos,nodelist=hubs, alpha = 0.8,node_color='blue',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=auth,alpha = 0.8,node_color='red',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=hubs_auth,alpha = 0.8,node_color='g',node_size=600)
nx.draw_networkx_nodes(G, pos, nodelist=others,alpha = 0.8,node_color='y',node_size=500)

nx.draw_networkx_labels(G,pos,font_size=14,font_color='k',font_family='SimHei',alpha=1)
plt.axis("off")

cut = 1.00
xmax = cut * max(xx for xx, yy in pos.values())
ymax = cut * max(yy for xx, yy in pos.values())
plt.xlim(0, xmax)
plt.ylim(0, ymax)

plt.savefig("my_graph.pdf",bbox_inches="tight")
plt.savefig("my_graph.png",bbox_inches="tight")
pylab.close()
del fig

#Assuming that the graph g has nodes and edges entered
save_graph(G,"my_graph.pdf")
save_graph(G,"my_graph.png")

