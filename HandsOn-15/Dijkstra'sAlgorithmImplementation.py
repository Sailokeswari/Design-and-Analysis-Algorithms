# Implementation of Dijkstra's algorithm

import heapq

def dijkstraAlgorithmImp(graph, start):
    # Initialize distances from start vertex to all other vertices
    initial_distances = {node: float('inf') for node in graph}
    initial_distances[start] = 0

    # Priority queue to store the vertices going to get visited next
    pq = [(0, start)]

    while pq:
        # Delet the vertex of the smallest distance from start
        current_distance, current_vertex = heapq.heappop(pq)

        # Visit each neighbor vertex from the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < initial_distances[neighbor]:
                initial_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return initial_distances

# Example
graph = {
    'A': {'B': 4, 'C': 5},
    'B': {'A': 9, 'C': 1, 'D': 4},
    'C': {'A': 8, 'B': 2, 'D': 6},
    'D': {'B': 7, 'C': 10},


}

start_node = 'A'
shortest_distances = dijkstraAlgorithmImp(graph, start_node)
print("Shortest distances from the source node", start_node)
for node, distance in shortest_distances.items():
    print(f"Node is{node}: Distance is {distance}")


'''
# Output:
Shortest distances from the source node A
Node isA: Distance is 0
Node isB: Distance is 4
Node isC: Distance is 5
Node isD: Distance is 8

'''    