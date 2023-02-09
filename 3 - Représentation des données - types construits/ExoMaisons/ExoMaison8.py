# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez un dictionnaire qui donne le nombre d'occurrences de chaque nombre présent dans la liste.
Vous pouvez utiliser count() et max()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
"""
L = [7, 3, 2, 6, 7, 3, 0, 3, 3, 5, 2, 6, 7, 2, 0]
dico = {}
for i in range(max(L)+1):
    dico[i] = L.count(i)
print("Dico code 1:", dico)


""" Code2** :
Comptage du nombre d occurrences maximum dans le dictionnaire du code1
Ne pas utiliser count()
Exemple :
Entrée : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
Sortie : il y en a 4 occurrences du nombre 3 dans la liste
"""
max_value = 0
key_of_max = 0
for key, value in dico.items():
    if value > max_value:
        key_of_max = key
        max_value = value

print(f"(Code 2) Il y a {max_value} occurrences du nombre {key_of_max} dans la liste")


""" Code3** : = code1 sans utiliser count() et max()
Créez un dictionnaire qui donne le nombre d'occurrences de chaque nombre présent dans la liste.
Vous ne pouvez pas utiliser count() et max()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : D={0:2,1:0,2:3,3:4,4:0,5:1,6:2,7:3}
"""
L = [7, 3, 2, 6, 7, 3, 0, 3, 3, 5, 2, 6, 7, 2, 0]
dico = {}
occur = 0
for i in L:
    for j in L:
        if i == j:
            occur += 1
    dico[i] = occur
    occur = 0
print("Dico code 3:", dico)


""" Code4*** :
Comptage du nombre d occurrences maximum dans une liste non triée
Ne pas utiliser count()
Exemple :
Entrée : L=[7,3,2,6,7,3,0,3,3,5,2,6,7,2,0]
Sortie : il y en a 4 occurrences du nombre 3 dans la liste
"""
L_code4 = [7, 3, 2, 6, 7, 3, 0, 3, 3, 5, 2, 6, 7, 2, 0]
dico_code4 = {}
occur_code4 = 0
for i in L_code4:
    for j in L_code4:
        if i == j:
            occur_code4 += 1
    dico_code4[i] = occur_code4
    occur_code4 = 0

max_value_code4 = 0
key_of_max_code4 = 0
for key, value in dico_code4.items():
    if value > max_value_code4:
        key_of_max_code4 = key
        max_value_code4 = value

print(f"(Code 4) Il y a {max_value_code4} occurrences du nombre {key_of_max_code4} dans la liste")