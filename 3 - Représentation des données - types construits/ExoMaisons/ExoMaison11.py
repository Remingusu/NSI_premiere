""" Code1* : 0,5 point
Créez un code permettant d'insérer le dernier élément d'une liste au début de la liste
Exemple :
    Entrée : L=[2,3,4,1]
    Sortie : L=[1,2,3,4]
"""
L = [2, 3, 4, 1]
L.insert(0, L[-1])
L.pop(-1)
print(L)

""" Code2** : 0,5 point
Créez un code permettant de permuter le dernier élément d'une liste avec le premier élément de la liste
Exemple :
    Entrée : L=[2,3,4,1]
    Sortie : L=[1,3,4,2]
"""
L = [2, 3, 4, 1]
val_temp = L[-1]
L.insert(-1, L[0])
L.pop(0)
L.insert(0, val_temp)
L.pop(-1)
print(L)
