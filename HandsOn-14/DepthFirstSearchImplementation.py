# Implementation of Depth First Search algorithm

from collections import defaultdict

class DepthFirstSearchGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge_to_graph(self, u, v):
        self.graph[u].append(v)

    def dfs_visited_nodes(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_visited_nodes(i, visited)

    def dfs_implementation(self, start):
        visited = defaultdict(bool)
        self.dfs_visited_nodes(start, visited)

# Example usage
g = DepthFirstSearchGraph()
g.add_edge_to_graph('m', 'x')
g.add_edge_to_graph('m', 'r')
g.add_edge_to_graph('m', 'q')
g.add_edge_to_graph('n', 'q')
g.add_edge_to_graph('q', 't')
g.add_edge_to_graph('n', 'u')
g.add_edge_to_graph('u', 't')
g.add_edge_to_graph('n', 'o')
g.add_edge_to_graph('o', 'r')
g.add_edge_to_graph('r', 'y')
g.add_edge_to_graph('y', 'v')
g.add_edge_to_graph('o', 'v')
g.add_edge_to_graph('o', 's')
g.add_edge_to_graph('p', 'o')
g.add_edge_to_graph('p', 's')
g.add_edge_to_graph('p', 'z')
g.add_edge_to_graph('v', 'w')
g.add_edge_to_graph('w', 'z')

print("The Depth First Search starting from the vertex 'p':")
g.dfs_implementation('p')

'''
Output:
The Depth First Search starting from the vertex 'p':
p o r y v w z s 

'''