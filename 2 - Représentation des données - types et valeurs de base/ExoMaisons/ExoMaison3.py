in_game = True

base = int(input("Choisissez la base 2 ou 16:\n"))
nb_a_conv = input("Entrez un nombre en base 2 à convertir vers la base 10:\n")

if base == 2:
    nb_conv = int(nb_a_conv, 2)
elif base == 16:
    nb_conv = int(nb_a_conv, 16)

nb_joueur = int(input("Entrez le résultat de cette conversion:\n"))

while in_game:
    if nb_conv == nb_joueur:
        print("Bravo")
        in_game = False
    else:
        nb_joueur = int(input("Faux. Entrez un nouveau résultat de la conversion.\n"))
