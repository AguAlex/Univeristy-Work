import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

# A
def binomial_custom_dice(n, p):
    probabilitati = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    outcomes = np.arange(n + 1)
    X = np.random.choice(outcomes, p=probabilitati)
    return X

# B
def binomial_bernoulli_sum(n, p):
    bernoulli_trials = np.random.binomial(1, p, n)
    X = np.sum(bernoulli_trials)
    return X

# C
def binomial_python(n, p):
    X = np.random.binomial(n, p)
    return X

def rez(n, p, N):
    # Liste pentru rez simulari
    results_a = [binomial_custom_dice(n, p) for i in range(N)]
    results_b = [binomial_bernoulli_sum(n, p) for i in range(N)]
    results_c = [binomial_python(n, p) for i in range(N)]
    
    plt.figure(figsize=(15, 5))
    
    # A
    plt.subplot(1, 3, 1)
    plt.hist(results_a, bins=np.arange(-0.5, n + 1.5, 1), density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Metoda (a)')
    plt.xlabel('Valoare')
    plt.ylabel('Frecventa relativa')
    
    # B
    plt.subplot(1, 3, 2)
    plt.hist(results_b, bins=np.arange(-0.5, n + 1.5, 1), density=True, alpha=0.7, color='green', edgecolor='black')
    plt.title('Metoda (b)')
    plt.xlabel('Valoare')
    plt.ylabel('Frecventa relativa')
    
    # C
    plt.subplot(1, 3, 3)
    plt.hist(results_c, bins=np.arange(-0.5, n + 1.5, 1), density=True, alpha=0.7, color='red', edgecolor='black')
    plt.title('Metoda (c)')
    plt.xlabel('Valoare')
    plt.ylabel('Frecventa relativa')
    
    plt.tight_layout()
    plt.show()
    
    # Graficul ponderilor 
    pk = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    plt.figure(figsize=(8, 5))
    plt.stem(range(n + 1), pk, use_line_collection=True) 
    plt.title('Graficul ponderilor')
    plt.xlabel('k')
    plt.ylabel('Probabilitate pk')
    plt.show()
    
    medie_a = np.mean(results_a)
    varianta_a = np.var(results_a)
    medie_b = np.mean(results_b)
    varianta_b = np.var(results_b)
    medie_c = np.mean(results_c)
    varianta_c = np.var(results_c)
    
    print(f"A: Media = {medie_a}, Varianta = {varianta_a}")
    print(f"B: Media = {medie_b}, Varianta = {varianta_b}")
    print(f"C: Media = {medie_c}, Varianta = {varianta_c}")

n = 10  # Nr aruncari
p = 0.5 # Probabilitatea de succes
N = 1000 # Nr simulari

rez(n, p, N)
