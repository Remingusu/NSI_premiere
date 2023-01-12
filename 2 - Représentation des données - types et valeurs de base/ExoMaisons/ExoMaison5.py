# Créez un programme de 2 lignes permettant l'affichage suivant : a b c d e f g h i j k l m n o p q r s t u v w x y z
# Aide : for i in range(4,8): i ira de i=4 à i=8-1=7
# Aide : print("toto",end=' ') : l'affichage sera toto suivi d'un espace

for i in range(0, 26):
    print(chr(97+i), end=' ')
