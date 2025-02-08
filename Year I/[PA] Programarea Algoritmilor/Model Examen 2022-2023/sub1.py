f = open("text.in")

dict = {}
dictfrecv = {}
for linie in f:
    aux = linie.split()
    for cuv in aux:
        cuv = cuv.strip(",.").lower()
        if cuv not in dict:
            dict[cuv] = 1
        else:
            dict[cuv] += 1

for i in dict:
    if dict[i] not in dictfrecv:
        dictfrecv[dict[i]] = [i]
    else:
        dictfrecv[dict[i]].append(i)

f.close()
keys = list(dictfrecv.keys())
keys.sort(reverse=True)
dict = {i : dictfrecv[i] for i in keys}

for i in dict:
    dict[i].sort()

f = open("text.out", "w")


for i in dict:
    f.write(f"Frecventa {i}" + "\n")
    for j in dict[i]:
        f.write(j + "\n")

print(dict)