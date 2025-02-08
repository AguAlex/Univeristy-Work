from collections import deque

def divide_into_teams(n, m, friendships):
    adiacenta = {}
    for a, b in friendships:
        if a not in adiacenta:
            adiacenta[a] = []
        if b not in adiacenta:
            adiacenta[b] = []
        adiacenta[a].append(b)
        adiacenta[b].append(a)
    
    teams = [0] * (n + 1)  
    
    def bfs(start):
        queue = deque([start])
        teams[start] = 1  
        while queue:
            node = queue.popleft()
            current_team = teams[node]
            next_team = 2 if current_team == 1 else 1
            for neighbor in adiacenta.get(node, []):
                if teams[neighbor] == 0:  
                    teams[neighbor] = next_team
                    queue.append(neighbor)
                elif teams[neighbor] == current_team:  
                    return False
        return True
    
    for i in range(1, n + 1):
        if teams[i] == 0 and i in adiacenta: 
            if not bfs(i):
                print("IMPOSSIBLE")
                return
    
    print(" ".join(str(c) for c in teams[1:]))

with open("input_files/problema1.in", "r") as file:
    aux = file.readline().strip().split()
    n = int(aux[0])
    m = int(aux[1])

    friendships = []
    for i in range(m):
        line = file.readline().strip().split()
        a = int(line[0])
        b = int(line[1])
        friendships.append((a, b))

divide_into_teams(n, m, friendships)
