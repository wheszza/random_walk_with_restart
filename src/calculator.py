import numpy as np
import graph

class Calculator():
    def __init__(self, graph):
        self.__graph = graph
        self.__n = graph.get_number_vertices()
        self.__A = np.zeros([self.__n, self.__n])
        self.__P = np.zeros([self.__n, self.__n])
        self.__r = 0.9
        self.__calculate_A()
        self.__calculate_P()

    def __calculate_A(self):
        for j in range(self.__n):
            for i in self.__graph.get_neighbors(j):
                self.__A[i][j] = 1 / len(self.__graph.get_neighbors(j))

    def __calculate_P(self):
        I = np.identity(self.__n)
        self.__P = (1 - self.__r) * np.linalg.inv(I - self.__r * self.__A)

    def save_P(self, outfile):
        np.savetxt(outfile, self.__P, fmt='%f', delimiter=' ')
    
    def unit_insert(self, edge):
        #code here
        return 0

    def unit_delete(self, edge):
        #code here
        return 0