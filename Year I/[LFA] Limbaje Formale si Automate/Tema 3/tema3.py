def citire_input():
    f = open("input.txt")
    stari = [x for x in f.readline().strip().split()]
    litere = [x for x in f.readline().strip().split()]
    litere_stiva = [x for x in f.readline().strip().split()]
    stare_initiala = f.readline().strip()
    stari_finale = [x for x in f.readline().strip().split()]
    numar_tranzitii = int(f.readline().strip())

    tranzitii = {x: [] for x in stari}
    for i in range(numar_tranzitii):
        aux = f.readline().strip().split("->")
        aux1 = aux[0].strip().split()
        aux2 = aux[1].strip().split()
        tranzitii[aux1[0]].append((aux1[1], aux1[2], aux2[0], aux2[1]))

    f.close()

    return stari, litere, litere_stiva, tranzitii, stare_initiala, stari_finale

stari, litere, litere_stiva, tranzitii, stare_initiala, stari_finale = citire_input()

def verificare(w):
    global stari_finale, stare_initiala, tranzitii
    stare_actuala = stare_initiala
    stack = ['Z']

    for symbol in w:
        if stare_actuala in tranzitii:
            for (lit, stack_top, urm_stare, modificare_stack) in tranzitii[stare_actuala]:
                if lit == symbol and stack[-1] == stack_top:
                    stare_actuala = urm_stare
                    if modificare_stack != '.':
                        stack.append(modificare_stack[0])  # Din XZ se adauga doar X
                    else:
                        stack.pop()
                    break
            else:
                return False  
        else:
            return False  

    return stare_actuala in stari_finale or (stack == ['Z'] or not stack)



cuvinte = ['aabb', "aaabb", "abbb"] 

for w in cuvinte:
    if verificare(w):
        print(f'Cuvantul {w} este acceptat.')
    else:
        print(f'Cuvantul {w} NU este acceptat.')
