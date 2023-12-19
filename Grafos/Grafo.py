import heapdict
import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def __initx__(self):
        self.G = {}

    def insertaDirigido(self, origen, destino, peso=None):
        if origen not in self.G:
            self.G[origen] = {}
        if destino not in self.G:
            self.G[destino] = {}
        self.G[origen][destino] = peso

    def inserta(self, v1, v2, peso=None):
        self.insertaDirigido(v1, v2, peso)
        self.insertaDirigido(v2, v1, peso)

    def depth_first_search(self) -> list:
        recorrido = []
        # creación de la lista de visitados
        visitados = {}
        for v in self.G:
            visitados[v] = False
        # primer for e if para conexidad
        for v in visitados:
            if not visitados[v]:
                # hago el recorrido DFS a partir de v
                self.__DFS(v, recorrido, visitados)
        return recorrido

    def __DFS(self, actual, recorrido: list, visitados: dict):
        # añado el nodo actual al recorrido y registro la visita
        recorrido.append(actual)
        visitados[actual] = True
        # reviso los nodos a los que v apunta
        for v in self.G[actual]:
            if not visitados[v]:
                self.__DFS(v, recorrido, visitados)
                # la llamada recursiva se detiene hasta que "actual" no apunta a nodos sin visitar

    def breadth_first_search(self) -> list:
        recorrido = []
        # creación de la lista de visitados
        visitados = {}
        for v in self.G:
            visitados[v] = False
        # primer for e if para conexidad
        for u in self.G:
            if not visitados[u]:  # comienza el recorrido BFS a partir de u
                # la cola es la propia lista "recorrido"
                recorrido.append(u)
                visitados[u] = True
                # recorro la "cola"
                for v in recorrido:
                    # reviso los nodos a los que v apunta
                    for w in self.G[v]:
                        if not visitados[w]:
                            # añado a la cola y registro la visita
                            recorrido.append(w)
                            visitados[w] = True
        return recorrido

    def minimum_spanning_tree(self, raiz) -> dict:
        # guardar vértices en el Minimum Spanning Tree e inicializar pesos
        mst = {}
        pesos = heapdict.heapdict()
        for v in self.G:
            mst[v] = None
            pesos[v] = float("inf")
        # se pone prioridad al nodo recibido por la función
        pesos[raiz] = 0
        while len(pesos) > 0:
            # tomo el nodo de mayor prioridad
            u, peso = pesos.popitem()
            # a cada nodo vecino a u, reviso la distancia(peso)
            for v in self.G[u]:
                # para los nodos aún no popeados, actualizo su peso
                if v in pesos and self.G[u][v] < pesos[v]:
                    pesos[v] = self.G[u][v]
                    # si se cumplió el if, la conexión más óptima de v es con u
                    mst[v] = u
        return mst

    def distancias_minimas_dijkstra(self, origen) -> dict:
        distMin = {}
        distancias = heapdict.heapdict()  # Instantiate an object of the heapdict class
        for v in self.G:
            distancias[v] = float("inf")
        distancias[origen] = 0
        while len(distancias) > 0:
            v, dist = distancias.popitem()
            distMin[v] = dist
            for u in self.G[v]:
                if u in distancias and distMin[v] + self.G[v][u] < distancias[u]:
                    distancias[u] = distMin[v] + self.G[v][u]
        return distMin

    def hayCaminoHamiltoniano(self) -> bool:
        for v in self.G:
            if self.__hayCaminoHamiltoniano(v, {v}):
                return True
        return False

    def __hayCaminoHamiltoniano(self, actual, visitados: set) -> bool:
        if len(visitados) == len(self.G):  # ya encontré el camino WIII
            return True
        for v in self.G[actual]:
            if v not in visitados:
                visitados.add(v)
                if self.__hayCaminoHamiltoniano(v, visitados):
                    return True
        visitados.remove(actual)
        return False

    def diametro(self) -> int:
        return max(self.__maxDist_a_Raiz(v) for v in self.G)

    def __maxDist_a_Raiz(self, raiz):
        dists_a_raiz = {raiz: 0}
        cola = [raiz]
        for actual in cola:
            for sig in self.G[actual]:
                if sig not in dists_a_raiz:
                    dists_a_raiz[sig] = dists_a_raiz[actual] + 1
                    cola.append(sig)
        return max(dists_a_raiz.values())

    def dibujaGrafo(self):
        G_nx = nx.DiGraph()
        for nodo, vecinos in self.G.items():
            for vecino, peso in vecinos.items():
                G_nx.add_edge(nodo, vecino, weight=peso)

        pos = nx.spring_layout(G_nx)
        nx.draw(G_nx, pos, with_labels=True, arrows=True)

        # Agrega etiquetas a las aristas
        edge_labels = {(u, v): w["weight"] for u, v, w in G_nx.edges(data=True)}
        nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels)

        plt.show()

    def flujoMax(self, inicio, final) -> float:
        gr = {v: self.G[v] for v in self.G}
        for v in gr:
            for u in gr[v]:
                if v not in gr[u]:
                    gr[u][v] = 0

        bfs = self.breadthSearch(gr, inicio, final)

        while final in bfs:
            camino = []
            pesoMin = float("inf")
            actual = final
            while actual != inicio:
                antes = bfs[actual]
                peso = gr[antes][actual]
                if peso < pesoMin:
                    pesoMin = peso

                camino.insert(0, actual)

                actual = antes
            actual = inicio

            for sig in camino:
                gr[actual][sig] -= pesoMin
                gr[sig][actual] += pesoMin
                actual = sig
            bfs = self.breadthSearch(gr, inicio, final)
        return sum(gr[final].values())

    def breadthSearch(self, gr: dict, inicio, final) -> dict:
        cola = [inicio]
        antBFS = {inicio: False}
        for v in cola:
            for u in gr[v]:
                if u not in antBFS and gr[v][u] > 0:
                    antBFS[u] = v
                    cola.append(u)
                    if u == final:
                        return antBFS
        return antBFS


G = Grafo()

G.insertaDirigido("a", "b", 4)
G.insertaDirigido("a", "h", 8)
G.insertaDirigido("b", "c", 8)
G.insertaDirigido("b", "g", 11)
G.insertaDirigido("h", "i", 7)
G.insertaDirigido("h", "g", 1)


G.dibujaGrafo()
print(G.flujoMax("a", "g"))

H = Grafo()
H.insertaDirigido("c", "f", 4)
H.insertaDirigido("c", "d", 7)
H.insertaDirigido("g", "f", 2)
H.insertaDirigido("d", "e", 9)
H.insertaDirigido("d", "f", 14)
H.insertaDirigido("f", "e", 10)

H.dibujaGrafo()
print(H.flujoMax("c", "e"))

I = Grafo()
I.insertaDirigido("S", "V1", 16)
I.insertaDirigido("S", "V2", 13)
I.insertaDirigido("V1", "V2", 10)
I.insertaDirigido("V1", "V3", 12)
I.insertaDirigido("V2", "V1", 4)
I.insertaDirigido("V2", "V4", 14)
I.insertaDirigido("V3", "V2", 9)
I.insertaDirigido("V3", "T", 20)
I.insertaDirigido("V4", "V3", 7)
I.insertaDirigido("V4", "T", 4)

I.dibujaGrafo()
print(I.flujoMax("S", "T"))
