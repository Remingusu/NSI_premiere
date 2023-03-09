# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé. Il y aura à chaque fois un code facile à faire.

""" Code1* :
Créez le code qui permet de trier une liste du plus grand au plus petit
Vous pouvez utiliser la méthode sort()
https://docs.python.org/3/library/stdtypes.html#list.sort
Exemple :
    Entrée : L=[1,7,9,8,1,10,3,5,6,9]
    Sortie : L=[10,9,9,8,7,6,5,3,1,1]
"""
L=[1,7,9,8,1,10,3,5,6,9]
L.sort(reverse=True)
print(L)


""" Code2** :
Créez le code qui permet de ne garder que la moitié d'une liste triée
Vous pouvez utiliser la méthode sort()
Exemple :
    Entrée : L=[1,7,9,8,1,10,3,5,6,9]
    Sortie : L=[1,1,3,5,6]
"""
L=[1,7,9,8,1,10,3,5,6,9]
L.sort()
for i in range(len(L)//2):
    L.pop(-1)
print(L)

