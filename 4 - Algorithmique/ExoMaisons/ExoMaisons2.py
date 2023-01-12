# Ecrivez un programme qui inverse les éléments d'une liste L1 dans une nouvelle liste L2
# vous n'utiliserez pas la méthode reverse().
# Exemple :
# Entrée : L1 = [5,6,7,8,9]
# Sortie : L2 = [9,8,7,6,5]

L1=[5,6,7,8,9]
L2=[L1[-i] for i in range(1, len(L1)+1)]

# Ecrivez un programme qui inverse les éléments d'une liste L (sans utiliser une nouvelle liste).
# vous n'utiliserez pas la méthode reverse().
# Exemple :
# Entrée : L = [5,6,7,8,9]
# Sortie : L = [9,8,7,6,5]

L=[5,6,7,8,9]
L=[L[-i] for i in range(1, len(L)+1)]
