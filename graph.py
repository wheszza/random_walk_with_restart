from typing import List

class Graph():
    def __init__(self):
        self.__graph = []
        self.__vertices = []
        self.__map = {}
        self.__has_out_edges = []
        self.__number_vertices = 0

    def add_vertex(self, vertex: int) :
        try:
            self.__map[vertex]
        except KeyError:
            self.__map[vertex] = self.__number_vertices
            self.__vertices.append(vertex)
            self.__graph.append([])
            self.__has_out_edges.append(False)
            self.__number_vertices += 1

    def add_edge(self, source : int, destination : int) :
        self.__graph[self.__map[source]].append(self.__map[destination])
        self.__has_out_edges[self.__map[source]] = True

    def get_number_vertices(self) -> int:
        return self.__number_vertices

    def get_vertex(self, index : int) -> int: 
        return self.__vertices[index]

    def get_index(self, vertex : int) -> int:
        return self.__map[vertex]

    def get_neighbors(self, index : int) -> List[int]:
        return self.__graph[index]

    def has_neighbors(self, index : int) -> bool:
        return self.__has_out_edges[index]

    def has_vertex(self, vertex : int) -> bool:
        try:
            self.__map[vertex]
        except KeyError:
            return False 
        return True

    def print_graph(self, filename):
        output = open(filename, "a")
        output.seek(0)
        output.truncate()

        for first in range(len(self.__graph)):
            source = self.__vertices[first]
            for second in self.__graph[first]:
                destination = self.__vertices[second]
                output.write(str(source) + "\t" + str(destination) + "\n")