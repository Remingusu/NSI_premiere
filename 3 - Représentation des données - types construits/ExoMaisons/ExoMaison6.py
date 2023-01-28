# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez un dictionnaire qui donne le nombre d'occurrences de chaque nombre présent dans la liste.
Vous pouvez utiliser count() et max()
Exemple :
Entrée : L=[3,2,7,1,3,3,4,5,6,3,7,2]
Sortie : D={0:0,1:1,2:2,3:4,4:1,5:1,6:1,7:2}
"""
L = [3, 2, 7, 1, 3, 3, 4, 5, 6, 3, 7, 2]
dico = {}
for i in range(max(L)+1):
    dico[i] = L.count(i)
print(dico)


""" Code2*** :
Comptage du nombre d occurrences maximum dans une liste non triée
Ne pas utiliser count()
Exemple :
Entrée : L=[3,2,7,1,3,3,4,5,6,3,7,2]
Sortie : il y en a 4 occurrences du nombre 3 dans la liste
"""
L = [3, 2, 7, 1, 3, 3, 4, 5, 6, 3, 7, 2]
max_occurrence = 0
occurrence = 0
for element in L:
    for i in range(len(L)):
        if element == L[i]:
            occurrence += 1
    if occurrence > max_occurrence:
        max_occurrence = occurrence
        max_element = element
    occurrence = 0
print(f"Il y a {max_occurrence} du nombre {max_element} dans la liste")
