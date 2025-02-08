def dfs(nod, adiacenta, vizitat, parinte, ciclu):
    vizitat[nod] = True
    for vecin in adiacenta[nod]:
        if not vizitat[vecin]:
            parinte[vecin] = nod
            rez = dfs(vecin, adiacenta, vizitat, parinte, ciclu)
            if rez != -1:  
                return rez
        elif vecin != parinte[nod]: 
            ciclu.append(vecin)  
            ciclu.append(nod)  
            while parinte[nod] != vecin and parinte[nod] != -1:
                nod = parinte[nod]
                ciclu.append(nod)
            ciclu.append(vecin) 
            return ciclu
            
    return -1

f = open("input_files/dfs2.in", "r")
line = f.readline().strip()
n, m = [int(x) for x in line.split()]
adiacenta = [[] for i in range(n + 1)]

for i in range(m):
    line = f.readline().strip()
    x, y = [int(z) for z in line.split()]
    adiacenta[x].append(y)
    adiacenta[y].append(x)

f.close()

vizitat = [False] * (n + 1)
parinte = [-1] * (n + 1)
ciclu = []

for nod in range(1, n + 1):
    if not vizitat[nod]:
        rez = dfs(nod, adiacenta, vizitat, parinte, ciclu)
        if rez != -1:
            break

f = open("output_files/dfs2.out", "w")
if ciclu:
    for i in ciclu:
        f.write(str(i) + " ")
else:
    f.write("Nu exista\n")
f.close()
