# Ensembles de codes qui ne fonctionnent pas : mission dépannage

'''
# Code 2
nb1 = int(input("Donner le 1er nombre: "))
nb2 = int(input("Donner le 2ème nombre: "))
addi_2nb = 0
while addi_2nb != nb1+nb2:
    addi_2nb = int(input("Donner l'addition de ces 2 nombres "))
    if addi_2nb == nb1+nb2:
        print("Bravo tu as réussis l'addition")
    elif addi_2nb != nb1+nb2:
        print("Essaye encore")
'''
'''
# Code 2
nb1 = int(input("Donner le 1er nombre: "))
nb2 = int(input("Donner le 2eme nombre: "))
d_rslt = 0
while d_rslt != (nb1+nb2):
    d_rslt = int(input("Donner le produit de " + str(nb1) + " et " + str(nb2) + " = "))
    if d_rslt != (nb1+nb2):
        print("Essais encore")
    else:
        print("Bravo !")
'''
'''
# Code3
nb1 = int(input("Donner le 1er nombre: "))
nb2 = int(input("Donner le 2ème nombre: "))
resultat = nb1 + nb2
rep_j = ""
nb_essais = 0
while rep_j != resultat and nb_essais != 5:
    rep_j = int(input(f"Donner le résultat de {nb1} + {nb2} "))
    if rep_j != resultat:
        print("Essaye encore !")
        nb_essais = nb_essais+1
if nb_essais <= 5:
    print("Dommage, les 5 essais sont passés")
else:
    print("Bravo, tu as réussi en", nb_essais, "essais !")
'''
'''
# Code3
nb1 = int(input("Donner le 1er nombre: "))
nb2 = int(input("Donner le 2eme nombre: "))
somme_j = ""
essais = 0
while essais != 5 and somme_j != nb1+nb2:
    somme_j = int(input("Donner le produit des deux: "))
    if somme_j != nb1+nb2:
        print("Essaie à nouveau")
        essais = essais+1
if essais < 5:
    print("Bravo tu as réussi en", essais, "essais")
else:
    print("Dommage les", essais, "essais sont passés")
'''
'''
# Code3
nb1 = int(input("Donner le 1er nombre "))
nb2 = int(input("Donner le 2eme nombre "))
nb3 = nb1+nb2
nb4 = ""
nb_essais = 0
while nb3 != nb4 and nb_essais != 5:
    nb4 = int(input("Donner la somme de ces 2 nombres "))
    if nb3 != nb4:
        print("Essais encore")
        nb_essais = nb_essais+1
if nb_essais == 5:
    print("Dommage, les ", nb_essais, "essais sont passés")
else:
    print("Bravo, tu as réussi en", nb_essais, "essais !")
'''
'''
# Code3
nb1 = int(input("Donner le 1er nombre... "))
nb2 = int(input("Donner le 2eme nombre... "))
resultat = nb1+nb2
nb_essais = 0
resultat_joueur = ""
while (resultat_joueur != resultat) and (nb_essais != 5):
    resultat_joueur = int(input("Donner le somme des 2 nombres... "))
    if resultat_joueur != resultat:
        print("Mauvaise réponse, retente ta chance")
        nb_essais = nb_essais + 1
if resultat_joueur == resultat:
    print("Bravo, tu as réussi en", nb_essais, "essais")
else:
    print("Tu as dépassé le nombre d'essais autorisés")
'''
'''
# Code3
nb1 = int(input("Donner le premier nombre: "))
nb2 = int(input("Donner le second nombre: "))
solution = int(input("Donner la somme de ces 2 nombres de tête: "))
essais = 0
while solution != nb1+nb2 and essais != 5:
    if solution != nb1+nb2:
        solution = int(input("Essayez à nouveau: "))
        essais = essais + 1
if essais < 5:
    print("Bravo tu as réussi en", essais, "essais !")
else:
    print("Dommage, les", essais, "essais sont passés")
'''