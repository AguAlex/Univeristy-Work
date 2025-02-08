from collections import deque

def bfs(n, s, adiacenta):
    distante = [-1] * (n + 1)
    distante[s] = 0
    coada = deque([s])
    
    while coada:
        nod = coada.popleft()
        for vecin in adiacenta[nod]:
            if distante[vecin] == -1:
                distante[vecin] = distante[nod] + 1
                coada.append(vecin)
    
    return distante

f = open("input_files/bfs.in")
linie = f.readline().split()
n = int(linie[0])
m = int(linie[1])
s = int(linie[2])
adiacenta = [[] for i in range(n + 1)]

for i in range(m):
    linie = f.readline().split()
    x = int(linie[0])
    y = int(linie[1])
    adiacenta[x].append(y)

f.close()
distante = bfs(n, s, adiacenta)

f = open("output_files/bfs.out", "w")
f.write(" ".join(str(dist) for dist in distante[1:]))
f.write("\n")
f.close()
