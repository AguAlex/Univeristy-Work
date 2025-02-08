import numpy as np
import matplotlib.pyplot as plt

def este_in_cerc(x, y, P, r):
    return (x - P[0])**2 + (y - P[1])**2 <= r**2

def este_in_elipsa(x, y, a, b):
    return (x/a)**2 + (y/b)**2 <= 1

P = (2, 2)
r = np.sqrt(2)
a, b = 3, 2
nr_simulari = 100000

x_puncte = np.random.uniform(-4, 4, nr_simulari)
y_puncte = np.random.uniform(-4, 4, nr_simulari)

puncte_in_intersectie = sum(este_in_cerc(x, y, P, r) and este_in_elipsa(x, y, a, b) 
                             for x, y in zip(x_puncte, y_puncte))

aria_totala = 8 * 8
aria_intersectie = (puncte_in_intersectie / nr_simulari) * aria_totala
print("Aria intersectiei:", aria_intersectie)

in_cerc_si_elipsa = [este_in_cerc(x, y, P, r) and este_in_elipsa(x, y, a, b) 
                         for x, y in zip(x_puncte, y_puncte)]

plt.figure(figsize=(6,6))
plt.scatter(x_puncte, y_puncte, c=in_cerc_si_elipsa, s=1, cmap='coolwarm')
plt.title('Simularea intersectiei')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
