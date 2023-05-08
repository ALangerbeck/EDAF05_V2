import sys

DEBUG = True

def dprint(text):
    if DEBUG:
        print(text)
    
class Edge:

    def __init__(self,capacity,node_a,node_b,edge_id):
        self.node_a = node_a
        self.node_b = node_b
        self.capacity = capacity
        self.edge_id = edge_id

class Node:
    
    def __init__(self,node_id) -> None:
        self.edges = []
        self.node_id = node_id
    
    def add_edge(self,edge_id):
        self.edges.append(edge_id)

class Graph:

    def __init__(self,n_nodes,n_edges,payload) -> None:
        self.edges = []
        self.nodes = []
        self.payload = payload
        
        for i in range(n_nodes):
            self.nodes.append(Node(i-1))

        self.n = n_nodes
        self.e = n_edges

    def add_edge(self,capacity,node_a,node_b):
        edge_id = len(self.edges)
        edge = Edge(capacity,node_a,node_b,edge_id)
        self.edges.append(edge)

        self.nodes[node_a].add_edge(edge_id)
        self.nodes[node_b].add_edge(edge_id)


        

def read_input():
    dprint("=== Reading Data ===")
    n_nodes,n_edges,payload,n_routes = sys.stdin.readline().strip().split(" ")
    
    graph = Graph(int(n_nodes),int(n_edges),int(payload))

    for lines in range(int(n_edges)):
        n1,n2,cap = sys.stdin.readline().strip().split(" ")
        graph.add_edge(int(cap),int(n1),int(n2))

    if DEBUG:
        for i in range(int(n_nodes)):
            print(f"Node {i} :  {graph.nodes[i].edges}")


def main():
    read_input()
    print("Not done with implementation")

if __name__ == "__main__":
    main()
