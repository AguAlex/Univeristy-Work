import numpy as np
import math

def probabilitate(n, p, k):
    nr = 0
    for i in range(nr_simulari):
        X = np.random.binomial(n, p);
        if X >= k:
            nr += 1
    
    return nr/nr_simulari

n = 500
p = 0.03
k = 10 # Cel putin k indivizi
nr_simulari = 10000
probabilitate = probabilitate(n, p, k)
print(probabilitate)
