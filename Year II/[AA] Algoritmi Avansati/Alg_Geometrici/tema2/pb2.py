#  Algoritmul ray-casting (numarare intersectii cu o raza trasa de la punct spre infinit).

def on_segment(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def point_position(polygon, point):
    x, y = point
    cnt = 0
    n = len(polygon)

    # Pentru fiecare latura a poligonului, verific interesctia
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]

        # Verific daca punctul e pe o muchie a poligonului
        if orientation(a, point, b) == 0 and on_segment(a, point, b):
            return "BOUNDARY"

        xi, yi = a
        xj, yj = b

        # Verific daca segmentul [a,b] intersecteaza o linie orizontala trasa la nivelul lui y
        if (yi > y) != (yj > y):
            x_int = xi + (y - yi) * (xj - xi) / (yj - yi)  # Intersectia razei cu segmentul
            if x < x_int:  # Daca punctul este la stanga intersectiei, cresc contorul
                cnt += 1

    # Daca numarul de intersectii este impar, punctul e in interior, altfel e in afara
    return "INSIDE" if cnt % 2 == 1 else "OUTSIDE"


n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
points = [tuple(map(int, input().split())) for _ in range(m)]

for pt in points:
    print(point_position(polygon, pt))
