# Se construieste frontiera inferioara a acoperirii convexe
def calc_viraj(xp, yp, xq, yq, xr, yr):
    det = xq * yr + xp * yq + xr * yp - yp * xq - xr * yq - xp * yr

    if det < 0:
        return "RIGHT"
    elif det > 0:
        return "LEFT"
    else:
        return "TOUCH"

n = int(input())
puncte = []
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    puncte.append((x, y))

frontiera_inferioara = [(puncte[0][0], puncte [0][1]), (puncte[1][0], puncte[1][1])]

for i in range(2, n):
    frontiera_inferioara.append((puncte[i][0], puncte[i][1]))
    while len(frontiera_inferioara) > 2 and calc_viraj(frontiera_inferioara[-3][0], frontiera_inferioara[-3][1], frontiera_inferioara[-2][0], frontiera_inferioara[-2][1], frontiera_inferioara[-1][0], frontiera_inferioara[-1][1]) != "LEFT":
        frontiera_inferioara.pop(-2)

while len(frontiera_inferioara) > 2 and calc_viraj( frontiera_inferioara[-2][0], frontiera_inferioara[-2][1], frontiera_inferioara[-1][0], frontiera_inferioara[-1][1], puncte[0][0], puncte[0][1]) != "LEFT":
        frontiera_inferioara.pop(-1)

if len(frontiera_inferioara) > 2 and calc_viraj( frontiera_inferioara[-1][0], frontiera_inferioara[-1][1], puncte[0][0], puncte[0][1], puncte[1][0], puncte[1][1]) != "LEFT":
        frontiera_inferioara.pop(0)

print(len(frontiera_inferioara))
for pct in frontiera_inferioara:
     print(pct[0], pct[1])
