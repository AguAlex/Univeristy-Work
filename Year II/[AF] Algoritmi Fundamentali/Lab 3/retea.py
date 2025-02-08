import heapq
import math

# Functie pentru prelucrarea inputului
def citire_input():
    f = open("retea.in")
    n, m = map(int, f.readline().split())
    
    # Citim coordonatele centralelor
    centrale = []
    for i in range(n):
        x, y = map(int, f.readline().split())
        centrale.append((x, y))
    
    # Citim coordonatele blocurilor
    blocuri = []
    for i in range(m):
        x, y = map(int, f.readline().split())
        blocuri.append((x, y))
    
    f.close()
    return n, m, centrale, blocuri

# Functie pentru distanta
def distanta(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n, m, centrale, blocuri = citire_input()

# Se foloseste algoritmul lui Prim
min_heap = []
vizitat = [False] * (n + m)  # Marcare pentru nodurile vizitate (centrale si blocuri)
cost_total = 0.0

# Adaugam toate centralele in heap ca puncte de pornire
for i in range(n):
    vizitat[i] = True
    for j in range(n, n + m):
        cost = distanta(centrale[i], blocuri[j - n])
        heapq.heappush(min_heap, (cost, i, j))

while min_heap and any(not vizitat[n + i] for i in range(m)):
    cost, c, b = heapq.heappop(min_heap)
    if vizitat[b]:
        continue
    vizitat[b] = True
    cost_total += cost
    
    # Extindem la blocuri nevizitate
    if b >= n:  # Dacă v este un bloc
        for j in range(n, n + m):
            if not vizitat[j]:
                cost = distanta(blocuri[b - n], blocuri[j - n])
                heapq.heappush(min_heap, (cost, b, j))

print(cost_total)
