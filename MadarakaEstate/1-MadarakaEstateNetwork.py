import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","J1","Mada","Phase3","ParkingLot"]
G.add_nodes_from(nodes)

#Adding the positions
G.nodes["SportsComplex"]['pos']=(-0.047857,0.043897)
G.nodes["Siwaka"]['pos']=(-0.04679,0.04389)
G.nodes["Ph.1A"]['pos']=(-0.04543,0.04395)
G.nodes["Ph.1B"]['pos']=(-0.04528,0.04269)
G.nodes["STC"]['pos']=(-0.04526,0.040781)
G.nodes["Phase2"]['pos']=(-0.044553,0.042706)
G.nodes["J1"]['pos']=(-0.043919,0.042688)
G.nodes["Mada"]['pos']=(-0.043103,0.042632)
G.nodes["Phase3"]['pos']=(-0.04416,0.04074)
G.nodes["ParkingLot"]['pos']=(-0.044157,0.039358)


G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="450m")
G.add_edge("Siwaka","Ph.1A",weight="10m")
G.add_edge("Ph.1A","Ph.1B",weight="100m")
G.add_edge("Siwaka","Ph.1B",weight="230m")
G.add_edge("Ph.1A","Mada",weight="850m")
G.add_edge("Ph.1B","Phase2",weight="112m")
G.add_edge("Ph.1B","STC",weight="50m")
G.add_edge("STC","Phase2",weight="50m")
G.add_edge("STC","ParkingLot",weight="250m")
G.add_edge("Phase2","J1",weight="600m")
G.add_edge("Phase2","Phase3",weight="500m")
G.add_edge("Mada","J1",weight="200m")
G.add_edge("Phase3","ParkingLot",weight="350m")
G.add_edge("Mada","ParkingLot",weight="700m")

node_pos = nx.get_node_attributes(G,'pos')
edge_col = ['darkturquoise' ]
node_col = ['darkturquoise']
arc_weight=nx.get_edge_attributes(G,'weight')

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=1000)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
plt.axis('off')
plt.show()
