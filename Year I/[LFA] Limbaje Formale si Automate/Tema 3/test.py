def citire_input():
    with open("input_tema1.txt") as f:
        stari = f.readline().strip().split()
        litere = f.readline().strip().split()
        litere_stiva = f.readline().strip().split()
        stare_initiala = f.readline().strip()
        stari_finale = f.readline().strip().split()
        numar_tranzitii = int(f.readline().strip())

        tranzitii = {}
        for _ in range(numar_tranzitii):
            tranzitie = f.readline().strip().split()
            stare_curenta, litera_citita, simbol_stiva, stare_urmatoare, simbol_nou_stiva = tranzitie
            if stare_curenta not in tranzitii:
                tranzitii[stare_curenta] = []
            tranzitii[stare_curenta].append((litera_citita, simbol_stiva, stare_urmatoare, simbol_nou_stiva))

    return stari, litere, litere_stiva, tranzitii, stare_initiala, stari_finale

def verificare(w):
    global stari_finale, stare_initiala, tranzitii
    stare_actuala = stare_initiala
    stack = ['Z']

    def tranziție(lit, stack_top, urm_stare, modificare_stack):
        nonlocal stare_actuala, stack
        if (lit == symbol or lit == '.') and stack[-1] == stack_top:
            stare_actuala = urm_stare
            if modificare_stack != '.':
                stack.pop()
                if modificare_stack != '.':
                    stack.extend(modificare_stack[::-1])
            else:
                stack.pop()
            return True
        return False

    for symbol in w:
        if stare_actuala in tranzitii:
            tranzitie_gasita = False
            for (lit, stack_top, urm_stare, modificare_stack) in tranzitii[stare_actuala]:
                if tranziție(lit, stack_top, urm_stare, modificare_stack):
                    tranzitie_gasita = True
                    break
            if not tranzitie_gasita:
                return False
        else:
            return False

    return stare_actuala in stari_finale and (stack == ['Z'] or not stack)

# Citirea datelor de intrare
stari, litere, litere_stiva, tranzitii, stare_initiala, stari_finale = citire_input()

# Cuvintele de verificat
cuvinte = ["abb", "cbba", "abba"] 

# Verificarea cuvintelor
for w in cuvinte:
    if verificare(w):
        print(f'Cuvântul {w} este acceptat.')
    else:
        print(f'Cuvântul {w} NU este acceptat.')
