import math
import numpy

R = 1
r = R/2

def genereaza_mijloc():
    unghi1 = numpy.random.rand() * 2 * math.pi
    unghi2 = numpy.random.rand() * 2 * math.pi

    P1 = (R * math.cos(unghi1), R * math.sin(unghi1))
    P2 = (R * math.cos(unghi2), R * math.sin(unghi2))

    return (P1, P2)

def distanta_centru_mijloc(M):
    
    distanta = math.sqrt(M[0]**2 + M[1]**2)
    
    return distanta

def estimeaza_probabilitatea(nr_simulari):
    contor_intersectii = 0
    
    for i in range(nr_simulari):
        M = genereaza_mijloc()
        
        distanta = distanta_centru_mijloc(M)
        
        if distanta < r:
            contor_intersectii += 1
    
    probabilitate = contor_intersectii / nr_simulari
    return probabilitate

nr_simulari = 1000000

probabilitate = estimeaza_probabilitatea(nr_simulari)
print(probabilitate)


