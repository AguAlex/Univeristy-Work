import numpy as np

a1 = np.random.uniform(0, 100)
b1 = np.random.uniform(a1, a1 + 100)

a2 = np.random.uniform(0, 100)
b2 = np.random.uniform(a2, a2 + 100)

c1 = np.random.uniform(a1, b1)
d1 = np.random.uniform(c1, b1)

c2 = np.random.uniform(a2, b2)
d2 = np.random.uniform(c2, b2)

n = 10000

x_random = np.random.uniform(a1, b1, n)
y_random = np.random.uniform(a2, b2, n)

cazuri_fav = np.sum((x_random >= c1) & (x_random <= d1) & (y_random >= c2) & (y_random <= d2))

probabilitate = cazuri_fav / n

print(probabilitate)
