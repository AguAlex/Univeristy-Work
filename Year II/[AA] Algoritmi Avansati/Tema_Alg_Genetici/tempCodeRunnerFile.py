import random
import numpy as np

def functie(x, a, b, c):
    return a * x**2 + b * x + c

def initializare_populatie(dimensiune, domeniu, precizie):
    numar_valori = int((domeniu[1] - domeniu[0]) * 10**precizie)
    return [random.randint(0, numar_valori) for _ in range(dimensiune)]

def decodeaza(cromozom, domeniu, precizie):
    numar_valori = int((domeniu[1] - domeniu[0]) * 10**precizie)
    return domeniu[0] + cromozom * (domeniu[1] - domeniu[0]) / numar_valori

def fitness(populatie, a, b, c, domeniu, precizie):
    return [functie(decodeaza(cr, domeniu, precizie), a, b, c) for cr in populatie]

def selectie_ruleta(populatie, fit):
    suma_fitness = sum(fit)
    probabilitati = [f / suma_fitness for f in fit]
    probabilitati_cumulate = np.cumsum(probabilitati)
    selectie = []
    for _ in range(len(populatie)):
        r = random.random()
        index = np.searchsorted(probabilitati_cumulate, r)
        selectie.append(populatie[index])
    return selectie, probabilitati, probabilitati_cumulate

def crossover(populatie, prob_crossover):
    random.shuffle(populatie)
    combinatii = []
    for i in range(0, len(populatie) - 1, 2):
        if random.random() < prob_crossover:
            punct_taiere = random.randint(1, len(bin(max(populatie))) - 2)

            lungime_cromozom = len(bin(max(populatie))) - 2
            binar1 = format(populatie[i], f'0{lungime_cromozom}b')
            binar2 = format(populatie[i+1], f'0{lungime_cromozom}b')

            copil1_bin = (binar1[:punct_taiere] + binar2[punct_taiere:]).zfill(lungime_cromozom)
            copil2_bin = (binar2[:punct_taiere] + binar1[punct_taiere:]).zfill(lungime_cromozom)

            copil1 = int(copil1_bin, 2)
            copil2 = int(copil2_bin, 2)

            populatie[i], populatie[i+1] = copil1, copil2
            combinatii.append((binar1, binar2, copil1_bin, copil2_bin))
    return populatie, combinatii


def mutatie(populatie, prob_mutatie):
    mutatii = []
    populatie_initiala = populatie[:]
    for i in range(len(populatie)):
        if random.random() < prob_mutatie:
            bit = 1 << random.randint(0, len(bin(max(populatie))) - 2)
            cromozom_initial = format(populatie[i], '020b')
            populatie[i] ^= bit
            cromozom_final = format(populatie[i], '020b')
            mutatii.append((i, cromozom_initial, bit, cromozom_final))
    return populatie, mutatii

def algoritm_genetic(dimensiune, domeniu, precizie, a, b, c, prob_crossover, prob_mutatie, etape):
    populatie = initializare_populatie(dimensiune, domeniu, precizie)
    max_fitness_evolutie = []
    
    with open("Evolutie.txt", "w") as f:
        for etapa in range(etape):
            fit = fitness(populatie, a, b, c, domeniu, precizie)
            populatie, probabilitati, probabilitati_cumulate = selectie_ruleta(populatie, fit)
            
            if etapa == 0:
                f.write("Populatia initiala:\n")
                for i, c in enumerate(populatie):
                    x = decodeaza(c, domeniu, precizie)
                    f.write(f"Individ {i+1}: Cromozom={format(c, '020b')} X={x:.6f} f(X)={fit[i]}\n")
                
                f.write("\nProbabilitati selectie:\n")
                for i, prob in enumerate(probabilitati):
                    f.write(f"Cromozom {i + 1}: {str(prob)}\n")

                f.write("\nIntervale selectie:\n")
                f.write(str(probabilitati_cumulate) + "\n")

                f.write("\nPopulatia dupa selectie:\n")
                for i, c in enumerate(populatie):
                    x = decodeaza(c, domeniu, precizie)
                    f.write(f"Individ {i+1}: Cromozom={format(c, '020b')} X={x:.6f} f(X)={functie(x, a, b, c)}\n")
                
                populatie, combinatii = crossover(populatie, prob_crossover)
                f.write("\nCombinatii dupa crossover:\n")
                for c in combinatii:
                    f.write(str(c) + "\n")
                
                populatie, mutatii = mutatie(populatie, prob_mutatie)
                f.write("\nCromozomi mutati:\n")
                for mut in mutatii:
                    f.write(f"Individ {mut[0]+1}: Initial={mut[1]}, Bit Modificat={mut[2]}, Final={mut[3]}\n")
                
            
            max_fitness = max(fit)
            mean_fitness = sum(fit) / len(fit)
            max_fitness_evolutie.append(max_fitness)
            
            f.write(f"\nEtapa {etapa+1} - Max Fitness: {max_fitness}, Mean Fitness: {mean_fitness}")
    
    return max_fitness_evolutie

dimensiune_populatie = 20
domeniu_definitie = (-1, 2)
precizie = 6
coef_a, coef_b, coef_c = (-1, 1, 2)
prob_crossover = 0.25
prob_mutatie = 0.01
numar_etape = 50

evolutie_max = algoritm_genetic(dimensiune_populatie, domeniu_definitie, precizie, coef_a, coef_b, coef_c, prob_crossover, prob_mutatie, numar_etape)

