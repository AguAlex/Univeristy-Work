f = open("date.in")
elevi = {}
n = int(f.readline())
for i in range(n):
    linie = f.readline()
    m = int(linie[-2])
    nume = linie[:-2] 
    materii = {}
    
    for j in range(m):
        linie = f.readline().strip().split(",")
        materie = linie[0]
        note = [int(x) for x in linie[1:]]
        materii[materie] = note

    elevi[nume.strip()] = materii


def detalii_elev(nume):
    aux = []
    for materie in elevi[nume]:
        medie = round(sum(elevi[nume][materie]) / len(elevi[nume][materie]), 2)
        if len(elevi[nume][materie]) == 1 or medie < 5:
               medie = 0

        aux.append((materie, medie))

    return sorted(aux, key=lambda x: x[0])
        

        

e = input("Nume Elev: ")
print(detalii_elev(e))
