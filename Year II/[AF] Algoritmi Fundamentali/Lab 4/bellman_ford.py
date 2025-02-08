def citire_input(fisier):
    with open(fisier, 'r') as f:
        n, m = map(int, f.readline().split())  # Nr noduri si muchii
        muchii = []
        for i in range(m):
            u, v, c = map(int, f.readline().split())
            muchii.append((u, v, c))
        sursa = int(f.readline().strip())
    return n, m, muchii, sursa


def bellman_ford(fisier):
    # Citeste datele din fisier
    n, m, muchii, sursa = citire_input(fisier)

    # Initializeaza distantele si parintii pentru reconstructia drumurilor
    inf = float('inf')
    dist = [inf] * (n + 1)  # Initializeaza toate distantele cu infinit
    parent = [-1] * (n + 1)  # Vectorul de parinti pentru reconstructia drumului
    dist[sursa] = 0

    for i in range(n - 1):
        for u, v, c in muchii:
            if dist[u] != inf and dist[u] + c < dist[v]:
                dist[v] = dist[u] + c  # Actualizeaza distanta
                parent[v] = u  # Actualizeaza parintele

    # Verifica ciclu negativ
    for u, v, c in muchii:
        if dist[u] != inf and dist[u] + c < dist[v]:
            # Reconstruieste ciclul negativ
            ciclu = []
            visited = set()
            node = v
            while node not in visited:
                visited.add(node)
                node = parent[node]
            start = node
            ciclu.append(start)
            node = parent[start]
            while node != start:
                ciclu.append(node)
                node = parent[node]
            ciclu.append(start)
            ciclu.reverse()
            
            print("Circuit de cost negativ:")
            print(" ".join(map(str, ciclu)))
            return

    # Daca nu exista circuit negativ, afiseaza drumurile minime
    for i in range(1, n + 1):
        if i == sursa:
            continue
        if dist[i] == inf:
            continue  # Nod inaccesibil, nu afisam nimic
        drum = []
        curent = i
        # Reconstruieste drumul de la sursa la nodul curent
        while curent != -1:
            drum.append(curent)
            curent = parent[curent]
        drum.reverse()  # Drumul a fost construit invers
        print(f"Drum: {' '.join(map(str, drum))} Cost: {dist[i]}")

bellman_ford('grafpond5.in')
