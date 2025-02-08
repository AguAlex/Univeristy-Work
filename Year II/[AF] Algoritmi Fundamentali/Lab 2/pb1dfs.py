
def dfs(nod, adiacenta, vizitat):
    vizitat[nod] = True
    for vecin in adiacenta[nod]:
        if not vizitat[vecin]:
            dfs(vecin, adiacenta, vizitat)


f = open("input_files/dfs1.in", "r")
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
numar_componente = 0

for nod in range(1, n + 1):
    if not vizitat[nod]:
        dfs(nod, adiacenta, vizitat)
        numar_componente += 1

f = open("output_files/dfs1.out", "w")
f.write(str(numar_componente) + "\n")
f.close()
