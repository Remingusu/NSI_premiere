# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

"""Code1* :
Comptage du nombre d'occurrences supérieures à l'occurrence choisie dans une liste non trièe
Ne pas utiliser count()
Exemple :
Entrée : L=[3,2,7,1,3,3,4,5,6,3,7,2] et 3
Sortie : Il y a 7 occurrences supérieures à l'occurrence 5 dans la liste
"""
"""
L = [3, 2, 7, 1, 3, 3, 4, 5, 6, 3, 7, 2]
nbr = int(input("Entrez un nombre pour compter son nombre d'occurrence: "))
i = 0

for value in L:
    if value > nbr:
        i += 1
print(f"Il y a {i} occurrences supérieures au nombre {nbr} dans la liste.")"""

"""Code2** :
Comptage du nombre d'occurrences (nombres égaux) dans une liste triée
Ne pas utiliser count()
Exemple :
Entrée : L=[1,2,3,4,5,5,5,6,7]
Sortie : 3
On ne se mettra pas dans la situation où il y a plusieurs valeurs identiques, ex : L=[1,2,3,3,3,3,4,5,5,6,7]
"""
L = [1, 2, 3, 4, 5, 5, 5, 6, 7]
occur = 0
t_occur = 0

for i in range(len(L)):
    for j in range(len(L)):
        if L[i] == L[j]:
            occur += 1
    if occur > 1:
        t_occur = occur
    occur = 0

if t_occur == 0:
    print("Il n'y a pas de nombre avec occurrence")
else:
    print(f"Il y a {t_occur} occurrences.")
