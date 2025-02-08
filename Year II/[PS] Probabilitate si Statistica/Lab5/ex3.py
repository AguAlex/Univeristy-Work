import numpy as np

nr_simulari = 100000

zar1 = np.random.randint(1, 7, nr_simulari)
zar2 = np.random.randint(1, 7, nr_simulari)

#ambele zaruri sa fie pare
A = (zar1 % 2 == 0)
P_A = np.mean(A)

#suma zarurilor sa fie 10
B = (zar1 + zar2 == 10)
P_B = np.mean(B)

#zar1 sa fie mai mic decat zar2
C = (zar1 < zar2)
P_C = np.mean(C)

A_and_C = A & C
P_A_and_C = np.mean(A_and_C)

B_and_C = B & C
P_B_and_C = np.mean(B_and_C)

A_and_B = A & B
P_A_and_B = np.mean(A_and_B)

A_and_B_and_C = A & B & C
P_A_and_B_and_C = np.mean(A_and_B_and_C)

print(P_A_and_C, P_A * P_C)
print(P_B_and_C, P_B * P_C)
print(P_A_and_B, P_A * P_B)
print(P_A_and_B_and_C, P_A * P_B * P_C)


