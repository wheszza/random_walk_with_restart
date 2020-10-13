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
        i, j = edge[0], edge[1]

        has_i = self.__graph.has_vertex(i)
        has_j = self.__graph.has_vertex(j)

        self.__graph.add_vertex(i)
        self.__graph.add_vertex(j)
        self.__graph.add_edge(i, j)

        i = self.__graph.get_index(i)
        j = self.__graph.get_index(j)

        if not has_i and has_j:
            self.__n += 1
            c = self.__r * self.__P[:,j]
            r = np.zeros([1, self.__n])
            self.__P = np.c_[self.__P, c]
            self.__P = np.r_[self.__P, r]
            self.__P[-1][-1] = 1 - self.__r
        elif has_i and not has_j:
            self.__n += 1
            if self.__graph.has_neighbors(i):
                e = np.zeros([self.__n - 1,1])
                e[i][0] = 1
                z = 1 / (len(self.__graph.get_neighbors(i)) + 1) * (
                    e - (1 - self.__r) * self.__P[:, i]
                )
                r = self.__r / len(self.__graph.get_neighbors(i) + 1) * (
                    self.__P[i] / (1 - z[i][0])
                )
                c = np.zeros([self.__n, 1])
                self.__P += z * self.__P[i] / (1 - z[i][0])
                self.__P = np.r_[self.__P, r]
                self.__P = np.c_[self.__P, c]
                self.__P[-1][-1] = 1 - self.__r
            else:
                return 0
        elif has_i and has_j:
            return 0
        else:
            return 0

    def unit_delete(self, edge):
        #code here
        return 0