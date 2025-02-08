def afisare_lista(lista):
    for m in lista:
        print(f"{m}: ", end="")
        if len(lista[m]) == 0:
            print("{}", " ")
        else:
            print(lista[m])

def afisare_matr(matrice):
    for linie in matrice[1:]:
        print(*linie)

def matr_list():
    file = open("input_matr-lista.txt")
    lista = {i: set() for i in range(1,12)}
    i = 1
    for linie in file:
        muchii = linie.split()
        j = 1
        for m in muchii:
            if m == "1":
                lista[int(i)].add(int(j))
            j += 1
        i += 1

    afisare_lista(lista)
    file.close()

def list_matr():
    file = open("input_lista-matr.txt")
    matr = [[0 for x in range(12)] for x in range(12)]
    for linie in file:
        aux = linie.split(":")
        nod = int(aux[0].strip())
        for x in aux[1][2:-2].split(","):
            x.strip()
            if "}" not in x:
                matr[nod][int(x)] = matr[int(x)][nod] = 1

    afisare_matr(matr)
    file.close()

alegere = int(input("Alege o conversie(1: matr -> lista; 2: lista -> matr): "))
if alegere == 1:
    matr_list()
elif alegere == 2:
    list_matr()
else:
    print("Input incorect")