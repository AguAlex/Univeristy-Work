def citire_lista(fisier):
    f = open(fisier)
    m = int(f.readline())
    M = []
    lista_aux = []
    for pereche in f:
        aux = [int(x) for x in pereche.split()]
        nr = aux[0]
        cateori = aux[1]
        while cateori > 0:
            if len(lista_aux) == m:
                M.append(lista_aux)
                lista_aux = []
            else:
                lista_aux.append(nr)
                cateori -= 1
    if len(lista_aux) < m:
        M.append(lista_aux)
    f.close()
    while len(M[-1]) < m:
        M[-1].append(0)
    return M
    
def prelucrare_liste(M, poz): 
    M = [row[:poz] + row[poz+1:] for row in M ]
    M = [M[i] for i in range(len(M)) if M[i].count(M[i][0]) != len(M[i])]
    return M

k = int(input("k="))
m = 5
x = 2
M = citire_lista("date.in")
rez = []
for i in M:
    for j in i:
        if j % k == 0 and j % (k**2) != 0:
            rez.append(j)

rez = set(rez)

f = open("rez.out", "w")

if len(rez) == 0:
    print("Imposibil!")
else:
    for i in sorted(rez, reverse=True):
        f.write(str(i) + "\n")
