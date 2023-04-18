import csv
import random
import networkx as nx
import matplotlib.pyplot as plt
import pyfiglet
from rich import print


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for i in range(vertices)] for j in range(vertices)]

    def add_edge(self, u, v):
        self.add_weighted_edge(u, v, 1)

    def add_weighted_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def add_edges(self, edges):
        for u, v in edges:
            self.add_edge(u, v)

    def remove_edge(self, u, v):
        self.edges[u][v] = 0
        self.edges[v][u] = 0

    def randomize(self, density, weight_check):
        max_edges = self.vertices * (self.vertices - 1) // 2
        num_edges = int(density * max_edges)
        for i in range(num_edges):
            u = random.randint(0, self.vertices - 1)
            v = random.randint(0, self.vertices - 1)
            while u == v or self.edges[u][v] != 0:
                u = random.randint(0, self.vertices - 1)
                v = random.randint(0, self.vertices - 1)
            if weight_check:
                weight = random.randint(1, 10)
            else:
                weight = 1
            self.add_weighted_edge(u, v, weight)

    def write(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(self.vertices):
                for j in range(i + 1, self.vertices):
                    if self.edges[i][j] != 0:
                        writer.writerow([i, j, self.edges[i][j]])

    def to_dict_with_weight(self):
        result = {}
        for i in range(self.vertices):
            result[i] = []
            for j in range(self.vertices):
                if self.edges[i][j] != 0:
                    result[i].append((j, self.edges[i][j]))
        return result

    def to_dict_without_weight(self):
        result = {}
        for i in range(self.vertices):
            result[i] = []
            for j in range(self.vertices):
                if self.edges[i][j] != 0:
                    result[i].append(j)
        return result

    def read_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                u, v, weight = map(int, row)
                self.add_weighted_edge(u, v, weight)

    def draw(self):
        G = nx.Graph()
        for i in range(self.vertices):
            G.add_node(i)
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.edges[i][j] != 0:
                    G.add_edge(i, j, weight=self.edges[i][j])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def __str__(self):
        result = ""
        for i in range(self.vertices):
            result += f"{i}: "
            for j in range(self.vertices):
                if self.edges[i][j] == 1:
                    result += f"{j} "
            result += "\n"
        return result


if __name__ == '__main__':
    # Example usage
    g = Graph(10)
    g.read_csv("graph.csv")
    g.randomize(0.5, False)

    print(pyfiglet.figlet_format("Generating Graph Table", font="digital"))
    print(g)

    print(pyfiglet.figlet_format("Dict With Weight", font="digital"))
    print(g.to_dict_with_weight())

    print(pyfiglet.figlet_format("Dict Without Weight", font="digital"))
    print(g.to_dict_without_weight())
    g.draw()
