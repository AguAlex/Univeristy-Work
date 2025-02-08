import numpy as np
import matplotlib.pyplot as plt

def HT_corecta():
    prob = np.random.rand()
    if prob <= 0.5:
        return "H"
    else:
        return "T"
    
def HT_masluita():
    prob = np.random.rand()
    if prob <= 0.7:
        return "H"
    else:
        return "T"

def probabilitate(nr_simulari):
    contor_H1 = 0

    for i in range(nr_simulari):
        prob = HT_corecta()
        if prob == "H":
            contor_H1 += 1

    contor_H2 = 0
    for i in range(nr_simulari):
        prob = HT_masluita()
        if prob == "H":
            contor_H2 += 1
    
    return contor_H1/nr_simulari, contor_H2/nr_simulari

nr_simulari = 10000
raspuns = probabilitate(nr_simulari)
print(f'Moneda corecta: {raspuns[0]} \nMoneda masluita: {raspuns[1]}')


x = np.linspace(-10, nr_simulari, 1000)
y = raspuns[0]*x
plt.plot(x, y)

plt.show()

