import numpy as np
import matplotlib.pyplot as plt

def estimeaza_pi_cerc_patrat(R, r, nr_simulari):
    x_puncte = np.random.uniform(-R/2, R/2, nr_simulari)
    y_puncte = np.random.uniform(-R/2, R/2, nr_simulari)
    
    puncte_in_cerc = sum(x**2 + y**2 <= r**2 for x, y in zip(x_puncte, y_puncte))
    
    return (puncte_in_cerc / nr_simulari) * (R**2 / r**2)

R = 2
r = 1
nr_simulari = 100000

pi_estimare = estimeaza_pi_cerc_patrat(R, r, nr_simulari)
print("Estimare pi: ", pi_estimare)
