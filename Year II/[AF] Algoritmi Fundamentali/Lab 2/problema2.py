from collections import deque

def find_course_rez(n, m, ordine):

    adiacenta = {i: [] for i in range(1, n + 1)} 
    in_degree = [0] * (n + 1) 
    
    for a, b in ordine:
        adiacenta[a].append(b) 
        in_degree[b] += 1  
    
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    rez = []
    while queue:
        course = queue.popleft()
        rez.append(course)
        for neighbor in adiacenta.get(course, []):
            in_degree[neighbor] -= 1  
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(rez) == n:
        order_str = ' '.join(str(course) for course in rez)
        print(order_str)
    else:
        print("IMPOSSIBLE")

with open("input_files/problema2.in", "r") as file:
    first_line = file.readline().strip().split()
    n = int(first_line[0])
    m = int(first_line[1])

    ordine = []
    for i in range(m):
        line = file.readline().strip().split()
        a = int(line[0])
        b = int(line[1])
        ordine.append((a, b))

find_course_rez(n, m, ordine)
