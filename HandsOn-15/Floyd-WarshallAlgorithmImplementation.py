# Implementation of Floyd-Warshall algorithm

def floydwarshallImplementation(graph):
    # the number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix with the same weights
    initial_distances = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        initial_distances[i][i] = 0
        for j in graph[i]:
            initial_distances[i][j] = graph[i][j]

    # distances using all vertices as intermediate nodes
    for k in range(V):
        for i in range(V):
            for j in range(V):
                initial_distances[i][j] = min(initial_distances[i][j], initial_distances[i][k] + initial_distances[k][j])

    return initial_distances

# Example
graph = {
    0: {3: 1, 2: 7},
    1: {2: 5, 3: 8},
    2: {1: 4, 3: 2},
    3: {}
}

shortest_paths = floydwarshallImplementation(graph)

# Printing the results ofshortest paths
print("Shortest paths between all the pairs of vertices:")
for i in range(len(shortest_paths)):
    for j in range(len(shortest_paths[0])):
        print(f"Shortest path from vertex {i} to {j} is {shortest_paths[i][j]}")


'''
Output:
Shortest paths between all the pairs of vertices:
Shortest path from vertex 0 to 0 is 0
Shortest path from vertex 0 to 1 is 11
Shortest path from vertex 0 to 2 is 7
Shortest path from vertex 0 to 3 is 1
Shortest path from vertex 1 to 0 is inf
Shortest path from vertex 1 to 1 is 0
Shortest path from vertex 1 to 2 is 5
Shortest path from vertex 1 to 3 is 7
Shortest path from vertex 2 to 0 is inf
Shortest path from vertex 2 to 1 is 4
Shortest path from vertex 2 to 2 is 0
Shortest path from vertex 2 to 3 is 2
Shortest path from vertex 3 to 0 is inf
Shortest path from vertex 3 to 1 is inf
Shortest path from vertex 3 to 2 is inf
Shortest path from vertex 3 to 3 is 0
'''        