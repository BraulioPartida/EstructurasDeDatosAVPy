from BloomFilter import BloomFilter
import random as rnd


def generaStrAzar(n):
    res = ""
    for i in range(n):
        res += chr(rnd.randint(65, 91))
    return res


datos = [generaStrAzar(5) for i in range(20)]
mitad = int(len(datos) / 2)
particion1 = datos[:mitad]
particion2 = datos[mitad:]
## revisamos que en efecto sean particiones
for elem in particion1:
    if elem in particion2:
        print("no es particion")

bloom = BloomFilter(m=80, k=10)

## insertar los datos
for elem in particion1:
    bloom.inserta(elem)

## preguntar por los datos que no metimos
fpcount = 0
for elem in particion2:
    if bloom.busca(elem):
        print(f"Encontre un bug con el elemento {elem}")
        fpcount += 1

print(f"al final tuve {fpcount} falsos positivos")
print(f"Mi porcentaje de falsos positivos es: {fpcount/len(particion2)}")
