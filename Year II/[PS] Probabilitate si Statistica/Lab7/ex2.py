import numpy as np

lambda_param = 150
nr_simulari = 100000

pacienti_simulare = np.random.poisson(lambda_param, nr_simulari)

probabilitate = np.mean(pacienti_simulare > 150)

print(probabilitate)
