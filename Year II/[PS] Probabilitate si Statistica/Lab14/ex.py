import matplotlib.pyplot as plt
from scipy.stats import t
import numpy as np

file_path = "Lab14/sample_Normal(mu,sigma2).npy"

data = np.load(file_path)

n = 10000
df = n - 1
alpha_values = [0.10, 0.05, 0.01] # 1-alpha

# 1
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
plt.title('Histograma valori xi')
plt.grid(alpha=0.3)
plt.show()

# 2
x_vals = np.linspace(-5, 5, 500)
t_dist = t.pdf(x_vals, df)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, t_dist,  color='red')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# 3
cuantile = {}
for alpha in alpha_values:
    ci = t.interval(1 - alpha, df)
    cuantile[f"1-alpha = {1-alpha:.2f}"] = ci

print(cuantile)

# 5
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)
standard_error = sample_std / np.sqrt(n)

intervale_incredere = {}
for alpha in alpha_values:
    ci = t.interval(1 - alpha, df, loc=sample_mean, scale=standard_error)
    intervale_incredere[f"1-alpha = {1-alpha:.2f}"] = ci

for x, ci in intervale_incredere.items():
    print(f"{x}: Interval de incredere pentru mu = {ci}")
