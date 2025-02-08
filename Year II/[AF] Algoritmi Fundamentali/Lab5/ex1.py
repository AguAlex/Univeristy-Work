from collections import defaultdict, deque

# Reprezentarea rețelei
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)
        self.capacity = {}
        self.flow = {}

    # Adăugăm un arc între u și v
    def add_edge(self, u, v, cap, fl):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Arc invers
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0  # Capacitatea inversă este 0
        self.flow[(u, v)] = fl
        self.flow[(v, u)] = 0  # Fluxul invers este 0

    # Verificăm validitatea fluxului
    def check_flow(self, source, sink):
        # Verificăm constrângerea de mărginire
        for u in range(1, self.n + 1):
            for v in self.adj[u]:
                if self.flow[(u, v)] < 0 or self.flow[(u, v)] > self.capacity[(u, v)]:
                    return False

        # Verificăm conservarea fluxului
        for u in range(1, self.n + 1):
            if u != source and u != sink:
                in_flow = sum(self.flow[(v, u)] for v in self.adj[u])
                out_flow = sum(self.flow[(u, v)] for v in self.adj[u])
                if in_flow != out_flow:
                    return False
        return True

    # BFS pentru a găsi o cale augmentantă
    def bfs(self, source, sink, parent):
        visited = [False] * (self.n + 1)
        queue = deque([source])
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if not visited[v] and self.capacity[(u, v)] > self.flow[(u, v)]:
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
                    visited[v] = True
        return False

    # Algoritmul Ford-Fulkerson pentru flux maxim
    def ford_fulkerson(self, source, sink):
        total_flow = 0
        parent = [-1] * (self.n + 1)

        # Căutăm căi augmentante și actualizăm fluxul
        while self.bfs(source, sink, parent):
            # Găsim calea augmentantă
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)] - self.flow[(parent[s], s)])
                s = parent[s]

            # Actualizăm fluxurile pe calea găsită
            total_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.flow[(u, v)] += path_flow
                self.flow[(v, u)] -= path_flow
                v = parent[v]

        return total_flow

    # Calcularea tăieturii minime
    def min_cut(self, source):
        visited = [False] * (self.n + 1)
        queue = deque([source])
        visited[source] = True

        # Găsim toate nodurile accesibile din sursă
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if not visited[v] and self.capacity[(u, v)] > self.flow[(u, v)]:
                    visited[v] = True
                    queue.append(v)

        # Arcele care formează tăietura minimă
        min_cut_edges = []
        for u in range(1, self.n + 1):
            for v in self.adj[u]:
                if visited[u] and not visited[v] and self.capacity[(u, v)] > self.flow[(u, v)]:
                    min_cut_edges.append((u, v))

        return min_cut_edges

# Citirea datelor de intrare
n = 6
s = 1
t = 6
m = 8
edges = [
    (1, 3, 6, 3),
    (1, 5, 8, 2),
    (3, 2, 5, 0),
    (3, 4, 3, 3),
    (5, 4, 4, 2),
    (2, 6, 7, 0),
    (4, 6, 5, 5),
    (3, 5, 1, 0)
]

# Crearea graficului și adăugarea arcelor
graph = Graph(n)
for u, v, cap, fl in edges:
    graph.add_edge(u, v, cap, fl)

# Verificarea fluxului
if graph.check_flow(s, t):
    print("DA")
else:
    print("NU")

# Calcularea fluxului maxim
max_flow = graph.ford_fulkerson(s, t)
print(max_flow)

# Afișarea fluxului pe fiecare arc
for u in range(1, n + 1):
    for v in graph.adj[u]:
        if graph.flow[(u, v)] > 0:
            print(f"{u} {v} {graph.flow[(u, v)]}")

# Calcularea și afișarea tăieturii minime
min_cut_edges = graph.min_cut(s)
min_cut_capacity = sum(graph.capacity[(u, v)] for u, v in min_cut_edges)
print(min_cut_capacity)
for u, v in min_cut_edges:
    print(f"{u} {v}")
