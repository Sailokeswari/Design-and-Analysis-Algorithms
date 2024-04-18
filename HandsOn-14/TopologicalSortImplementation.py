# Implementation of Topological Sort Algorithm

from collections import defaultdict

class TopologicalSortGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge_to_graph(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def topological_sort_stack(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_stack(i, visited, stack)

        stack.append(v)

    def topological_sort_implementation(self):
        visited = {}
        stack = []

        for vertex in self.graph.keys():
            visited[vertex] = False

        for vertex in self.graph.keys():
            if not visited[vertex]:
                self.topological_sort_stack(vertex, visited, stack)

        return stack[::-1]

# Example usage
g = TopologicalSortGraph()
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

print("The Topological Sort for given vertices are:", g.topological_sort_implementation())

'''
Output:
The Topological Sort for given vertices are: 
['p', 'n', 'o', 's', 'u', 'm', 'q', 't', 'r', 'y', 'v', 'w', 'z', 'x']

'''