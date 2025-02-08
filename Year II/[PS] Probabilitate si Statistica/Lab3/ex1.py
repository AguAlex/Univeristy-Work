import numpy as np

a = np.random.uniform(0, 100)
b = np.random.uniform(a, a + 100)  

c = np.random.uniform(a, b)
d = np.random.uniform(c, b)  

n = 10000
cazuri_fav = 0
for i in range(n):
    x = np.random.uniform(a, b)
    if x <= d and x >= c:
        cazuri_fav += 1

print(cazuri_fav/n)


