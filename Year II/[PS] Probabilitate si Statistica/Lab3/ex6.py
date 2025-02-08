import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return x**2 + y**4 + 2*x*y - 1

def f2(x, y):
    return y**2 + x**2 * np.cos(x) - 1

def f3(x, y):
    return np.exp(x**2) + y**2 - 4 + 2.99 * np.cos(y)

def estimeaza_aria(functie, domeniu, N):
    x_puncte = np.random.uniform(domeniu[0], domeniu[1], N)
    y_puncte = np.random.uniform(domeniu[2], domeniu[3], N)
    puncte_in_domeniu = sum(functie(x, y) <= 0 for x, y in zip(x_puncte, y_puncte))
    aria_totala = (domeniu[1] - domeniu[0]) * (domeniu[3] - domeniu[2])
    return (puncte_in_domeniu / N) * aria_totala

domeniu_D1 = [-3, 3, -3, 3]
domeniu_D2 = [-5, 5, -5, 5]
domeniu_D3 = [-2.5, 2.5, -2.5, 2.5]

aria_D1 = estimeaza_aria(f1, domeniu_D1, 100000)
aria_D2 = estimeaza_aria(f2, domeniu_D2, 100000)
aria_D3 = estimeaza_aria(f3, domeniu_D3, 100000)

print("Aria D1:", aria_D1)
print("Aria D2:", aria_D2)
print("Aria D3:", aria_D3)

x_puncte = np.random.uniform(-3, 3, 100000)
y_puncte = np.random.uniform(-3, 3, 100000)
in_D1 = [f1(x, y) <= 0 for x, y in zip(x_puncte, y_puncte)]

plt.figure(figsize=(6,6))
plt.scatter(x_puncte, y_puncte, c=in_D1, s=1, cmap='coolwarm')
plt.title('Simularea domeniului D1')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
