import numpy as np
import matplotlib.pyplot as plt

def zar_corect():
    prob = np.random.rand()
    if prob <= 1/6:
        return 1
    elif prob <= 2/6:
        return 2
    elif prob <= 3/6:
        return 3
    elif prob <= 4/6:
        return 4
    elif prob <= 5/6:
        return 5
    else:
        return 6

def probabilitate(nr_simulari):
    contor_6 = 0

    for i in range(nr_simulari):
        rezultat = zar_corect()
        if rezultat == 6:
            contor_6 += 1

    return contor_6 / nr_simulari

nr_simulari = 1000
prob_6 = probabilitate(nr_simulari)

print(f'Probabilitatea de a obtine 6 cu zarul: {prob_6}')



