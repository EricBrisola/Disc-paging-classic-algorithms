import random
import matplotlib.pyplot as plt

numPaginas = int(input("Insira a quantidade de paginas aleatorias desejadas : "))
tamanhoQuadro = int(input("insira o tamanho do quadro inicial: "))
tamanhoQuadroFinal = int(input("insira o tamanho do quadro final: "))
paginas = [random.randint(0, 7) for i in range(numPaginas)]


def fifo(paginas, tamanhoQuadro):
    faltaDePaginas = 0
    quadros = []
    pos = 0
    for pagina in paginas:
        if (pagina not in quadros):
            faltaDePaginas += 1
            if (len(quadros) < tamanhoQuadro):
                quadros.append(pagina)
            else:
                if (pos >= tamanhoQuadro):
                    pos = 0
                else:
                    quadros[pos] = pagina
                    pos = (pos + 1) % tamanhoQuadro

    #print("Quadros finais FIFO:", quadros)
    return faltaDePaginas


def secondChance(paginas, tamanhoQuadro):
    faltaDePaginas = 0
    quadros = []
    pos = 0
    bitsReferencia = []
    print(tamanhoQuadro)

    for n in range(tamanhoQuadro):
        bitsReferencia.append(1)
    print(bitsReferencia)

    for pagina in paginas:
        if (pagina not in quadros):
            faltaDePaginas += 1
            if (len(quadros) < tamanhoQuadro):
                quadros.append(pagina)
            else:
                if (pos >= tamanhoQuadro):
                    pos = 0
                else:
                    if(bitsReferencia[pos] == 1):
                        bitsReferencia[pos] = 0
                    else:
                        quadros[pos] = pagina
                        pos = (pos + 1) % tamanhoQuadro
        else:
            bitsReferencia[quadros.index(pagina)] = 1

    #print("Quadros finais segunda chance:", quadros)
    bitsReferencia = []
    return faltaDePaginas


def lru(paginas, tamanhoQuadro):
    faltaDePaginas = 0
    quadros = []
    recemUsado = []

    for pagina in paginas:
        if (pagina not in quadros):
            faltaDePaginas += 1
            if (len(quadros) < tamanhoQuadro):
                quadros.append(pagina)
            else:
                if (recemUsado[0] in quadros):
                    quadros[quadros.index(recemUsado[0])] = pagina
                    recemUsado.remove(recemUsado[0])
        else:
            recemUsado.remove(pagina)

        recemUsado.append(pagina)

    #print("Quadros finais LRU: ", quadros)

    return faltaDePaginas


print("\nPáginas:", paginas, "\n")
#print("FIFO - Faltas de pagina:", fifo(paginas, tamanhoQuadro), "\n")
#print("LRU - Faltas de pagina: ", lru(paginas, tamanhoQuadro), "\n")
print("Segunda chance - Faltas de pagina: ", secondChance(paginas, tamanhoQuadro), "\n")


faltasFifo = []
faltasLru = []
faltasSecondChance = []

numQuadrosTotal = list(range(tamanhoQuadro, tamanhoQuadroFinal + 1))
print(numQuadrosTotal)
for numQuadros in numQuadrosTotal:
    faltasFifo.append(fifo(paginas, numQuadros))
    faltasLru.append(lru(paginas, numQuadros))
    faltasSecondChance.append(secondChance(paginas, numQuadros))

plt.plot(numQuadrosTotal, faltasFifo, label='FIFO', linestyle='-', marker='o')
plt.plot(numQuadrosTotal, faltasLru, label='LRU', linestyle='--', marker='D')
plt.plot(numQuadrosTotal, faltasSecondChance, label='Segunda chance', linestyle=':', marker='X')

plt.ylabel('Faltas de página')
plt.xlabel("Número de quadros de RAM")
plt.legend()
plt.grid(True)
plt.show()






