#q - stare curenta, w - cuvantul de verificat
def delta_tilda(q, w):
    global tranzitii
    if len(w) == 0:
        return {q}
    else:
        stari_noi = set()
        for tranzitie in tranzitii[str(q)]:
            aux = tranzitie[1]
            if tranzitie[0] == w[0]:
                stari_noi = stari_noi | delta_tilda(int(aux), w[1:])
        return stari_noi

# tranzitii = {
#     1: [(a, ...), (b, ...)],
#     2: [(a, ...), (b, ...)],
#     etc.
# }

f = open('input.txt')
g = open("output.txt", "w")
numar_stari = f.readline().strip()
stari = [int(x) for x in f.readline().strip().split()]

numar_litere = f.readline().strip()
litere = [x for x in f.readline().strip().split()]

stare_initiala = int(f.readline().strip())

numar_stari_finale = int(f.readline().strip())
stari_finale = [int(x) for x in f.readline().strip().split()]

numar_tranzitii = int(f.readline().strip())
tranzitii = {str(x):[] for x in stari}
for i in range(numar_tranzitii):
    aux = f.readline().strip().split()
    tranzitii[aux[0]].append((aux[1], int(aux[2])))

numar_cuvinte = int(f.readline().strip())
for i in range(numar_cuvinte):
    cuvant = f.readline().strip()
    stari_aux = delta_tilda(stare_initiala, cuvant)
    validat = False
    for i in stari_finale:
        if i in stari_aux:
            validat = True
            break
    if validat == True:
        g.write("DA" + "\n")
    else:
        g.write("NU" + "\n")
f.close()
g.close()

