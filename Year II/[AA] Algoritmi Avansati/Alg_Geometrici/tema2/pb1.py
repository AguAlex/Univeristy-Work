def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

# Verific daca r este pe segmentul [pq]
def on_segment(p, q, r):
    if orientation(p, q, r) != 0:
        return False
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])


def point_in_triangle(a, b, c, p):
    # Verific daca p e in triunghiul format de a, b si c
    o1 = orientation(a, b, p)
    o2 = orientation(b, c, p)
    o3 = orientation(c, a, p)
    
    if o1 == 0 and on_segment(a, p, b):
        return "BOUNDARY"
    if o2 == 0 and on_segment(b, p, c):
        return "BOUNDARY"
    if o3 == 0 and on_segment(c, p, a):
        return "BOUNDARY"
    
    if o1 > 0 and o2 > 0 and o3 > 0:
        return "INSIDE"
    if o1 < 0 and o2 < 0 and o3 < 0:
        return "INSIDE"
    
    return "OUTSIDE"

def verificare_punct(polygon, point):
    n = len(polygon)
    a = polygon[0]

    if orientation(a, polygon[1], point) < 0 or orientation(a, polygon[-1], point) > 0:
        return "OUTSIDE"

    # Impart poligonul in triunghuri
    left, right = 1, n - 1
    while right - left > 1:
        mid = (left + right) // 2
        if orientation(a, polygon[mid], point) >= 0:
            left = mid
        else:
            right = mid

    return point_in_triangle(a, polygon[left], polygon[(left + 1) % n], point)


n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
points = [tuple(map(int, input().split())) for _ in range(m)]


for point in points:
    print(verificare_punct(polygon, point))
