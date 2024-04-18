# Implementation of Kruskal Algorithm

class KruskalAlgorithmGraph:
    def __init__(self):
        self.graph = []

    def add_edge_to_graph(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent_node(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent_node(parent, parent[i])

    def union_nodes(self, parent, rank, x, y):
        x_root = self.find_parent_node(parent, x)
        y_root = self.find_parent_node(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst_Implementation(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = {}
        rank = {}

        for edge in self.graph:
            u, v, w = edge
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0

        while e < len(parent) - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent_node(parent, u)
            y = self.find_parent_node(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union_nodes(parent, rank, x, y)

        return result

# Example usage
g = KruskalAlgorithmGraph()
g.add_edge_to_graph('C', 'E', 12)
g.add_edge_to_graph('C', 'B', 8)
g.add_edge_to_graph('A', 'D', 4)
g.add_edge_to_graph('B', 'F', 25)
g.add_edge_to_graph('C', 'D', 8)
g.add_edge_to_graph('D', 'A', 2)
g.add_edge_to_graph('F', 'B', 16)
g.add_edge_to_graph('F', 'G', 20)
g.add_edge_to_graph('A', 'F', 3)
g.add_edge_to_graph('G', 'B', 15)
g.add_edge_to_graph('B', 'D', 9)

print("Edges in the minimum spanning tree using Kruskal Algorithm:")
print(g.kruskal_mst_Implementation())

'''
Output:
Edges in the minimum spanning tree using Kruskal Algorithm:
[['D', 'A', 2], ['A', 'F', 3], ['C', 'B', 8], ['C', 'D', 8], ['C', 'E', 12], ['G', 'B', 15]]

'''