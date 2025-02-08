import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return np.exp(-x**2)

def monte_carlo_integrala(f, a, b, n):
    x_samples = np.random.uniform(a, b, n)
    integrala = (b - a) * np.mean(f(x_samples))
    return integrala

a, b = 0, 1
n_values = np.linspace(100, 10000, 20, dtype=int)
simulari = 10000

x = np.linspace(a, b, 1000)
y = func1(x)
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title(f'Graficul functiei pe intervalul [{a}, {b}]')
plt.legend()
plt.grid(True)
plt.show()

# (b)
integrale = []
for n in n_values:
    integrale.append(monte_carlo_integrala(func1, a, b, n))

# (c)
plt.figure(figsize=(8, 4))
plt.plot(n_values, integrale)
plt.title('Aproximarea integralei in functie de esantioane')
plt.legend()
plt.grid(True)
plt.show()

# (d)
simulations = [monte_carlo_integrala(func1, a, b, n_values[-1]) for i in range(simulari)]

# (e) Histograma 
plt.figure(figsize=(8, 4))
plt.hist(simulations, bins=15, color='skyblue', edgecolor='black')
plt.title(f'Histograma simulari')
plt.grid(True)
plt.show()
