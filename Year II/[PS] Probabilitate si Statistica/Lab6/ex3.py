# Consideram o persoana care arunca o moneda corecta (cu probabilitate 
# p = 0.5 pentru "cap") de 10 ori (deci n=10). Dorim să aflam probabilitatea
# de a obtine exact 6 "cap".

import numpy as np

n = 10
p = 0.5 # probabilitatea de "cap" pentru fiecare aruncare
k = 6  # numarul de succese dorit

nr_simulari = 100000
rezultate = np.random.binomial(n, p, nr_simulari)

probabilitate_k = np.mean(rezultate == k)

print(f"Probabilitatea estimata de a obtine exact {k} 'cap' in {n} aruncari este: {probabilitate_k}")
