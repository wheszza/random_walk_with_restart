import graph
import re

class Parser():
    def __init__(self, filename):
        self.__graph = graph.Graph()
        self.__inputfile = filename
        self.__parse_graph()

    def get_graph(self):
        return self.__graph
        
    def __parse_graph(self):
        ms = open(self.__inputfile)

        for line in ms.readlines():
            edge = re.findall(r"\d+\.?\d*", line)
            self.__graph.add_vertex(int(edge[0]))
            self.__graph.add_vertex(int(edge[1]))
            self.__graph.add_edge(int(edge[0]),int(edge[1]))