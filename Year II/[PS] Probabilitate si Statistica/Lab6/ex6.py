# Consideram o persoana care arunca o moneda echitabila, unde probabilitatea de a obtine "cap" la fiecare aruncare este de 
# p=0.5. Dorim sa aflam probabilitatea ca prima aparitie a lui "cap" sa fie exact la a treia aruncare.

import numpy as np

p = 0.5    
k = 3    # numarul de aruncari pana la primul succes dorit

nr_simulari = 100000

rezultate = np.random.geometric(p, nr_simulari)

probabilitate_k = np.mean(rezultate == k)

print(f"Probabilitatea estimata ca primul 'cap' sa apara exact la aruncarea a {k}-a este: {probabilitate_k}")
