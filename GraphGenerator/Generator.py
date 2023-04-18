import csv
import random


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for i in range(vertices)] for j in range(vertices)]

    def add_edge(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 1

    def add_edges(self, edges):
        for u, v in edges:
            self.add_edge(u, v)

    def randomize(self, density):
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if random.random() < density:
                    self.add_edge(i, j)

    def write(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(self.vertices):
                for j in range(i + 1, self.vertices):
                    if self.edges[i][j] == 1:
                        writer.writerow([i, j])

    def __str__(self):
        result = ""
        for i in range(self.vertices):
            result += f"{i}: "
            for j in range(self.vertices):
                if self.edges[i][j] == 1:
                    result += f"{j} "
            result += "\n"
        return result


# Example usage
g = Graph(10)
# g.add_edges([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

g.randomize(0.5)
g.write("example.csv")
print(g)
# print(g.edges)
