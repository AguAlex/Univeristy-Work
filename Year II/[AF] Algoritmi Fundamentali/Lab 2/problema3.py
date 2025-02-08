def count_rooms(n, m, building_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        while stack:
            current_x, current_y = stack.pop()
            for dx, dy in directions:
                new_x, new_y = current_x + dx, current_y + dy
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and building_map[new_x][new_y] == '.':
                    visited[new_x][new_y] = True
                    stack.append((new_x, new_y))

    
    visited = [[False] * m for i in range(n)]
    room_count = 0

    for i in range(n):
        for j in range(m):
            if building_map[i][j] == '.' and not visited[i][j]:
                dfs(i, j)
                room_count += 1

    return room_count


with open("input_files/problema3.in", "r") as file:
    first_line = file.readline().strip().split()
    n = int(first_line[0])
    m = int(first_line[1])

    building_map = []
    for i in range(n):
        line = file.readline().strip()  
        building_map.append(line)

print(count_rooms(n, m, building_map))
