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

n, m, lista_muchii = citire_input()

# Sortam lista de muchii dupa cost
lista_muchii.sort(key=lambda x: x[2])

# Lista de tati 
T = [i for i in range(n + 1)]
apm = 0

# Functiile pentru algoritm
def find(x):
    if x == T[x]:
        return x
    else:
        T[x] = find(T[x])  # Optimizarea pentru complexitate
        return T[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    T[x] = y
    return True

# Aplicam algorimtul 
for muchie in lista_muchii:
    x, y, c = muchie
    if union(x, y):
        apm += c

print("Costul minim: ", apm)
