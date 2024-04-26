# Implementation of Bellman-Ford algorithm

class GraphEdge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def bellmanordfordImplementation(edges, V, start):
    # Initialize distances from start vertex to all other vertices
    initial_distances = [float("inf")] * V
    initial_distances[start] = 0

    # Choose a simple shortest path from start to any other vertex
    for _ in range(V - 1):
        for edge in edges:
            if initial_distances[edge.u] + edge.weight < initial_distances[edge.v]:
                initial_distances[edge.v] = initial_distances[edge.u] + edge.weight
    for edge in edges:
        if initial_distances[edge.u] + edge.weight < initial_distances[edge.v]:
            print("Graph contains negative weight cycle")
            return None

    return initial_distances

# Example
edges = [
    GraphEdge(2, 1, 1),
    GraphEdge(0, -2, 4),
    GraphEdge(-1, 2, -2),
    GraphEdge(2, -3, 1),
    GraphEdge(4, 4, -2),
    GraphEdge(3, 2, 2),
    GraphEdge(3, 2, 1),
    GraphEdge(4, 2, 2)
]
V = 5  # Number of vertices in the graph
start = 0  # Starting node

distances = bellmanordfordImplementation(edges, V, start)
if distances:
    print("Vertex Distance from Source vertex")
    for i in range(V):
        print(f"{i}\t\t{distances[i]}")


'''
Output:
Vertex Distance from Source vertex
0               0
1               6
2               5
3               4
4               inf

'''        