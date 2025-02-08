import math

def floyd_warshall(numar_noduri, muchii):
    # Initiem matricea distantelor cu infinit
    distante = [[math.inf] * (numar_noduri + 1) for i in range(numar_noduri + 1)]
    # Matrice pentru pastrarea traseului pentru reconstructia drumului
    urmator = [[None] * (numar_noduri + 1) for i in range(numar_noduri + 1)]

    # Setam distantele initiale pe baza muchiilor
    for i in range(1, numar_noduri + 1):
        distante[i][i] = 0
    for sursa, destinatie, cost in muchii:
        distante[sursa][destinatie] = cost
        urmator[sursa][destinatie] = destinatie

    # Algoritmul Floyd-Warshall pentru calculul distantelor minime
    for nod_intermediar in range(1, numar_noduri + 1):
        for sursa in range(1, numar_noduri + 1):
            for destinatie in range(1, numar_noduri + 1):
                if distante[sursa][nod_intermediar] != math.inf and distante[nod_intermediar][destinatie] != math.inf:
                    if distante[sursa][destinatie] > distante[sursa][nod_intermediar] + distante[nod_intermediar][destinatie]:
                        distante[sursa][destinatie] = distante[sursa][nod_intermediar] + distante[nod_intermediar][destinatie]
                        urmator[sursa][destinatie] = urmator[sursa][nod_intermediar]

    # Detectam circuitele cu cost negativ
    for nod in range(1, numar_noduri + 1):
        if distante[nod][nod] < 0:  # Daca distanta de la un nod la el insusi devine negativa
            circuit_negativ = reconstruieste_circuit(urmator, nod)
            return None, circuit_negativ

    return distante, None

def reconstruieste_circuit(urmator, nod_start):
    """
    Reconstruim un circuit cu cost negativ utilizand matricea 'urmator'.
    """
    vizitat = [False] * len(urmator)
    circuit = []

    # Gasim un nod din circuit
    nod_curent = nod_start
    while not vizitat[nod_curent]:
        vizitat[nod_curent] = True
        nod_curent = urmator[nod_curent][nod_curent]

    # Reconstruim circuitul
    nod_start_circuit = nod_curent
    circuit.append(nod_start_circuit)
    nod_curent = urmator[nod_start_circuit][nod_start_circuit]

    while nod_curent != nod_start_circuit:
        circuit.append(nod_curent)
        nod_curent = urmator[nod_curent][nod_curent]
    circuit.append(nod_start_circuit)

    return circuit

def rezolvare(f):
    # Citim datele din fisier
    with open(f, 'r') as f:
        numar_noduri, numar_muchii = map(int, f.readline().strip().split())
        muchii = [tuple(map(int, f.readline().strip().split())) for i in range(numar_muchii)]

    # Aplicam algoritmul Floyd-Warshall
    matrice_distantelor, circuit_negativ = floyd_warshall(numar_noduri, muchii)

    # Afisam rezultatele pe ecran
    if circuit_negativ:
        print("Circuit de cost negativ:")
        print(" ".join(map(str, circuit_negativ)))
    else:
        print("Matricea distantelor minime:")
        for i in range(1, numar_noduri + 1):
            print(" ".join(str(int(x)) if x != math.inf else "0" for x in matrice_distantelor[i][1:numar_noduri + 1]))

rezolvare("grafpond6.in")
