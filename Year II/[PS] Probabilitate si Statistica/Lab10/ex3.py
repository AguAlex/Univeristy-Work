import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

date = data('mtcars')

# Extragem coloanele relevante
x = np.array(date['hp'])
y = np.array(date['mpg'])

# (a)
print("Set date:")
print("HP (x):", x[:5])
print("MPG (y):", y[:5])

# (b)
covarianta = np.cov(x, y, bias=True)[0, 1]
corelatia = np.corrcoef(x, y)[0, 1]
print(f"Covarianta: {covarianta}")
print(f"Corelatia: {corelatia}")

# (c)
media_x, media_y = np.mean(x), np.mean(y)
panta = np.sum((x - media_x) * (y - media_y)) / np.sum((x - media_x)**2)
intersectie = media_y - panta * media_x
print(f"Coeficientii regresiei liniare: intersectie = {intersectie}, panta = {panta}")

# (d)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Datele originale')
linia_regresiei = panta * x + intersectie
plt.plot(x, linia_regresiei, color='red', label='Dreapta de regresie')
plt.xlabel('HP')
plt.ylabel('MPG)')
plt.title('Regresia liniara - MPG vs HP')
plt.legend()
plt.grid(True)
plt.show()

# (e)

indici = np.arange(len(x))
numar_antrenare = int(0.8 * len(x))

indici_antrenare = indici[:numar_antrenare]
indici_testare = indici[numar_antrenare:]

x_antrenare, y_antrenare = x[indici_antrenare], y[indici_antrenare]
x_testare, y_testare = x[indici_testare], y[indici_testare]

# Calculam regresia liniara pe setul de antrenare
media_x_antrenare, media_y_antrenare = np.mean(x_antrenare), np.mean(y_antrenare)
panta_antrenare = np.sum((x_antrenare - media_x_antrenare) * (y_antrenare - media_y_antrenare)) / np.sum((x_antrenare - media_x_antrenare)**2)
intersectie_antrenare = media_y_antrenare - panta_antrenare * media_x_antrenare
print(f"Coeficientii regresiei liniare pe setul de antrenare: intersectie = {intersectie_antrenare:.2f}, panta = {panta_antrenare:.2f}")

# Comparam valorile exacte cu cele prezise pentru setul de testare
y_prezis = panta_antrenare * x_testare + intersectie_antrenare
comparare = np.column_stack((y_testare, y_prezis))
print("Compararea valorilor exacte cu cele prezise:")
print("Exact   Prezis")
print(comparare[:5])

# Afisam graficul pentru setul de testare
plt.figure(figsize=(8, 6))
plt.scatter(x_testare, y_testare, color='blue', label='Date test - Exacte')
plt.scatter(x_testare, y_prezis, color='orange', label='Date test - Prezise')
plt.plot(x_testare, panta_antrenare * x_testare + intersectie_antrenare, color='red', label='Dreapta de regresie')
plt.xlabel('HP')
plt.ylabel('MPG')
plt.title('Compararea valorilor exacte si prezise')
plt.legend()
plt.grid(True)
plt.show()
