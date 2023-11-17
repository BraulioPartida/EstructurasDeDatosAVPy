from NodoTrie import NodoTrie


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()
        self.cont = 0

    def inserta(self, palabra):
        actual = self.raiz
        for letra in palabra:
            if letra in actual.hijos.keys():
                actual = actual.hijos[letra]
            else:
                actual.hijos[letra] = NodoTrie()
                actual = actual.hijos[letra]
        actual.fin = True
        self.cont += 1

    def busca(self, palabra):
        actual = self.raiz
        flag = True
        for letra in palabra:
            if letra in actual.hijos.keys():
                actual = actual.hijos[letra]
            else:
                flag = False
        return actual.fin and flag

    def buscaR(self, actual, palabra):
        if len(palabra) == 0:
            return actual.fin
        sig = palabra[0]
        if sig not in actual.hijos.keys():
            return False
        return self.buscaR(actual.hijos[sig], palabra[1:])

    def borra(self, palabra):
        return self.borraR(self.raiz, palabra)

    def borraR(self, actual, palabra):
        if len(palabra) == 0:
            actual.fin = False
            if len(actual.hijos.keys()) == 0:
                return True
            else:
                return False
        sig = palabra[0]
        if sig not in actual.hijos.keys():
            return False
        resp = self.buscaR(actual.hijos[sig], palabra[1:])
        if resp == True:
            actual.hijos.pop(sig)
            if len(actual.hijos.keys()) == 0 and actual.fin == False:
                return True
            else:
                return False
        else:
            return False

    def printTrie(self, actual=None, palabra=""):
        if actual is None:
            actual = self.raiz
        if actual.fin:
            print(palabra)
        for letra, nodo in sorted(actual.hijos.items()):
            self.printTrie(nodo, palabra + letra)

    def insertFromFile(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                for word in line.split():
                    self.inserta(word.lower())


trie = Trie()
trie.insertFromFile("texto.txt")
trie.printTrie()
