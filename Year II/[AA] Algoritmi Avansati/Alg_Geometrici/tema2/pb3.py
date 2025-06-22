#  Verificarea daca un poligon este monoton fata de o axa (x sau y).
def monoton(polygon, axa='x'):
    n = len(polygon)

    # Alegem indexul minim si maxim in fct de axa
    key = 0 if axa == 'x' else 1
    min_idx = max_idx = 0
    for i in range(1, n):
        if polygon[i][key] < polygon[min_idx][key]:
            min_idx = i
        if polygon[i][key] > polygon[max_idx][key]:
            max_idx = i

    # Lant de la min_idx la max_idx crescator
    i = min_idx
    ok1 = True
    while i != max_idx:
        next_i = (i + 1) % n
        if polygon[next_i][key] < polygon[i][key]:
            ok1 = False
            break
        i = next_i

    # Lant de la min_idx la max_idx descrescator
    i = min_idx
    ok2 = True
    while i != max_idx:
        prev_i = (i - 1 + n) % n
        if polygon[prev_i][key] < polygon[i][key]:
            ok2 = False
            break
        i = prev_i

    return ok1 and ok2

n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

print("YES" if monoton(polygon, 'x') else "NO")
print("YES" if monoton(polygon, 'y') else "NO")
