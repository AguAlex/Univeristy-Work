import numpy as np
import matplotlib.pyplot as plt

def estimeaza_pi_buffon(N, lungime_ac=1, distanta_linii=1):
    unghiuri = np.random.uniform(0, np.pi/2, N)
    distante = np.random.uniform(0, distanta_linii/2, N)
    
    lovituri = sum(lungime_ac / 2 * np.sin(unghi) >= distanta 
                   for unghi, distanta in zip(unghiuri, distante))
    
    return (2 * lungime_ac * N) / (distanta_linii * lovituri)

pi_buffon_estimare = estimeaza_pi_buffon(100000)
print("Estimare pi:", pi_buffon_estimare)
