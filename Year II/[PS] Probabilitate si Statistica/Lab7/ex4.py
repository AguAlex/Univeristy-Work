import numpy as np
import matplotlib.pyplot as plt

lambda_param = 5.0
N = 10000

U = np.random.uniform(0, 1, N)
exponentiala_a = -1 / lambda_param * np.log(U)

exponentiala_b = np.random.exponential(1 / lambda_param, N)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(exponentiala_a, bins=50, color='blue', alpha=0.7, edgecolor='black', density=True)
plt.title('(A)')

plt.subplot(1, 2, 2)
plt.hist(exponentiala_b, bins=50, color='green', alpha=0.7, edgecolor='black', density=True)
plt.title('(B)')

plt.tight_layout()
plt.show()

x_vals = np.linspace(0, 10, 1000)
pdf_vals = lambda_param * np.exp(-lambda_param * x_vals)

plt.figure(figsize=(10, 6))
plt.hist(exponentiala_a, bins=50, color='blue', alpha=0.5, edgecolor='black', density=True, label='Metoda a')
plt.hist(exponentiala_b, bins=50, color='green', alpha=0.5, edgecolor='black', density=True, label='Metoda b')
plt.plot(x_vals, pdf_vals, color='red', linewidth=2)
plt.title('Densitate')
plt.legend()
plt.show()

media_a = np.mean(exponentiala_a)
varianta_a = np.var(exponentiala_a)

media_b = np.mean(exponentiala_b)
varianta_b = np.var(exponentiala_b)

print(f"Media a: {media_a}")
print(f"Varianta a: {varianta_a}")
print(f"Media b: {media_b}")
print(f"Varianta b: {varianta_b}")
