"""# init to dictionary
dicoProfs = {}
dicoProfs['NSI'] = "Turing"
dicoProfs['Maths'] = "Pythagore"
dicoProfs['Français'] = "Balzac"
print(dicoProfs)
print(dicoProfs['NSI'])

dicoProfs2 = {'SI': "Eiffel",
              'Phys': "Einstein",
              'Espagnol': "Dali"}
print(dicoProfs2)

#dicoProfs3=dict("Anglais"=" Shakespeare","EPS"="Bolt","H-G"="Michelet")
#print(dicoProfs3)

if "NSI" in dicoProfs.keys():
    print(True)
else:
    print(False)

if "NSI" in dicoProfs:
    print(True)
else:
    print(False)

if "Turing" in dicoProfs.values():
    print(True)
else:
    print(False)

for cle in dicoProfs.keys():
    print(cle)

for valeur in dicoProfs.values():
    print(valeur)

for cle, valeur in dicoProfs.items():
    print(cle, valeur)

del dicoProfs['NSI']
print(dicoProfs)

print(type(dicoProfs))"""

# Code 1
dicoEleves = {"e2022001": "Sophie",
              "e2022002": "Noé",
              "e2022003": "Léa",
              "e2022004": "Alex",
              "e2022005": "Manon"}


# Code 2
def ajouterEleve(dicoEleves, cle, nom):
    if cle in dicoEleves.keys():
        print(f"La clé spécifié est déjà présente pour {nom}")
    else:
        dicoEleves[cle] = nom
    return dicoEleves


# Code 3
def modifierEleve(dicoEleves, cle, nom):
    if cle in dicoEleves.keys():
        dicoEleves[cle] = nom
    else:
        print(f"La clé spécifié est absente ({cle})")
    return dicoEleves


# Code 4
def supprimerEleve(dicoEleves, cle):
    if cle not in dicoEleves.keys():
        print(f"La clé spécifié est absente ({cle})")
    else:
        print(f"{dicoEleves[cle]} supprimé")
        del dicoEleves[cle]
    return dicoEleves


# Code 5
def afficherCle(dicoEleves, nom):
    if nom not in dicoEleves.values():
        print(f"{nom} n'a pas de clé")
    else:
        for cle in dicoEleves:
            if nom == dicoEleves[cle]:
                print(nom, cle)


# Code 6
def supprimerHomonyme(dicoEleves, nom):
    i = 0
    for cle in dicoEleves:
        if nom == dicoEleves[cle]:
            print(nom, cle)
            i += 1

    if i == 0:
        print(f"{nom} n'est pas présent")
    elif i == 1:
        print(f"{nom} n'a pas d'homonyme")

    while i >= 2:
        cle = input(f"Quel {nom} voulez-vous supprimer ?\n")
        supprimerEleve(dicoEleves, cle)
        i -= 1
    return dicoEleves


loop = True
while loop:
    action = input("\nQue voulez-vous faire ?\n"
                   "1. Ajouter un élève\n"
                   "2. Modifier un élève\n"
                   "3. Supprimer un élève\n"
                   "4. Afficher la clé d'un élève\n"
                   "5. Supprimer un homonyme\n"
                   "6. Afficher la liste des élèves et leur clé\n"
                   "(Noter le numéro de l'action)\n")
    if action == '1':
        cle = input("Donnez la clé: ")
        nom = input("Donnez le nom lié à la clé: ")
        ajouterEleve(dicoEleves, cle, nom)
    elif action == '2':
        cle = input("Donnez la clé associer au nom à modifier: ")
        nom = input("Nouveau nom: ")
        modifierEleve(dicoEleves, cle, nom)
    elif action == '3':
        cle = input("Donnez la clé associer à l'élève à supprimer: ")
        supprimerEleve(dicoEleves, cle)
    elif action == '4':
        nom = input("Donnez le nom de l'élève: ")
        afficherCle(dicoEleves, nom)
    elif action == '5':
        nom = input("Nom de l'élève ayant (possiblement) un/des homonyme(s): ")
        supprimerHomonyme(dicoEleves, nom)
    elif action == '6':
        print(dicoEleves)
    else:
        loop = False
