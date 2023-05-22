import time


def somme_utilisation(L_valeurs, L_nb_pieces):
    somme = 0
    nb_pieces = 0
    for i in range(len(L_valeurs)):
        somme += L_valeurs[i] * L_nb_pieces[i]
        nb_pieces += L_nb_pieces[i]
    return somme, nb_pieces


def rendu_monnaie_brutforce(somme, L_valeurs):
    possibilites = [[]]  # liste des possibilités
    for i in range(len(L_valeurs)):
        possibilites_pieces_prec = possibilites.copy()
        possibilites = []
        for j in range(len(possibilites_pieces_prec)):
            s_obtenue, n = somme_utilisation(L_valeurs, possibilites_pieces_prec[j] + [0] * (len(L_valeurs) - i))
            s_min = 0
            s_max = (somme - s_obtenue) // L_valeurs[i]
            for s in range(s_min, 1 + s_max):
                L_nb_pieces = possibilites_pieces_prec[j].copy()
                L_nb_pieces.append(s)
                possibilites.append(L_nb_pieces)
    # recherche de la meilleure configuration
    # initialisation des paramètres de recherche
    L_nb_pieces_meilleur = []
    nb_pieces_min = -1
    # parcours de toutes les possibilités précédemment calculées
    for j in range(len(possibilites)):
        s, n = somme_utilisation(L_valeurs, possibilites[j])
        if s == somme and (nb_pieces_min == -1 or n < nb_pieces_min):
            L_nb_pieces_meilleur = possibilites[j]
            nb_pieces_min = n
    return L_nb_pieces_meilleur


syst_euros = [200, 100, 50, 20, 10, 5, 2, 1]
syst_euros_m1c = [200, 100, 50, 20, 10, 5, 2]
syst_euros_p25c = [200, 100, 50, 25, 20, 10, 5, 2, 1]


# L_valeurs : ordonné de la plus grande à la plus petite, version for
def rendu_monnaie_glouton(somme, L_valeurs):
    L_nb_pieces = []
    somme_restante = somme
    for i in range(len(L_valeurs)):
        nb_pieces_i = somme_restante // L_valeurs[i]
        # somme_restante = somme_restante - (nb_pieces_i * L_valeurs[i])
        somme_restante = somme_restante % L_valeurs[i]
        L_nb_pieces.append(nb_pieces_i)
    return L_nb_pieces


def glouton_vs_brutforce(somme, L_valeurs):
    t0 = time.process_time()
    L_nb_pieces_g = rendu_monnaie_glouton(somme, L_valeurs)
    t1 = time.process_time()
    L_nb_pieces_b = rendu_monnaie_brutforce(somme, L_valeurs)
    t2 = time.process_time()
    somme_g, nb_pieces_g = somme_utilisation(L_valeurs, L_nb_pieces_g)
    somme_b, nb_pieces_b = somme_utilisation(L_valeurs, L_nb_pieces_b)
    print("Obtenir", somme, "à partir de", L_valeurs)
    print("Sommes :", somme_g, "vs", somme_b)
    print("Nombre de pièces :", nb_pieces_g, "vs", nb_pieces_b)
    print("Temps d’exécution (s) :", t1 - t0, "secondes vs", t2 - t1, "secondes")
    print()


tests = [(0, syst_euros),
         (100, syst_euros),
         (98, syst_euros),
         (98, syst_euros_m1c),
         (90, syst_euros),
         (90, syst_euros_p25c),
         (200, syst_euros),
         (198, syst_euros),
         (198, syst_euros_m1c),
         (190, syst_euros),
         (190, syst_euros_p25c)]

print("Glouton vs Brutforce")
for somme, L_valeurs in tests:
    glouton_vs_brutforce(somme, L_valeurs)

"""
def rendu_monnaie(somme, L_valeurs):
    L_nb_pieces = []
    somme_restante = somme
    for i in range(len(L_valeurs)):
        val = somme_restante//L_valeurs[i]
        L_nb_pieces.append(val)
        somme_restante = somme_restante%L_valeurs[i]
    return L_nb_pieces


L_valeurs = [200, 100, 50, 25, 20, 10, 5, 2, 1]
print(rendu_monnaie(390, L_valeurs))
"""
