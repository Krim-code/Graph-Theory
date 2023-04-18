from pprint import pprint

import pyfiglet

from GraphGenerator.Generator import Graph


class MaxConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * graph.vertices

    def del_useless_edges(self,max_components):
        base_dict = self.graph
        for i in self.graph.to_dict_without_weight().keys():
            if max_components.to_dict_without_weight().get(i) == []:
                base_dict.edges[i] = [0 for i in range(self.graph.vertices)]
        return base_dict



    def dfs(self, u, component):
        self.visited[u] = True
        component.add_edge(u, u)  # добавляем узел как ребро с самим собой
        for v in range(self.graph.vertices):
            if self.graph.edges[u][v] != 0 and not self.visited[v]:
                self.dfs(v, component)

    def get_max_connected_component(self):
        components = []
        for u in range(self.graph.vertices):
            if not self.visited[u]:
                component = Graph(self.graph.vertices)
                self.dfs(u, component)
                components.append(component)

        max_component = max(components, key=lambda x: x.vertices)

        return self.del_useless_edges(max_component)


if __name__ == '__main__':
    g = Graph(10)
    g.read_csv("graph.csv")
    pprint(g.to_dict_without_weight())
    g.draw()
    mcc = MaxConnectedComponent(g)
    max_component = mcc.get_max_connected_component()
    pprint(max_component.to_dict_without_weight())

    max_component.draw()
