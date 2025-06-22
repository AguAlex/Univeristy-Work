# ordonare descrescatoare dupa valoare / greutate
rez = 0
obiecte = []

nr_obiecte, GMax = map(int, input().split())

# (greutate, valoare)
for _ in range(nr_obiecte):
    greutate, valoare = map(int, input().split())
    obiecte.append((greutate, valoare, valoare / greutate))

# Sortare descrescatoare dupa valoare / greutate
obiecte.sort(key=lambda x: x[2], reverse=True)

greutate_curenta = 0
cnt_obiect = 0

while cnt_obiect < nr_obiecte and greutate_curenta < GMax:
    greutate, valoare, eficienta = obiecte[cnt_obiect]

    if greutate_curenta + greutate <= GMax:
        # Daca incape complet
        greutate_curenta += greutate
        rez += valoare
    else:
        # Daca nu incape complet
        rest = GMax - greutate_curenta
        rez += eficienta * rest
        greutate_curenta += rest
        break

    cnt_obiect += 1

print(rez)
