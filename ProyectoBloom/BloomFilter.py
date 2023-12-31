import numpy as np
import hashlib as hl
import random as rnd
import pandas as pd
import math as mth


class BloomFilter:
    def __init__(self, m, k):
        # en realidad estas tres líneas de código son una "funcion"
        # de cuantos veces haremos la llamada a md5 y cuantos cachos tomamos de el
        self.bits = mth.ceil(mth.log(m, 2))
        # cuantos cachos de caracteres voy a tomar del objeto
        self.caracteres_hexa = mth.ceil(self.bits / 4)
        # cuantos procesos voy a hacer, dividimos entre 32
        # porque ese es el tamaño de hl.md5().hexdigest()
        # la complejidad de insertar: O(procesosMD5) en realidad es O(k)
        self.procesosMD5 = mth.ceil(k * self.caracteres_hexa / 32)
        self.m = m
        self.k = k
        self.bloom = np.zeros(m, dtype=bool)

    def calculaKposiciones(self, objeto: str):
        # Regresa k posiciones para poner en True en el bloom
        posiciones = []
        hash = ""

        # al hacer este for estoy repitiendo mi string
        # digamos que mi resultado de hl.md5(cadena2.encode('utf-8')).hexdigest()
        # es: 1983adf (no es real porque en realidad es de tamaño 32)
        # despues de esto mi hash seria 1983adf1983adf...1983adf
        for procesos in range(self.procesosMD5):
            cadena2 = objeto + str(procesos)
            # la funcion hl.md5() necesita recibir el string encoded
            # luego regresa un objeto al que podemso aplicar hexdigest
            hexa = hl.md5(cadena2.encode("utf-8")).hexdigest()
            hash += hexa

        ## k * caracteres_hexa me dice cuantos caracteres voy a tomar
        ## la manera en la que iteramos es sobre bloques caracteres_hexa
        ## hace sentido porque k * caracteres_hexa/caracteres_hexa = k
        for i in range(0, self.k * self.caracteres_hexa, self.caracteres_hexa):
            # int(hexa, 16) tiene que tener modulo m para que quepa en el arreglo
            valor = int(hash[i : i + self.caracteres_hexa], 16) % self.m
            posiciones.append(valor)

        return posiciones

    def inserta(self, objeto: str):
        posiciones = self.calculaKposiciones(objeto)

        for pos in posiciones:
            self.bloom[pos] = True

    def busca(self, objeto: str):
        posiciones = self.calculaKposiciones(objeto)
        i = 0
        found = True
        while i < len(posiciones) and found:
            found = self.bloom[posiciones[i]]
            i += 1

        return found
