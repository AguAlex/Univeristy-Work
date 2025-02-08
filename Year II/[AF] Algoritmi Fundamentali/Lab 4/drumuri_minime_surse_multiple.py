import heapq

def citeste_input(nume_fisier):
    with open(nume_fisier, 'r') as f:
        n, m, k = map(int, f.readline().split())
        fortarete = list(map(int, f.readline().split()))
        
        # Construim lista de adiacenta pentru graf
        graf = [[] for i in range(n + 1)]
        for i in range(m):
            x, y, c = map(int, f.readline().split())
            graf[x].append((y, c))
            graf[y].append((x, c))
    
    return n, m, k, fortarete, graf

def dijkstra_fortarete(n, fortarete, graf):
    inf = float('inf')
    distanta = [inf] * (n + 1)  # Initializam distantele la infinit
    fortareata_parinte = [0] * (n + 1)  # Vectorul pentru retinerea fortaretei parinte
    
    # Initializam coada de prioritati cu fortaretele
    queue = []
    for fortareata in fortarete:
        distanta[fortareata] = 0
        fortareata_parinte[fortareata] = fortareata  # Fiecare fortareata se leaga de ea insasi
        heapq.heappush(queue, (0, fortareata))
    
    # Algoritmul Dijkstra modificat pentru multiple surse
    while queue:
        dist_curenta, nod = heapq.heappop(queue)
        
        if dist_curenta > distanta[nod]:
            continue
        
        # Verificam vecinii
        for vecin, cost in graf[nod]:
            noua_distanta = dist_curenta + cost
            if noua_distanta < distanta[vecin] or (noua_distanta == distanta[vecin] and fortareata_parinte[nod] < fortareata_parinte[vecin]):
                distanta[vecin] = noua_distanta
                fortareata_parinte[vecin] = fortareata_parinte[nod]
                heapq.heappush(queue, (noua_distanta, vecin))
    
    return fortareata_parinte


# Citim datele de intrare
n, m, k, fortarete, graf = citeste_input('catun.in')

rezultat = dijkstra_fortarete(n, fortarete, graf)

print(" ".join(map(str, rezultat[1:])))


