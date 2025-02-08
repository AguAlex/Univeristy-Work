import numpy as np
import matplotlib.pyplot as plt

def genereaza_numere(N, a, b):
    uniforme = np.random.uniform(0, 1, N)
    
    beta = np.random.beta(a, b, N)
    
    phi = np.random.uniform(-np.pi, np.pi, N)
    cos_dist = np.cos(phi)
    
    normal = np.random.normal(0, 1, N)
    
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(uniforme, bins=50, color='blue', alpha=0.7)

    plt.subplot(2, 2, 2)
    plt.hist(beta, bins=50, color='green', alpha=0.7)

    plt.subplot(2, 2, 3)
    plt.hist(phi, bins=50, color='orange', alpha=0.7)

    plt.subplot(2, 2, 4)
    plt.hist(normal, bins=50, color='red', alpha=0.7)

    plt.tight_layout()
    plt.show()

N = 10000
a = 2
b = 5
genereaza_numere(N, a, b)
