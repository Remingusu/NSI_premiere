# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

""" Code1* :
Ecrivez un programme qui inverse les éléments d'une liste (sans utiliser une nouvelle liste).
Exemple :
Entrée : L = [5,6,7,8,9]
Sortie : L = [9,8,7,6,5]
"""
L = [5, 6, 7, 8, 9]
L.reverse()
print(L)

""" Code2** :
Ecrivez un programme qui inverse les éléments d'une liste (sans utiliser une nouvelle liste).
Vous n'utiliserez pas la méthode reverse().
Exemple :
Entrée : L = [5,6,7,8,9]
Sortie : L = [9,8,7,6,5]
"""
L = [5, 6, 7, 8, 9]
for i in range(len(L)):
    L.insert(i, L[-1])
    L.pop(-1)
print(L)
