from pprint import pprint

from GraphGenerator.Generator import Graph


class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        self.parent = list(range(graph.vertices))
        self.rank = [0] * graph.vertices

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

    def get_minimum_spanning_tree(self):
        edges = []
        for u in range(self.graph.vertices):
            for v in range(u + 1, self.graph.vertices):
                if self.graph.edges[u][v] != 0:
                    edges.append((u, v, self.graph.edges[u][v]))
        edges.sort(key=lambda x: x[2])
        result = Graph(self.graph.vertices)
        for u, v, weight in edges:
            if self.union(u, v):
                result.add_weighted_edge(u, v, weight)
        return result


g = Graph(7)
g.randomize(0.5, True)
g.read_csv("graph.csv")
g.draw()
print("Importing graph", end="\n")
pprint(g.to_dict_with_weight())

print("Output:", end="\n")
kruskal = Kruskal(g)
mst = kruskal.get_minimum_spanning_tree()
pprint(mst.to_dict_without_weight())
mst.draw()
