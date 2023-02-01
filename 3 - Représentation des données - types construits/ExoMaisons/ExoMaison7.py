# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez une liste à partir du dictionnaire du nombre d'occurrence de chaque chiffre présent dans la liste.
Vous pouvez utiliser count() et max()
Exemple :
Entrée : D={0:0,1:1,2:2,3:4,4:1,5:1,6:1,7:2}
Sortie : L=[1,2,2,3,3,3,3,4,5,6,7,7]
"""
D = {0: 0, 1: 1, 2: 2, 3: 4, 4: 1, 5: 1, 6: 1, 7: 2}
L = []
for key in D.keys():
    for i in range(D[key]):
        L.append(key)
print(L)


""" Code2** :
Comptage du nombre de chiffres qui se répètent dans une liste triée
Ne pas utiliser count()
L non triée = [1,4,9,3,6,3,2,5,6,3,7,8,3]
L triée     = [1,2,3,3,3,3,4,5,6,6,7,8,9]
Entrée : L=[1,2,3,3,3,3,4,5,6,6,7,8,9]
Sortie : 6 (car il y a 4 "3" + 2 "6" = 6)
"""
L = [1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9]
D = {}
occur = 0
output = 0

for val in L:
    for val2 in L:
        if val == val2:
            occur += 1
    if occur > 1:
        D[val] = occur
    occur = 0

for val in D.values():
    output += val

print(output)
