import numpy as np
import matplotlib.pyplot as plt

data = np.load('Lab11/sample_Bernoulli_1.npy')
estimare = np.mean(data)
plt.hist(data, bins=100, edgecolor='black')
plt.title(f'Histograma Bernoulli 1 {estimare}')
plt.show()

# data = np.load('Lab11/sample_Bernoulli_2.npy')

# plt.hist(data, bins=100, edgecolor='black')
# plt.title('Histograma Bernoulli 2')
# plt.show()

# data = np.load('Lab11/sample_Exp.npy')
# plt.hist(data, bins=100, edgecolor='black')
# plt.title('Histograma Exp')
# plt.show()

# data = np.load('Lab11/sample_Geom.npy')

# plt.hist(data, bins=100, edgecolor='black')
# plt.title('Histograma Geom')
# plt.show()

# data = np.load('Lab11/sample_Normal.npy')

# plt.hist(data, bins=100, edgecolor='black')
# plt.title('Histograma Normal')
# plt.show()

# (b)
def log_likelihood(theta, data):
    if theta <= 0 or theta >= 1:
        return -np.inf  
    return np.sum(data * np.log(theta) + (1 - data) * np.log(1 - theta))

theta_values = np.linspace(0.01, 0.99, 500)  
log_likelihood_values = [log_likelihood(theta, data) for theta in theta_values]

plt.plot(theta_values, log_likelihood_values)
plt.title('Functia Log-Likelihood pentru Bernoulli')
plt.grid()
plt.show()


