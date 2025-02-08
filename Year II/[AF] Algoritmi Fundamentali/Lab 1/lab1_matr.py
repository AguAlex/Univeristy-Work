file = open('input.txt', 'r')

matrice = [[0 for x in range(11)] for x in range(11)]

def matr_graf_orientat():
    for linie in file:
        muchie = linie.split()
        x = int(muchie[0])
        y = int(muchie[1])
        matrice[x-1][y-1] = matrice[y-1][x-1] = 1
    return matrice

def matr_graf_neorientat():
    for linie in file:
        muchie = linie.split()
        x = int(muchie[0])
        y = int(muchie[1])
        matrice[x-1][y-1] = 1
    return matrice

def afisare(matrice):
    for linie in matrice:
        print(*linie)


input = int(input('Alege graf (1 - orientat; 2 - neorientat): '))
if input == 1:
    matrice = matr_graf_orientat()
    afisare(matrice)
elif input == 2:
    matrice = matr_graf_neorientat()
    afisare(matrice)
else:
    print('Input gresit! ')



file.close()
