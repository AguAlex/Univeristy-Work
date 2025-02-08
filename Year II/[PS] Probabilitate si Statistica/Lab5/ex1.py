import numpy as np

nr_simulari = 100000

zar1 = np.random.randint(1, 7, nr_simulari)
zar2 = np.random.randint(1, 7, nr_simulari)

A = (zar1 == 1)
P_A = np.mean(A)

B = (zar2 == 6)
P_B = np.mean(B)

C = (zar1 + zar2 == 7)
P_C = np.mean(C)

A_and_C = A & C
P_A_and_C = np.mean(A_and_C)

B_and_C = B & C
P_B_and_C = np.mean(B_and_C)

A_and_B_and_C = A & B & C
P_A_and_B_and_C = np.mean(A_and_B_and_C)

print(P_A_and_C, P_A * P_C)
print(P_B_and_C, P_B * P_C)
print(P_A_and_B_and_C, P_A * P_B * P_C)


