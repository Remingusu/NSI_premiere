from random import randint # importe la fonction randint

print("Vous devez deviner un nombre entre 1 et 100.") # affichage

nb_ordi = randint(1,100) # choisis un nombre aléatoire entre 1 et 100
nb_essais=0 # met le nombre d'essais à 0.
nb_utilisateur="" # met nb_utilisateur à rien pour éviter une erreur avec la boucle

while nb_utilisateur!=nb_ordi and nb_essais!=10: # tant que nb_utilisateur est différent du nb_ordi et que le nb_essais n'est pas 10 alors:
    nb_utilisateur = int(input("Proposez un nombre en 1 et 100 ")) # demande à l'utilisateur un nombre
    if nb_ordi==nb_utilisateur: # si c'est vrai:
        print("Bravo, vous avez faits", nb_essais, "essais.") # afficher nombre d'essais (sort de la boucle)
    elif nb_ordi<nb_utilisateur: # sinon si le nb_ordi est inférieur au nb_utilisateur alors:
        print("C'est moins.") # affichage
    else: # sinon:
        print("C'est plus.") # affichage
    nb_essais=nb_essais+1 # ajoute un au nombre d'essais si le nombre n'est pas trouvé (si 10 essais sort de la boucle)

if nb_essais==10: # si le nombre d'essais est égale à 10:
    print(f"Vous avez épuisé votre nombre d'essais. Le nombre était {nb_ordi}") # afficher nombre à trouver