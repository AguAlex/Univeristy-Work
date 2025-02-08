import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

miu = 0
sigma = 1
N = 1000000

def normala_cos(miu, sigma, N):
    U1 = np.random.uniform(0, 1, N)
    U2 = np.random.uniform(0, 1, N)
    X = miu + sigma * np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    return X

def normala_sin(miu, sigma, N):
    U1 = np.random.uniform(0, 1, N)
    U2 = np.random.uniform(0, 1, N)
    X = miu + sigma * np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)
    return X

def normala(miu, sigma, N):
    return np.random.normal(miu, sigma, N)

sim_cos = normala_cos(miu, sigma, N)
sim_sin = normala_sin(miu, sigma, N)
sim_numpy = normala(miu, sigma, N)



plt.figure(figsize=(10, 6))
plt.hist(sim_cos, bins=50, density=True, alpha=0.5, label="Metoda cos")
plt.hist(sim_sin, bins=50, density=True, alpha=0.5, label="Metoda sin")
plt.hist(sim_numpy, bins=50, density=True, alpha=0.5, label="Functia numpy")

x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, miu, sigma)
plt.plot(x, pdf, 'k-', label="Functia de densitate normala")

plt.grid(True)
plt.show()

def estimeaza_statistici(simiulari):
    media = np.mean(simiulari)
    varianta = np.var(simiulari)
    return media, varianta

media_cos, varianta_cos = estimeaza_statistici(sim_cos)
media_sin, varianta_sin = estimeaza_statistici(sim_sin)
media_numpy, varianta_numpy = estimeaza_statistici(sim_numpy)

print(f"Metoda 1: Media = {media_cos}, Varianta = {varianta_cos}")
print(f"Metoda 2: Media = {media_sin}, Varianta = {varianta_sin}")
print(f"Metoda 3: Media = {media_numpy}, Varianta = {varianta_numpy}")
