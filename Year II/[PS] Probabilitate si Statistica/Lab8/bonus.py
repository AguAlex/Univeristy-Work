import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Functie pentru simularea unei traiectorii aleatoare
def mers_aleator(n, p):
    pozitii = [0]  # Pozitia initiala
    for i in range(n):
        pas = np.random.choice([-1, 1], p=[1-p, p])  # Pas aleator cu probabilitati p si 1-p
        pozitii.append(pozitii[-1] + pas)  # Actualizam pozitia curenta
    return pozitii

# Functie pentru simularea N pozitii finale dupa n pasi
def simuleaza_traiectorii(n, num_simulari, p):
    pozitii_finale = []
    for _ in range(num_simulari):
        pozitii = mers_aleator(n, p)
        pozitii_finale.append(pozitii[-1])  # Adaugam pozitia finala dupa n pasi
    return pozitii_finale

# Afisare grafic a traiectoriei si a histogramei pozitiei finale
def afiseaza_grafice(n, num_simulari, p):
    # Simulare si afisare a unei singure traiectorii
    traseu = mers_aleator(n, p)
    
    # Simulam mai multe traiectorii si colectam pozitiile finale
    pozitii_finale = simuleaza_traiectorii(n, num_simulari, p)
    
    # Calculam parametrii pentru distributia normala
    medie = (2 * p - 1) * n  # E[X1] = 2p - 1
    dispersie = 4 * p * (1 - p) * n  # Var(X1) = 4p(1-p)
    
    # Graficul traiectoriei
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(traseu, marker='o')
    plt.title(f'Traseul unei simulari (p={p}, {n} pasi)')
    plt.xlabel('Pasul')
    plt.ylabel('Pozitia')
    
    # Histograma pozitiilor finale
    plt.subplot(1, 2, 2)
    plt.hist(pozitii_finale, bins=30, density=True, color='orange', edgecolor='black', alpha=0.6, label='Simulare')
    
    # Distributia normala teoretica
    x = np.linspace(min(pozitii_finale), max(pozitii_finale), 100)
    plt.plot(x, norm.pdf(x, medie, np.sqrt(dispersie)), 'r-', lw=2, label='Distributia teoretica')
    
    plt.title(f'Histograma pozitiilor finale si distributia normala (p={p})')
    plt.xlabel('Pozitia finala')
    plt.ylabel('Densitate')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Parametrii simularii
n = 100        # Numarul de pasi
num_simulari = 1000  # Numarul de simulari
p = 0.7        # Probabilitatea pasului la dreapta

# Apelam functia de afisare
afiseaza_grafice(n, num_simulari, p)
