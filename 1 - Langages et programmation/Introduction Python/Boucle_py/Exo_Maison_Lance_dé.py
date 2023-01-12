from random import randint
from time import sleep

points_joueur1 = 0
points_joueur2 = 0
in_game = 1

while points_joueur1 != 5 and points_joueur2 != 5:
    question = input("Lancer le dé ? (Oui / Non) ")
    
    if question == "Non":
        in_game = 0
    
    sleep(0.5)
    de_joueur1 = randint(1, 6)
    de_joueur2 = randint(1, 6)
    print(f"Le jour 1 a obtenu {de_joueur1}. Le joueur 2 a obtenu {de_joueur2}.")
    
    sleep(0.5)
    if de_joueur1 < de_joueur2:
        points_joueur2 = points_joueur2+1
        print("Le joueur 2 a gagné, il remporte 1 point !")
    elif de_joueur1 == de_joueur2:
        print("Egalité, aucun point attribé !")
    else:
        points_joueur1 = points_joueur1+1
        print("Le joueur 1 a gagné, il remporte 1 point !")
    sleep(0.5)
    print(f"Le joueur 1 a {points_joueur1} points et le joueur 2 a {points_joueur2} points.")

if points_joueur1 < points_joueur2:
    print("Fin du jeu. Le joueur 2 a gagné !")
else:
    print("Fin du jeu. Le joueur 1 a gagné !")
