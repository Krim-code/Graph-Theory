from pprint import pprint

import pyfiglet

from GraphGenerator.Generator import Graph

class DFS:

    def __init__(self, graph, node):
        self.graph = graph
        self.node = node
        self.visited = set()
        self.visit(self.node)

    def visit(self, node):
        if node not in self.visited:
            print(node)
            self.visited.add(node)
            for neighbour in self.graph[node]:
                self.visit(neighbour)


class BFS:
    def __init__(self, graph, node):
        self.visited = list()
        self.queue = []
        self.graph = graph
        self.node = node

        self.visit(self.node)

    def visit(self,node):
        self.visited.append(node)
        self.queue.append(node)

        while self.queue:
            m = self.queue.pop(0)
            print(m, end="\n")

            for neighbour in self.graph[m]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)


if __name__ == '__main__':
    G = Graph(10)
    G.randomize(0.3,False)
    pprint(G.to_dict_without_weight())

    print(pyfiglet.figlet_format("DFS", font = "digital" ))
    DFS = DFS(G.to_dict_without_weight(), 0)

    print(pyfiglet.figlet_format("BFS", font = "digital" ))
    BFS = BFS(G.to_dict_without_weight(),0)

    G.draw()