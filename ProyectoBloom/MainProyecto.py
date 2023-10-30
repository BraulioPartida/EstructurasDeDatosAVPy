import pandas as pd
from BloomFilter import BloomFilter
import matplotlib.pyplot as plt


def calcFalsoPosi(estan, noEstan, n: int, k: int, cantNoEstan: int) -> float:
    bloom = BloomFilter(n, k)
    focount = 0
    for idx, elem in estan:
        bloom.inserta(elem)
    for idx, elem in noEstan:
        if bloom.busca(elem):
            focount += 1
    return focount / cantNoEstan


def calcMinM(fPMAX: float, estan, noEstan, n: int, k: int) -> str:
    nMin = 1
    nMax = n * 3
    cantNoEstan = noEstan.size
    p = 0
    bandera = True
    while True:
        nMid = (nMin + nMax) // 2
        enumEstan = enumerate(estan["url"])
        enumNoTan = enumerate(noEstan["url"])
        fP = calcFalsoPosi(enumEstan, enumNoTan, nMid, k, cantNoEstan)
        print(f"m:{nMid}, falsoPositivo:{fP}")

        if fP <= fPMAX and fP >= fPMAX - 0.0001:
            return f"{nMid}, {fP}"
        elif p == nMid:
            return f"{nMid}, {fP}"

        if fP > fPMAX:
            nMin = nMid
        else:
            nMax = nMid

        p = nMid


df = pd.read_csv("ProyectoBloom/CSVs/data.csv")

df["malicious"] = df["type"].apply(lambda x: 1 if x != "benign" else 0)


datos_insertar = df[df["malicious"] == 1]
datos_revisar = df[df["malicious"] == 0]
datos_insertar.to_csv("ProyectoBloom/CSVs/insercionBF.csv", index=False)
datos_revisar.to_csv("ProyectoBloom/CSVs/revisarBF.csv", index=False)


d = {"k": [], "m": [], "fP": []}
for k in range(1, 60):
    resp = calcMinM(0.01, datos_insertar, datos_revisar, datos_revisar.size, k).split(
        ", "
    )
    d["k"].append(k)
    d["m"].append(resp[0])
    d["fP"].append(resp[1])

    print("\n")

datosResultantes = pd.DataFrame(d)
