import numpy as np
import matplotlib.pyplot as plt

m = 5  
M = 10
nr_simulari = 100000

def simuleaza_joc(m, M):
    suma = m
    nr_aruncari = 0

    while suma > 0 and suma < M: 
        nr_aruncari += 1
        if np.random.rand() < 0.5:  
            suma += 1
        else:  
            suma -= 1
    
    return int(suma >= M), nr_aruncari

rezultate = np.zeros(nr_simulari)
duratele = np.zeros(nr_simulari)

for i in range(nr_simulari):
    rezultat, nr_aruncari = simuleaza_joc(m, M)
    rezultate[i] = rezultat
    duratele[i] = nr_aruncari

probabilitate_castig = np.mean(rezultate)
print(probabilitate_castig)

plt.figure(figsize=(10, 5))
plt.hist(duratele, bins=50, color='blue', alpha=0.7, edgecolor='black')
plt.show()
