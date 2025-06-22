
import math
def intersectie_semiplane(inegalitati):
    INF = float("inf")
    x_min, x_max = -INF, INF
    y_min, y_max = -INF, INF

    for a, b, c in inegalitati:
        if a != 0:
            # Semiplan vertical
            x_bound = -c / a
            if a > 0:
                x_max = min(x_max, x_bound)
            else:
                x_min = max(x_min, x_bound)
        elif b != 0:
            # Semiplan orizontal
            y_bound = -c / b
            if b > 0:
                y_max = min(y_max, y_bound)
            else:
                y_min = max(y_min, y_bound)

    if x_min > x_max or y_min > y_max:
        print("VOID")
    elif math.isfinite(x_min) and math.isfinite(x_max) and math.isfinite(y_min) and math.isfinite(y_max):
        print("BOUNDED")
    else:
        print("UNBOUNDED")

n = int(input())
inegalitati = []
for _ in range(n):
    inegalitati.append(tuple(map(int, input().split())))

intersectie_semiplane(inegalitati)
