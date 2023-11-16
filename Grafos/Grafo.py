import numpy as np


class grafo:
    def __init__(self):
        self.G = {}

    def insertaD(self, v1, v2, w=0):
        if v1 not in self.G:
            self.G[v1] = {}
        self.G[v1][v2] = w
        if v2 not in self.G:
            self.G[v2] = {}

    def inserta(self, v1, v2, w=0):
        self.insertaD(v1, v2, w)
        self.insertaD(v2, v1, w)

    def callDFS(self):
        visitado = {}
        for i in self.G.keys():
            visitado[i] = False
        l = []
        for j in visitado:
            if not visitado[j]:
                self.__DFS(j, l, visitado)
        return l

    def __DFS(self, v, l, visitado):
        if visitado[v]:
            return
        visitado[v] = True
        l.append(v)
        for u in self.G[v]:
            self.__DFS(u, l, visitado)

    def callBFS(self):
        visitado = {}
        for i in self.G.keys():
            visitado[i] = False
        l = []
        for j in visitado:
            if not visitado[j]:
                self.__BFS(j, l, visitado)
        return l

    def __BFS(self, v, lista, visitados):
        visitados = {v: True}
        cola = [v]
        while len(cola) != 0:
            dato = cola.pop(0)
            lista.append(dato)
            for u in self.G[dato]:
                if u not in visitados:
                    visitados[u] = True
                    cola.append(u)
