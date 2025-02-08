import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * x) + 0.3 * np.cos(10 * x) + 0.05 * np.sin(100 * x)

def gaussian(f, x_puncte, sigma, n_samples):
    F_sigma2 = []
    for x in x_puncte:
        y_samples = np.random.normal(0, sigma, n_samples)
        integrala = np.mean(f(x - y_samples))
        F_sigma2.append(integrala)
    return np.array(F_sigma2)

a, b = 0, 5
x_puncte = np.linspace(a, b, 200)
n_samples = 10000
sigma_values = [1, 0.5, 0.2, 0.1, 0.05]
colors = ['blue', 'green', 'orange', 'red', 'purple']

# (a)
x_vals = np.linspace(a, b, 1000)
f_vals = f(x_vals)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='f(x)', color='black', linewidth=1.5)

# (b) si (c)
for sigma, color in zip(sigma_values, colors):
    F_sigma2_vals = gaussian(f, x_puncte, sigma, n_samples)
    plt.plot(x_puncte, F_sigma2_vals, color=color)
plt.legend()
plt.grid(True)
plt.show()
