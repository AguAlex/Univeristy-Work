import numpy as np
import matplotlib.pyplot as plt

# (a) Generarea geometrica folosind formula
def generare_geometric_formula(p):
    U = np.random.uniform(0, 1)
    X = int(np.floor(np.log(U) / np.log(1 - p))) + 1 
    return X

# (b) Generarea geometrica folosind functia din python
def generare_geometric_numpy(p):
    return np.random.geometric(p)

# (c) 
def simulari(n, p, N):
    rez_a = [generare_geometric_formula(p) for i in range(N)]
    
    rez_b = [generare_geometric_numpy(p) for i in range(N)]
    
    plt.figure(figsize=(15, 5))
    
    # A
    plt.subplot(1, 3, 1)
    plt.hist(rez_a, bins=range(1, max(rez_a) + 1), density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Metoda (a)')

    # B
    plt.subplot(1, 3, 2)
    plt.hist(rez_b, bins=range(1, max(rez_b) + 1), density=True, alpha=0.7, color='green', edgecolor='black')
    plt.title('Metoda (b)')
    
    plt.tight_layout()
    plt.show()

    # (e)
    k_values = np.arange(1, 21)
    pk = (1 - p) ** (k_values - 1) * p
    
    plt.figure(figsize=(8, 5))
    plt.stem(k_values, pk, basefmt=" ")
    plt.title('Graficul ponderilor pk')
    plt.show()

    # (f) 
    media_a = np.mean(rez_a)
    varianta_a = np.var(rez_a)
    
    media_b = np.mean(rez_b)
    varianta_b = np.var(rez_b)

    print(f"Media = {media_a}, Varianta = {varianta_a}")
    print(f"Media = {media_b}, Varianta = {varianta_b}")

n = 10  
p = 0.3  
N = 1000  

simulari(n, p, N)
