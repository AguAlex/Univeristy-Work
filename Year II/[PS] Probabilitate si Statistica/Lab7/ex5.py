import numpy as np

functionare_1 = 2.5 
functionare_2 = 5.0 

N = 100000

simul_telefon1 = np.random.exponential(scale=functionare_1, size=N)
simul_telefon2 = np.random.exponential(scale=functionare_2, size=N)

prob_telefon1_estimat = np.mean(simul_telefon1 > 2.5)
prob_telefon2_estimat = np.mean(simul_telefon2 > 5.0)

print(f"Probabilitate telefon 1: {prob_telefon1_estimat}")
print(f"Probabilitate telefon 2: {prob_telefon2_estimat}")
