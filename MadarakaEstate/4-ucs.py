from collections import defaultdict
from queue import PriorityQueue  
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, directed): 
        """Parametrized constructor of class Graph 
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with weight as Algorithm is of UCS"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Uniform Cost Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                visited.append(current_node)
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))
        return visited
       
g = Graph(False)


g.graph =  defaultdict(list)
g.add_edge("Sports Complex","Siwaka",weight="450")
g.add_edge("Siwaka","Phase 1A",weight="10")
g.add_edge("Siwaka","Phase 1B",weight="230")
g.add_edge("Phase 1A","Phase 1B",weight="100")
g.add_edge("Phase 1B","Phase 2",weight="112")
g.add_edge("Phase 1B","STC",weight="50")
g.add_edge("Phase 2","J1",weight="600")
g.add_edge("J1","Madaraka",weight="200")
g.add_edge("Phase 2","Phase 3",weight="500")
g.add_edge("Phase 2","STC",weight="50")
g.add_edge("Phase 3","Parking Lot",weight="350")
g.add_edge("STC","Parking Lot",weight="250")
g.add_edge("Madaraka","Parking Lot",weight="700")


g.graph
#g.ucs('Sports Complex', 'Parking Lot')


G = nx.Graph()
nodes=["Sports Complex","Siwaka", "Phase 1A", "Phase 1B", "Phase 2", "STC", "J1", "Madaraka", "Phase 3", "Parking Lot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights

G.add_edge("Sports Complex","Siwaka",weight="450")
G.add_edge("Siwaka","Phase 1A",weight="10")
G.add_edge("Siwaka","Phase 1B",weight="230")
G.add_edge("Phase 1A","Phase 1B",weight="100")
G.add_edge("Phase 1B","Phase 2",weight="112")
G.add_edge("Phase 1B","STC",weight="50")
G.add_edge("Phase 2","J1",weight="600")
G.add_edge("J1","Madaraka",weight="200")
G.add_edge("Phase 2","Phase 3",weight="500")
G.add_edge("Phase 2","STC",weight="50")
G.add_edge("Phase 3","Parking Lot",weight="350")
G.add_edge("STC","Parking Lot",weight="250")
G.add_edge("Madaraka","Parking Lot",weight="700")


#position the nodes to resemble Nairobis map
G.nodes["Sports Complex"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(4,0)
G.nodes["Phase 1A"]['pos']=(6,0)
G.nodes["Phase 1B"]['pos']=(6,-4)
G.nodes["Phase 2"]['pos']=(8,-4)
G.nodes["STC"]['pos']=(6,-6)
G.nodes["J1"]['pos']=(10,-4)
G.nodes["Madaraka"]['pos']=(12,-4)
G.nodes["Phase 3"]['pos']=(10,-6)
G.nodes["Parking Lot"]['pos']=(10,-8)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')

route_list = g.ucs('Sports Complex', 'Parking Lot')
print(route_list)

#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()


