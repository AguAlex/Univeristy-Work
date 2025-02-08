import numpy as np

def estimeaza_aria_discului(r, R, n):
    x_random = np.random.uniform(-R, R, n)
    y_random = np.random.uniform(-R, R, n)
    
    distante = np.sqrt(x_random**2 + y_random**2)
    
    cazuri_fav = np.sum(distante <= r)
    
    aria_patratului = (2 * R) ** 2
    aria_discului_estimat = (cazuri_fav / n) * aria_patratului
    
    return aria_discului_estimat

r = 1
R = 1  
n = 100000  

aria_estimata = estimeaza_aria_discului(r, R, n)
print(aria_estimata)

