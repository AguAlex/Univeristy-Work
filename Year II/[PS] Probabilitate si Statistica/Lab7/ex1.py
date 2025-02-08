import numpy as np
import matplotlib.pyplot as plt

lambda_param = 4  
n = 1000          
N = 10000   

binomial = np.random.binomial(n, lambda_param / n, N)

poisson = np.random.poisson(lambda_param, N)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(binomial, bins=30, alpha=0.7, color='blue', edgecolor='black', density=True)
plt.title("(A)")

plt.subplot(1, 2, 2)
plt.hist(poisson, bins=30, alpha=0.7, color='green', edgecolor='black', density=True)
plt.title("(B)")

plt.tight_layout()
plt.show()

media_binomial = np.mean(binomial)
varianta_binomial = np.var(binomial)

media_poisson = np.mean(poisson)
varianta_poisson = np.var(poisson)

print(f"Media a: {media_binomial}")
print(f"Varianta a: {varianta_binomial}")
print(f"Media b: {media_poisson}")
print(f"Varianta b: {varianta_poisson}")
