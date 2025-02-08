import numpy as np

def probabilitate(nr_simulari):
    nr_coliziuni = 0
    for i in range(nr_simulari):
        zile = []
        for j in range(23):
            nr = np.random.randint(1, 365)
            if nr in zile:
                nr_coliziuni+=1
                break
            zile.append(nr)
    
    return nr_coliziuni/nr_simulari


nr_simulari = 10000

print(probabilitate(nr_simulari))