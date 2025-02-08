import numpy as np

zar_rosu = [1, 4, 4, 4, 4, 4]   
zar_verde = [3, 3, 3, 3, 3, 6]  
zar_negru = [2, 2, 2, 5, 5, 5]  

def arunca_zar(zar):
    return np.random.choice(zar)

def calculeaza_probabilitate(zar_A, zar_B, nr_simulari):
    count_A_castiga = 0
    for i in range(nr_simulari):
        rezultat_A = arunca_zar(zar_A)
        rezultat_B = arunca_zar(zar_B)
        if rezultat_A > rezultat_B:
            count_A_castiga += 1
    return count_A_castiga / nr_simulari  

nr_simulari = 1000

prob_rosu_vs_verde = calculeaza_probabilitate(zar_rosu, zar_verde, nr_simulari)
prob_rosu_vs_negru = calculeaza_probabilitate(zar_rosu, zar_negru, nr_simulari)
prob_verde_vs_negru = calculeaza_probabilitate(zar_verde, zar_negru, nr_simulari)

prob_verde_vs_rosu = 1 - prob_rosu_vs_verde
prob_negru_vs_rosu = 1 - prob_rosu_vs_negru
prob_negru_vs_verde = 1 - prob_verde_vs_negru

print(f'Probabilitatea ca zarul roșu să bată zarul verde: {prob_rosu_vs_verde:}')
print(f'Probabilitatea ca zarul roșu să bată zarul negru: {prob_rosu_vs_negru:}')
print(f'Probabilitatea ca zarul verde să bată zarul negru: {prob_verde_vs_negru:}')
print(f'Probabilitatea ca zarul verde să bată zarul roșu: {prob_verde_vs_rosu:}')
print(f'Probabilitatea ca zarul negru să bată zarul roșu: {prob_negru_vs_rosu:}')
print(f'Probabilitatea ca zarul negru să bată zarul verde: {prob_negru_vs_verde:}')
