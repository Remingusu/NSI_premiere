from random import randint

def master_dur(L_couleurs):
    L_master=[]
    for i in range (4):
        couleur=randint(0,5)
        L_master.append(L_couleurs[couleur])
    return(L_master)

def master_facile(L_couleurs):
    L_couleurs_cop = L_couleurs.copy()
    L_master=[]
    for i in range (4):
        couleur=randint(0, len(L_couleurs_cop)-1)
        L_master.append(L_couleurs_cop[couleur])
        L_couleurs_cop.remove(L_couleurs_cop[couleur])
    return(L_master)

def joueur(L_couleurs):
    L_joueur = []
    for i in range(4):
        lettre = input("Entrez une lettre entre A et F compris: ")
        lettre = lettre.lower()
        lettre=chr(ord(lettre)-32)
        L_joueur.append(lettre)

    for i in range(len(L_joueur)):
        while L_couleurs.count(L_joueur[i]) == 0:
            print(L_joueur[i],"n'est pas une couleur du jeu changez là.")
            lettre = input("Nouvelle couleur: ").lower()
            L_joueur[i] = chr(ord(lettre)-32)
    return (L_joueur)

def bien_et_mal_places(L_master, L_joueur):
    L_master_cop=L_master.copy()
    L_joueur_cop=L_joueur.copy()
    nb_mal_places=0
    i_joueur=0
    for inc in range(4):
        loop=True
        i_master=0
        while loop and i_master!=len(L_master_cop):
            if L_joueur_cop[i_joueur] == L_master_cop[i_master]:
                loop=False
                nb_mal_places+=1
                L_joueur_cop.pop(i_joueur)
                L_master_cop.pop(i_master)
            i_master+=1
        if loop==True:
            i_joueur+=1

    L_master_cop_2=L_master.copy()
    L_joueur_cop_2=L_joueur.copy()
    nb_bien_places=0
    for i in range(len(L_master_cop_2)):
        if L_master_cop_2[i] == L_joueur_cop_2[i]:
            nb_bien_places+=1
            L_joueur_cop_2[i]=0
            nb_mal_places-=1
    nb_bien_mal_places=[nb_mal_places, nb_bien_places]
    return nb_bien_mal_places


L_couleurs=['A', 'B', 'C', 'D', 'E', 'F']

master_type = input("Master Dur ou Facile: ").lower()
while master_type!="dur" and master_type!="facile":
    master_type = input("Master Dur ou Facile").lower()

if master_type == "dur":
    L_master = master_dur(L_couleurs)
elif master_type == "facile":
    L_master = master_facile(L_couleurs)

result = [0, 0]
essais = 0
while result[1] != 4:
    L_joueur = joueur(L_couleurs)
    result = bien_et_mal_places(L_master, L_joueur)
    print(f"Bien placés: {result[1]}\nMal placés: {result[0]}")
    essais+=1

if result[1] == 4:
    print(f"Bravo !\nVous avez réussi en {essais} essais.")
