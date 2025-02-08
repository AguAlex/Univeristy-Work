import heapq

# Algoritmului Dijkstra
def dijkstra(noduri, graf, sursa):
    dist = [float('inf')] * (noduri + 1)  # Distantele initiale
    dist[sursa] = 0  # Distanța fata de sursa este 0
    parinte = [None] * (noduri + 1)  # Array pentru a urmari drumul minim
    pq = [(0, sursa)]  # Coada de prioritati
    
    while pq:
        curent_dist, nod = heapq.heappop(pq)  # Nodul cu distanta minimă
        if curent_dist > dist[nod]:
            continue
        # Parcurgem vecinii
        for vecin, cost in graf[nod]:
            if dist[nod] + cost < dist[vecin]:
                dist[vecin] = dist[nod] + cost
                parinte[vecin] = nod
                heapq.heappush(pq, (dist[vecin], vecin))
    
    return dist, parinte

# Functie pentru a reconstrui drumul minim
def reconstruiește_drum(parinte, destinatie):
    drum = []
    while destinatie is not None:
        drum.append(destinatie)
        destinatie = parinte[destinatie]
    return drum[::-1]

def citeste_input(fisier):
    # Citim datele din fisier
    with open(fisier, 'r') as f:
        # Citim nr de noduri si muchii
        noduri, muchii = map(int, f.readline().split())
        
        # Lista de adiacenta
        graf = {i: [] for i in range(1, noduri + 1)}
        
        # Citim muchiile
        for i in range(muchii):
            u, v, cost = map(int, f.readline().split())
            graf[u].append((v, cost))
            graf[v].append((u, cost))
            
        # Citim k puncte de control
        k = int(f.readline())
        puncte_control = list(map(int, f.readline().split()))
        
        # Citim varful de start s
        sursa = int(f.readline())
        
    return noduri, graf, puncte_control, sursa

def f(input):
    noduri, graf, puncte_control, sursa = citeste_input(input)
    
    # Aplicam algoritmul Dijkstra
    dist, parinte = dijkstra(noduri, graf, sursa)
    
    # Gasim cel mai apropiat punct de control
    dist_minima = float('inf')
    cel_mai_apropiat_punct = None
    for punct in puncte_control:
        if dist[punct] < dist_minima:
            dist_minima = dist[punct]
            cel_mai_apropiat_punct = punct
    
    # Reconstruim drumul minim
    drum = reconstruiește_drum(parinte, cel_mai_apropiat_punct)
    
    # Afisam output ul
    print(f"Cel mai apropiat punct de control de la {sursa} este {cel_mai_apropiat_punct}")
    print(" ".join(map(str, drum)))

f("grafpond2.in")
