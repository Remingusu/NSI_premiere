"""
Coder un programme réalisant la multiplication de 2 entiers n1 et n2
Ne pas utiliser les opérateurs : *, / et abs()
Aide : 3x4=3+3+3+3
Exemple :
Si n1=3 et n2=4 --> résulat=12
Si n1=3 et n2=-4 --> résulat=-12
Si n1=-3 et n2=4 --> résulat=-12
Si n1=-3 et n2=-4 --> résulat=12
"""
n1 = float(input("Donnez le premier nombre de la multiplication: "))
n2 = int(input("Donnez le deuxième nombre de la multiplication (nombre entier positif): "))
produit = 0
for i in range(n2):
    produit = produit+n1
print(produit)
