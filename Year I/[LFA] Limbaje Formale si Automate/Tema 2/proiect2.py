#Functie pentru prelucrarea datelor de intrare, se face un dictionar

def dict_productii():

    f = open('input.txt')

    L1 = []
    L2 = []

    for linie in f:
        aux = linie.split("->")
        L1.append(aux[0].strip())
        L2.append([x.strip() for x in aux[1].split("|")])

    productii = {L1[i]: L2[i] for i in range(len(L1))}

    
        
    f.close()
    return productii

productii = dict_productii()

#Functie de verificare daca cuvant apartine gramaticii expriamte prin dictionarul productii
def verificare(productii, symbol_curent, cuvant_curent, cuvant):
    
    # Verificăm dacă cuvântul curent este egal cu cuvântul cautat
    if cuvant_curent == cuvant and symbol_curent == '':
        return True
    
    # Dacă lungimea curentă a cuvântului depășește lungimea cuvântului cautat, oprim căutarea
    if len(cuvant_curent) > len(cuvant):
        return False

    # Explorăm toate produsele simbolului curent din gramatică
    if symbol_curent in productii:
        for productie in productii[symbol_curent]:
            cuvant_aux = cuvant_curent
            symboluri = []
            for symbol in productie:
                #Verific daca e terminal
                if symbol.islower():
                    cuvant_aux += symbol
                else:
                    symboluri.append(symbol)

            # Dacă nu sunt simboluri non-terminale, verificăm direct cuvântul
            if not symboluri and cuvant_aux == cuvant:
                return True
            # Continuăm generarea recursiv pentru următoarele simboluri
            for symbol in symboluri:
                if verificare(productii, symbol, cuvant_aux, cuvant):
                    return True
                    
    return False

#Aflam toate symbolurile terminale intr-o lista "terminal"
terminal = []
for prod in productii:
    for productie in productii[prod]:
        for symbol in productie:
            if symbol not in terminal and symbol.islower():
                terminal.append(symbol)


n = int(input("n = "))

#Se genereaza toate cuvintele de lungime n posibile
def generare(L, n):

    #Caz de baza
    if n == 0:
        return ['']
    
    #Recursivitatea
    rez = []
    for i in range(len(L)):
        litera_curenta = L[i]
        for perm in generare(L, n-1):
            rez.append(litera_curenta + perm)
    
    return rez

cuvinte = generare(terminal, n)

for p in cuvinte:
    if verificare(productii, 'S', '', p):
        print(p)


# aacbb da
# abb da
# aa nu
# abc nu
