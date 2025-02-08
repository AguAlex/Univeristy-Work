s = [3, 11, 103, 1, 14, 99, 8]
l = len(s)-1


def heapify(s, i):
    global l
    left = 2*i + 1
    right = 2*i + 2

    if left <= l and s[left] > s[i]:
        maxim = left
    else:
        maxim = i

    if right <= l and s[right] > s[maxim]:
         maxim = right

    if maxim != i:
        s[maxim], s[i] = s[i], s[maxim]
        heapify(s, maxim)

        


def buildMax(s):
    global l
    for i in range(l//2, -1, -1):
        heapify(s, i)




def heapSort(s):
    global l
    buildMax(s)
    for i in range(len(s)-1, 0, -1):
        s[0], s[i] = s[i], s[0]
        l=l-1
        heapify(s, 0)

heapSort(s)
print(s)