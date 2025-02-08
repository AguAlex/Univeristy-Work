file = open('input.txt', 'r')

lista = {x:set() for x in range(1, 12)}

def lista_graf_orientat():
    for linie in file:
        muchie = linie.split()
        x = int(muchie[0])
        y = int(muchie[1])
        lista[x].add(y)
        lista[y].add(x)
    return lista

def lista_graf_neorientat():
    for linie in file:
        muchie = linie.split()
        x = int(muchie[0])
        y = int(muchie[1])
        lista[x].add(y)
    return lista

def afisare(lista):
    for m in lista:
        print(f"{m}: ", end="")
        if len(lista[m]) == 0:
            print("{}", " ")
        else:
            print(lista[m])

input = int(input('Alege graf (1 - orientat; 2 - neorientat): '))
if input == 1:
    lista = lista_graf_orientat()
    afisare(lista)
elif input == 2:
    lista = lista_graf_neorientat()
    afisare(lista)
else:
    print('Input gresit! ')

file.close()

