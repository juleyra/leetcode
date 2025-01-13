from collections import defaultdict

class Graph:
    def __init__(self, vertices:list = None):
        self.adjacency_list = defaultdict(list)
        if vertices is not None:
            for v in vertices:
                self.add_vertex(v)


    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return
        self.adjacency_list.pop(vertex)
        for neighbors in self.adjacency_list.values():
            if vertex in neighbors:
                neighbors.remove(vertex)


    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].remove(vertex1)

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if vertex < neighbor:
                    edges.append((vertex, neighbor))
        return edges

# check
    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def is_adjacent(self, vertex1, vertex2):
        return vertex2 in self.adjacency_list[vertex1]

    def get_vertex_count(self):
        return len(self.adjacency_list)

    def get_edge_count(self):
        # why?
        # count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        # return count // 2
        return len(self.adjacency_list.values())

    def dfs(self, startVertex):
        visited = set()
        stack = []
        stack.append(startVertex)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)


# graph = Graph([1, 2, 3, 4, 5, 6])
# edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)]
# for edge in edges:
#     graph.add_edge(*edge)
# print(graph.adjacency_list)
# graph.dfs(1)


def func(x=[ ]):
 x.append(1)
 return x

print(func(), end= ' ')
print(func())
