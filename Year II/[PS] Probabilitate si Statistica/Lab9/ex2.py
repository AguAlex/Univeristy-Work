import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 10 * np.exp(-10 * x) * x**2 * np.sin(x)

lambda_param = 10
def importanta(x):
    return lambda_param * np.exp(-lambda_param * x)

def monte_carlo_imp(f, importance_pdf, lambda_param, n):
    x_samples = np.random.exponential(1/lambda_param, n)
    
    aprox = f(x_samples) / importance_pdf(x_samples)
    integrala_estimare = np.mean(aprox)
    
    return integrala_estimare, x_samples

a, b = 0, 100
n_values = np.linspace(100, 10000, 20, dtype=int)
simulari = 100

# (b)
integrala_aprox = []
for n in n_values:
    integral_estimate, _ = monte_carlo_imp(func, importanta, lambda_param, n)
    integrala_aprox.append(integral_estimate)

# Graficul aproximarilor
plt.figure(figsize=(8, 5))
plt.plot(n_values, integrala_aprox)
plt.title('Aproximarea integralei')
plt.legend()
plt.grid(True)
plt.show()

# (c) 
n_fixat = n_values[-1]
simulations = [monte_carlo_imp(func, importanta, lambda_param, n_fixat)[0] for i in range(simulari)]

# Histograma simularilor
plt.figure(figsize=(8, 5))
plt.hist(simulations, bins=15, color='skyblue', edgecolor='black')
plt.title(f'Histograma simulari pentru n fixat')
plt.grid(True)
plt.show()
