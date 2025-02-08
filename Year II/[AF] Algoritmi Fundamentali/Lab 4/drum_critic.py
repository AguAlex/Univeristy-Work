from collections import deque

# Functie pentru citirea datelor din fisierul de intrare
def citeste_fisier_intrare(f):
    with open(f, 'r') as f:
        numar_activitati = int(f.readline().strip())
        durate = list(map(int, f.readline().strip().split()))
        numar_dependente = int(f.readline().strip())
        dependente = [tuple(map(int, f.readline().strip().split())) for i in range(numar_dependente)]
    return numar_activitati, durate, dependente

# Functie pentru calcularea timpului minim si identificarea activitatilor critice
def drum_critic(numar_activitati, durate, dependente):
    # Initializare grafului de dependente si gradului de intrare al fiecarui nod
    graf = [[] for i in range(numar_activitati + 1)]
    grad_intrare = [0] * (numar_activitati + 1)
    for i, j in dependente:
        graf[i].append(j)  # Activitatea i trebuie sa se termine inainte ca j sa inceapa
        grad_intrare[j] += 1  # Incrementam gradul de intrare pentru nodul j

    # Sortare topologica folosind o coada
    ordine_topologica = []
    coada = deque([i for i in range(1, numar_activitati + 1) if grad_intrare[i] == 0])  # Noduri fara dependente
    while coada:
        nod = coada.popleft()
        ordine_topologica.append(nod)  # Adăugăm nodul în ordinea topologica
        for vecin in graf[nod]:
            grad_intrare[vecin] -= 1  # Reducem gradul de intrare pentru vecinii nodului
            if grad_intrare[vecin] == 0:  # Daca gradul de intrare devine 0, il adaugam în coada
                coada.append(vecin)

    # Calcularea timpilor de inceput cel mai devreme pentru fiecare activitate
    inceput_devreme = [0] * (numar_activitati + 1)
    for nod in ordine_topologica:
        for vecin in graf[nod]:
            # Timpul cel mai devreme cand poate incepe vecinul este actualizat
            inceput_devreme[vecin] = max(inceput_devreme[vecin], inceput_devreme[nod] + durate[nod - 1])

    # Calcularea timpilor de inceput cel mai tarziu pentru fiecare activitate
    durata_proiect = max(inceput_devreme[i] + durate[i - 1] for i in range(1, numar_activitati + 1))
    inceput_tarziu = [durata_proiect] * (numar_activitati + 1)
    for nod in reversed(ordine_topologica):
        for vecin in graf[nod]:
            # Actualizam timpul cel mai tarziu cand nodul poate incepe fara intarziere
            inceput_tarziu[nod] = min(inceput_tarziu[nod], inceput_tarziu[vecin] - durate[nod - 1])

    # Identificarea activitatilor critice
    activitati_critice = []
    for i in range(1, numar_activitati + 1):
        # Activitatea este critica daca timpul cel mai devreme si cel mai tarziu coincid
        if inceput_devreme[i] == inceput_tarziu[i]:
            activitati_critice.append(i)

    # Calcularea intervalelor pentru fiecare activitate
    intervale = [(inceput_devreme[i], inceput_devreme[i] + durate[i - 1]) for i in range(1, numar_activitati + 1)]

    return durata_proiect, activitati_critice, intervale

# Functie pentru afisarea rezultatelor
def output(durata_proiect, activitati_critice, intervale):
    print(f"Timp minim: {durata_proiect}")
    print(f"Activitati critice: {' '.join(map(str, activitati_critice))}")
    for i, interval in enumerate(intervale, start=1):
        # Afisam intervalele posibile de desfasurare pentru fiecare activitate
        print(f"{i}: {interval[0]} {interval[1]}")

# Citim datele din fisierul de intrare
numar_activitati, durate, dependente = citeste_fisier_intrare('activitati.in')

# Calculam durata proiectului, activitatile critice si intervalele
durata_proiect, activitati_critice, intervale = drum_critic(numar_activitati, durate, dependente)

# Afisam rezultatele
output(durata_proiect, activitati_critice, intervale)
