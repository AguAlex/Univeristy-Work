f = open("txt.in")

date = {}
linie = f.readline()
while linie != "":
    if "Destinatie" in linie:
        aux = linie.split(":")[1].strip()
        date[aux] = []
        dest = aux
    else:
        aux = linie.split()
        nota = aux[-1]
        stele = aux[-3]
        nume = " ".join(aux[0:-3])
        date[dest].append((nume, int(stele), float(nota)))
    linie = f.readline()


def recomandari(date, *orase, nr_stele_min=0, scor_min=0):
    rez = []
    for oras in orase:
        if oras in date:
            L = []
            for dest in date[oras]:
                if dest[1] >= nr_stele_min and dest[2] >= scor_min:
                    L.append((dest[0], dest[1]))
            
            if len(L):
                rez.append((oras, L))

    L=[]
    for i in rez:
        L.append((i[0], sorted(i[1], key=lambda x: -x[1])))
    
    
    L = sorted(L, key=lambda x: (-len(x[1]), x[0]))
    rez = [(x[0], [y[0] for y in x[1]]) for x in L]
    return rez

def act_recenzii(date, nume_oras, nume_unitate):
    m = set()
    valmax = 0
    for i in date[nume_oras]:
        if i[0] in nume_unitate:
            i[2] = (i[2] + nume_unitate[i[0]]) // 2
            if i[2] > valmax:
                valmax = i[2]
    
    for i in date[nume_oras]:
        if i[2] == valmax:
            m.add(i[0])
    return m, valmax



    
nume_oras = "Busteni"
nume_unitate = {
"Hotel Mare": 10
}
print(date)
print(act_recenzii(date, nume_oras, nume_unitate))
