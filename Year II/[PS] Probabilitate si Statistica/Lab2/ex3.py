import numpy as np

def arunca_moneda():
    return "H" if np.random.rand() <= 0.5 else "T"

def genereaza_aruncari(nr_aruncari):
    return [arunca_moneda() for i in range(nr_aruncari)]

def are_consecutive(secventa, nr_consecutive):
    count = 1  
    for i in range(1, len(secventa)):
        if secventa[i] == secventa[i-1]:
            count += 1
            if count >= nr_consecutive:
                return True
        else:
            count = 1  
    return False

def procentaje_consecutive(nr_simulari, nr_aruncari, nr_consecutive):
    count_consecutive = 0
    for i in range(nr_simulari):
        secventa = genereaza_aruncari(nr_aruncari)
        if are_consecutive(secventa, nr_consecutive):
            count_consecutive += 1
    return count_consecutive / nr_simulari

nr_simulari = 10000  

procentaj_10_aruncari = procentaje_consecutive(nr_simulari, 10, 4)
procentaj_20_aruncari = procentaje_consecutive(nr_simulari, 20, 4)
procentaj_100_aruncari = procentaje_consecutive(nr_simulari, 100, 8)

print(f'Procentajul secventelor de 10 aruncari care au 4 consecutive identice: {procentaj_10_aruncari:}')
print(f'Procentajul secventelor de 20 aruncari care au 4 consecutive identice: {procentaj_20_aruncari:}')
print(f'Procentajul secventelor de 100 aruncari care au 8 consecutive identice: {procentaj_100_aruncari:}')
