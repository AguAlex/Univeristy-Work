# Viraje in poligon
n = int(input())
stanga, dreapta, nimic = 0, 0, 0

xp, yp = [int(x) for x in input().split()]
xstart, ystart = xp, yp
xq, yq = [int(x) for x in input().split()]
for _ in range(n - 2):
    xr, yr = [int(x) for x in input().split()]
    
    det = xq * yr + xp * yq + xr * yp - yp * xq - xr * yq - xp * yr

    if det < 0:
        dreapta += 1
    elif det > 0:
        stanga += 1
    else:
        nimic += 1

    xp, yp = xq, yq
    xq, yq = xr, yr

xr, yr = xstart, ystart
det = xq * yr + xp * yq + xr * yp - yp * xq - xr * yq - xp * yr

if det < 0:
    dreapta += 1
elif det > 0:
    stanga += 1
else:
    nimic += 1

    
print(stanga, dreapta, nimic)



