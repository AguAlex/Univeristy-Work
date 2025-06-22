from itertools import combinations
from collections import defaultdict

def find_min_area_rectangles(ineq, points):
    vertical_lines = []
    horizontal_lines = []

    for a, b, c in ineq:
        if a != 0:
            x = -c / a
            vertical_lines.append(x)
        else:
            y = -c / b
            horizontal_lines.append(y)

    vertical_lines = sorted(set(vertical_lines))
    horizontal_lines = sorted(set(horizontal_lines))

    results = []
    for xq, yq in points:
        min_area = float('inf')
        ok = False
        for i in range(len(vertical_lines) - 1):
            for j in range(len(horizontal_lines) - 1):
                x1, x2 = vertical_lines[i], vertical_lines[i+1]
                y1, y2 = horizontal_lines[j], horizontal_lines[j+1]
                if x1 < xq < x2 and y1 < yq < y2:
                    ok = True
                    area = (x2 - x1) * (y2 - y1)
                    min_area = min(min_area, area)

        if ok:
            print("YES")
            print(f"{min_area:.6f}")
        else:
            print("NO")

    return results

ineq = []
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    ineq.append((a, b, c))

m = int(input())
points = []
for _ in range(m):
    x, y = map(float, input().split())
    points.append((x, y))

find_min_area_rectangles(ineq, points)
