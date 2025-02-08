import numpy as np

def simulare(nr):
    nr_cazuri_fav = 0
    nr_test_pozitiv = 0

    for i in range(nr):
        bolnav = np.random.randint(1, 101)
        if bolnav > 98:
            bolnav = True
        else:
            bolnav = False

        if bolnav:
            test_pozitiv = np.random.randint(1, 101) <= 98
        else:
            test_pozitiv = np.random.randint(1, 101) > 95

        if test_pozitiv:
            nr_test_pozitiv += 1
            if bolnav:  
                nr_cazuri_fav += 1

    probabilitate = nr_cazuri_fav / nr_test_pozitiv
    return probabilitate

numar_simulari = 100000
probabilitate_test_pozitiv_bolnav = simulare(numar_simulari)
print(probabilitate_test_pozitiv_bolnav)
