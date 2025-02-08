import heapq

# Functie pentru citirea inputului
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

# Construieste lista de adiacenta
adiacenta = [[] for i in range(n + 1)]
for x, y, c in lista_muchii:
    adiacenta[x].append((c, y))
    adiacenta[y].append((c, x))

# Algoritmul Prim
def prim(n, adiacenta):
    vizitat = [False] * (n + 1)  # Marcam nodurile vizitate
    min_heap = [(0, 1)]  # Initializam coada de prioritati cu nodul 1
    apm = 0

    while min_heap:
        cost, nod = heapq.heappop(min_heap)

        if vizitat[nod]:
            continue
        
        vizitat[nod] = True
        apm += cost

        # Adaugam in coada toate nodurile adiacente cu nodul curent
        for c, n in adiacenta[nod]:
            if not vizitat[n]:
                heapq.heappush(min_heap, (c, n))

    return apm

apm = prim(n, adiacenta)
print("Costul minim: ", apm)
