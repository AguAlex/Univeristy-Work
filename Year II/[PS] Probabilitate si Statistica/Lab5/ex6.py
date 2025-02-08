import numpy as np
import matplotlib.pyplot as plt

def simulare_joc(m, M):
    bani = m
    pasi = 0
    while bani > 0 and bani < M:
        pasi += 1
        if np.random.rand() < 0.5:
            castig = np.random.randint(1, 11)
            bani += castig
        else:
            pierdere = np.random.randint(1, 11)
            bani -= pierdere
    return pasi, bani >= M

def simulare_multipla(num_simulari, m, M):
    victorii = 0
    durate_jocuri = []

    for i in range(num_simulari):
        pasi, castigat = simulare_joc(m, M)
        durate_jocuri.append(pasi)
        if castigat:
            victorii += 1

    probabilitate_castig = victorii / num_simulari
    return probabilitate_castig, durate_jocuri

m = 50
M = 200
num_simulari = 1000

probabilitate_castig, durate_jocuri = simulare_multipla(num_simulari, m, M)

print(probabilitate_castig)

plt.hist(durate_jocuri, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Durata jocului')
plt.ylabel('Frecventa')
plt.title('Histograma')
plt.show()
