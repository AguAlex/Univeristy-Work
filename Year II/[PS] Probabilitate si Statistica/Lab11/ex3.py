import numpy as np
import matplotlib.pyplot as plt

def log_likelihood_theta2(data, theta2, miu=0):
    n = len(data)
    if theta2 <= 0:
        return -np.inf
    return -n * np.log(np.sqrt(2 * np.pi * theta2)) - (1 / (2 * theta2)) * np.sum((data - miu) ** 2)

def log_likelihood_theta1(data, theta1, sigma2=0.01):
    n = len(data)
    return -n * np.log(np.sqrt(2 * np.pi * sigma2)) - (1 / (2 * sigma2)) * np.sum((data - theta1) ** 2)

data = np.load('Lab11/sample_Normal.npy')
n = len(data)

# (a) 
plt.figure(figsize=(8, 6))
plt.hist(data, bins=20, edgecolor='black', alpha=0.7)
plt.title('Histograma datelor')
plt.grid()
plt.show()

# (b)
miu = 0
theta2_values = np.linspace(0.001, 0.1, 500)
log_likelihood_values_theta2 = [log_likelihood_theta2(data, theta2, miu) for theta2 in theta2_values]

# (c)
theta2_est = np.mean((data - miu) ** 2)
print(f"Estimare: {theta2_est}")

# (d)
plt.figure(figsize=(8, 6))
plt.plot(theta2_values, log_likelihood_values_theta2, color='blue')
plt.grid()
plt.show()

# (e)
sigma2 = 0.01
theta1_values = np.linspace(-1, 1, 500)
log_likelihood_values_theta1 = [log_likelihood_theta1(data, theta1, sigma2) for theta1 in theta1_values]

# (f)
theta1_est = np.mean(data)
print(f"Estimare: {theta1_est}")

# (g)
plt.figure(figsize=(8, 6))
plt.plot(theta1_values, log_likelihood_values_theta1, color='green')
plt.grid()
plt.show()