listeBibliotheque = []


def creationLivre(auteur, titre, page, editeur):
    dicoLivre = {'Auteur': auteur,
                 'Titre': titre,
                 'Page': page,
                 'Editeur': editeur}
    return dicoLivre


def ajoutLivre(dicoLivre, listeBibliotheque):
    listeBibliotheque.append(dicoLivre)
    return listeBibliotheque


def afficherBibliotheque(listeBibliotheque):
    for i in range(len(listeBibliotheque)):
        livre = listeBibliotheque[i]
        print(f"####Livre {i+1}####")
        print(livre['Titre'] + " de " + livre['Auteur'])
        print("Edition " + livre['Editeur'] + ": " + str(livre['Page']) + " pages")


marche = True
while marche:
    action = input("\nQue voulez-vous faire ?\n"
                   "1. Créer un livre\n"
                   "2. Ajouter un livre\n"
                   "3. Afficher la bibliothèque\n"
                   "(Noter le numéro de l'action)\n")

    if action == '1':
        auteur = input("Donnez l'auteur: ")
        titre = input("Donnez le titre: ")
        pages = int(input("Donnez le nombre de page: "))
        editeur = input("Donnez l'éditeur: ")
        dicoLivre = creationLivre(auteur, titre, pages, editeur)
    elif action == '2':
        ajoutLivre(dicoLivre, listeBibliotheque)
    elif action == '3':
        afficherBibliotheque(listeBibliotheque)

    loop = True
    arret = input("Voulez-vous arrêter le logiciel ? o/n: ")

    while loop:
        arret = arret.lower()
        if arret == 'o':
            marche = False
            loop = False
        elif arret == 'n':
            loop = False
        else:
            arret = input("Entrez \'o\' ou \'n\': ")
