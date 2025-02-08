import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

miu = 0
sigma = 1
n = 30 # Nr de variabile independente
N = 10000  # Nr simiulari

def genereaza_z(miu, sigma, n, N):
    X = np.random.normal(miu, sigma, (N, n))

    medii_X = np.mean(X, axis=1)

    Z = np.sqrt(n) * (medii_X - miu) / sigma
    return Z

sim_z = genereaza_z(miu, sigma, n, N)

plt.figure(figsize=(10, 6))

plt.hist(sim_z, bins=50, density=True, alpha=0.6, color='blue')

x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, 0, 1)
plt.plot(x, pdf, 'r-', lw=2, label="Functia densitate N(0,1)")

plt.grid(True)
plt.show()
