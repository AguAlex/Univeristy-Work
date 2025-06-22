# Muchii legale
#import numpy as np

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

    rez = []
    for p in points:
        d = det4(A, B, C, p)
        if d > 0:
            rez.append("INSIDE")
        elif d == 0:
            rez.append("BOUNDARY")
        else:
            rez.append("OUTSIDE")
    return rez
    


def verificare_muchie_legala(P1, P2, P3, P4):
    # Muchia AC este diagonala triunghiului ABC, verificam daca D este in cercul lui ABC
    res1 = pozitie_cerc(P1, P2, P3, [P4])[0]
    # Muchia BD este diagonala triunghiului BCD, verificam daca A este in cercul lui BCD
    res2 = pozitie_cerc(P2, P3, P4, [P1])[0]
    
    AC_status = "ILLEGAL" if res1 == "INSIDE" else "LEGAL"
    BD_status = "ILLEGAL" if res2 == "INSIDE" else "LEGAL"
    
    print(f"AC: {AC_status}")
    print(f"BD: {BD_status}")

P1 = tuple(map(int, input().split()))
P2 = tuple(map(int, input().split()))
P3 = tuple(map(int, input().split()))
P4 = tuple(map(int, input().split()))

verificare_muchie_legala(P1, P2, P3, P4)
