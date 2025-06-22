# Pct in cercul circumscris
import math
# import numpy as np

def pozitie_cerc(A, B, C, points):
    def det4(a, b, c, p):
        mat = [
            [a[0], a[1], a[0]**2 + a[1]**2, 1],
            [b[0], b[1], b[0]**2 + b[1]**2, 1],
            [c[0], c[1], c[0]**2 + c[1]**2, 1],
            [p[0], p[1], p[0]**2 + p[1]**2, 1]
        ]
        return round(
            mat[0][0]*(
                mat[1][1]*mat[2][2]*mat[3][3] + mat[1][2]*mat[2][3]*mat[3][1] + mat[1][3]*mat[2][1]*mat[3][2]
                - mat[1][3]*mat[2][2]*mat[3][1] - mat[1][1]*mat[2][3]*mat[3][2] - mat[1][2]*mat[2][1]*mat[3][3]
            )
            - mat[0][1]*(
                mat[1][0]*mat[2][2]*mat[3][3] + mat[1][2]*mat[2][3]*mat[3][0] + mat[1][3]*mat[2][0]*mat[3][2]
                - mat[1][3]*mat[2][2]*mat[3][0] - mat[1][0]*mat[2][3]*mat[3][2] - mat[1][2]*mat[2][0]*mat[3][3]
            )
            + mat[0][2]*(
                mat[1][0]*mat[2][1]*mat[3][3] + mat[1][1]*mat[2][3]*mat[3][0] + mat[1][3]*mat[2][0]*mat[3][1]
                - mat[1][3]*mat[2][1]*mat[3][0] - mat[1][0]*mat[2][3]*mat[3][1] - mat[1][1]*mat[2][0]*mat[3][3]
            )
            - mat[0][3]*(
                mat[1][0]*mat[2][1]*mat[3][2] + mat[1][1]*mat[2][2]*mat[3][0] + mat[1][2]*mat[2][0]*mat[3][1]
                - mat[1][2]*mat[2][1]*mat[3][0] - mat[1][0]*mat[2][2]*mat[3][1] - mat[1][1]*mat[2][0]*mat[3][2]
            )
        )

        # return np.linalg.det(mat)

    for p in points:
        d = det4(A, B, C, p)
        if d > 0:
            print("INSIDE")
        elif d == 0:
            print("BOUNDARY")
        else:
            print("OUTSIDE")
    

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

nr_pct = int(input())
points = []

for _ in range(nr_pct):
    p = tuple(map(int, input().split()))
    points.append(p)

pozitie_cerc(A, B, C, points)
