import sys
import queue

DEBUG = False

def dprint(text):
    if DEBUG:
        print(text)
    
class Edge:

    def __init__(self,capacity,node_a,node_b,edge_id):
        self.node_a = node_a
        self.node_b = node_b
        self.capacity = capacity
        self.edge_id = edge_id
        self.flow = 0
        self.residual_edge = None
    
    def other_node(self,node):
        if node.node_id == self.node_a.node_id:
            return self.node_b
        elif node.node_id == self.node_b.node_id:
            return self.node_a
        print(f"Node {node.node_id} does not belong to edge {self.edge_id}")

            

class Node:
    
    def __init__(self,node_id) -> None:
        self.edges = []
        self.node_id = node_id

        self.path_parent = None
        self.visited = None
    
    def add_edge(self,edge):
        self.edges.append(edge)


class Graph:

    def __init__(self,n_nodes,n_edges) -> None:
        self.edges = []
        self.nodes = []
        self.sink = n_nodes-1
        for i in range(n_nodes):
            self.nodes.append(Node(i))

        self.n = n_nodes
        self.e = n_edges
    
    def get_sink(self):
        return self.nodes[self.sink]
    
    def get_source(self):
        return self.nodes[0]

    def add_edge(self,capacity,node_a,node_b):
        edge_id = len(self.edges)
        edge_ab = Edge(capacity,node_a,node_b,edge_id)
        edge_ba = Edge(capacity,node_b,node_a,edge_id)
        edge_ab.residual_edge = edge_ba
        edge_ba.residual_edge = edge_ab
        self.edges.append(edge_ab)

        node_a.add_edge(edge_ab)
        node_b.add_edge(edge_ba)
        
    def get_edge(self,node_a,node_b):
        for edge in node_a.edges:
            if edge.node_b == node_b:
                return edge
            

    def reset_nodes(self):
        for n in self.nodes:
            n.path_parent = None
            n.visited = False
        
    def remove_edge(self,edge_id):
        edge = self.edges[edge_id]
        node_a = edge.node_a
        node_b = edge.node_b
        edge.node_a.edges.remove(edge)
        edgeb = self.get_edge(node_b,node_a)
        edge.node_b.edges.remove(edgeb)

def read_input():
    dprint("=== Reading Data ===")
    n_nodes,n_edges,payload,n_routes = sys.stdin.readline().strip().split(" ")
    
    graph = Graph(int(n_nodes),int(n_edges))

    for lines in range(int(n_edges)):
        n1,n2,cap = sys.stdin.readline().strip().split(" ")
        graph.add_edge(int(cap),graph.nodes[int(n1)],graph.nodes[int(n2)])
    
    remove_list = []
    for lines in range(int(n_routes)):
        remove_list.append(int(sys.stdin.readline().strip()))

    
    if DEBUG:
        for i in range(int(n_nodes)):
            print(f"Node {i} : ",end="")
            for edge in graph.edges:
                print(f"{edge.edge_id} ",end="")
            print("")

    return graph,remove_list,int(payload)

def bfs(g:Graph):
    dprint("Start bfs")
    g.reset_nodes()
    g.get_source().visited = True
    q = queue.SimpleQueue()
    q.put(g.get_source()) #Put source in the queue
    while not(q.empty()):
        u = q.get()
        dprint(f"Handling node {u.node_id}")

        for edge in u.edges:
            #dprint("New Edge")
            v = edge.node_b
            remaining_capacity = edge.capacity - edge.flow
            if v.visited or remaining_capacity <= 0:
                continue
            v.visited = True
            q.put(v)
            v.path_parent = u

            if v == g.get_sink():
                return v
    return False

def ff(g:Graph):
    dprint("Start FF")
    path_node = bfs(g)
    while path_node != False:
        dprint("New iteration of ff")
        #Adjust the flow of the path 
        path = []
        while path_node.node_id != 0:
            path.append(g.get_edge(path_node.path_parent,path_node,))
            path_node = path_node.path_parent
        #print path
        delta = float('inf')
        for edge in path:
            remaining_capacity = edge.capacity - edge.flow
            if remaining_capacity < delta:
                delta = remaining_capacity
        for edge in path:
            edge.flow += delta
        path_node = bfs(g)

    #for edge in path:
        #print(f" {edge.edge_id} <- " ,end="")
    maximum_payload = 0
    for edge in g.get_source().edges:
        maximum_payload += edge.flow
    return maximum_payload

def main():
    graph,remove_list,capacity = read_input()

    for edge_id in remove_list:
        graph.remove_edge(edge_id)
    
    maxflow = ff(graph)

    count = len(remove_list) - 1
    while(maxflow < capacity):
        dprint(f"Addin edge {remove_list[count]}")
        removed_edge_id = remove_list[count]
        edge = graph.edges[removed_edge_id]
        edge.node_a.add_edge(edge)
        edge.node_b.add_edge(edge.residual_edge)
        maxflow = ff(graph)
        count -= 1

        #dprint(f"Removing {graph.edges[removed_routes].edge_id}")
        #graph.remove_edge(remove_list[removed_routes])
        #new_maxflow = ff(graph)
        #dprint(f"new maxflow has been calculated to {new_maxflow}")
        #if new_maxflow < capacity:
        #    break 
        #removed_routes += 1
        #maxflow = new_maxflow
        #if removed_routes >= len(remove_list):
        #    break

    print(f"{count+1} {maxflow}")
        


if __name__ == "__main__":
    main()
