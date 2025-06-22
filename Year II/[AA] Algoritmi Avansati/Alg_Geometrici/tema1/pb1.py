
n = int(input())
for _ in range(n):
    xp, yp, xq, yq, xr, yr = [int(x) for x in input().split()]
    
    det = xq * yr + xp * yq + xr * yp - yp * xq - xr * yq - xp * yr

    if det < 0:
        print("RIGHT")
    elif det > 0:
        print("LEFT")
    else:
        print("TOUCH")



