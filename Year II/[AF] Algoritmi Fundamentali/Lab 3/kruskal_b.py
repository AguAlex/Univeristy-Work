# Functie pentru prelucrarea inputului
def citire_input():
    f = open("grafpond.in")
    lista_muchii = []
    
    # Citeste numarul de noduri si numarul de muchii
    aux = f.readline().split()
    n = int(aux[0])
    m = int(aux[1])
    
    # Citeste fiecare muchie
    for i in range(m):
        aux = f.readline().split()
        x = int(aux[0])
        y = int(aux[1])
        c = int(aux[2])
        lista_muchii.append((x, y, c))

    f.close()
    return n, m, lista_muchii

# Citeste cele trei muchii impuse de la tastatura
def citire_muchii_impuse():
    muchii_impuse = []
    for i in range(3):
        aux = input(f"Introduceti muchia {i+1}: ").split()
        x = int(aux[0])
        y = int(aux[1])
        muchii_impuse.append((x, y))
    return muchii_impuse

n, m, lista_muchii = citire_input()
muchii_impuse = citire_muchii_impuse()

# Sortam lista de muchii dupa cost
lista_muchii.sort(key=lambda x: x[2])

# Lista de tati
T = [i for i in range(n + 1)]
apm = 0
arbore_final = []  # Lista pentru muchiile din arborele rezultat

# Functiile pentru algoritm
def find(x):
    if x == T[x]:
        return x
    else:
        T[x] = find(T[x])
        return T[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    T[x] = y
    return True

# Adaugam muchiile impuse in arbore si actualizam structura de uniune
for (x, y) in muchii_impuse:
    if union(x, y):
        arbore_final.append((x, y))
    else:
        print("Nu se poate construi un arbore cu cele trei muchii citite.")
        exit()

# Aplicam algoritmul pentru restul muchiilor
for muchie in lista_muchii:
    x, y, c = muchie
    if union(x, y):
        arbore_final.append((x, y))
        apm += c

# Afisam rezultatele
print("Costul minim:", apm)
print("Muchiile arborelui parțial minim: ")
for (x, y) in arbore_final:
    print(f"{x}  {y}")
