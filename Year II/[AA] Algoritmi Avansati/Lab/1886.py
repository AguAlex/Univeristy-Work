# ordonare descrescatoare dupa valoare
rez = 0
obiecte = []

# Citim numarul de obiecte si capacitatea maxima a rucsacului
nr_obiecte, GMax = map(int, input().split())

# Citim obiectele (greutate, valoare)
for _ in range(nr_obiecte):
    greutate, valoare = map(int, input().split())
    obiecte.append((greutate, valoare, valoare / greutate))

# Sortare descrescatoare dupa valoare, apoi greutate
obiecte.sort(key=lambda x: (-x[1], x[0])) 
