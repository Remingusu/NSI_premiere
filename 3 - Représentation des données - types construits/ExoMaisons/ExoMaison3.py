# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

"""
Code 1 :
Créez la liste L_match_2=['Samira', 'Laura', 'Lucie']
la liste L_match_2 sera créée à partir de la liste L_match_1 dont vous remplacerez Léa par Laura
vous pourrez utiliser copy()
"""
def code1():
    L_match_1 = ["Samira", "Léa", "Lucie"]
    L_match_2 = [n for n in L_match_1]
    for i in range(L_match_2.count("Léa")):
        i_lea = L_match_2.index("Léa")
        L_match_2[i_lea] = "Laura"
    print("Code 1:", L_match_2)


"""
Code 2 :
Créez le dictionnaire D_match_2={'joueuse1': 'Samira', 'Joueuse2': 'Laura', 'Joueuse3': 'Lucie'}
le dico D_match_2 sera créé à partir du dico D_match_1 dont vous remplacerez Léa par Laura
vous pourrez utiliser copy()
"""
def code2():
    D_match_1 = {"Joueuse 1": "Samira", "Joueuse 2": "Léa", "Joueuse 3": "Lucie"}
    D_match_2 = {}
    i = 0
    for value in D_match_1.values():
        i += 1
        if value == "Léa":
            D_match_2[f"Joueuse {i}"] = "Laura"
        else:
            D_match_2[f"Joueuse {i}"] = value
    print("Code 2:", D_match_2)


"""
Code 3 :
Quel est l'instruction permettant d'afficher "Mbappé" depuis le dictionnaire dicoProfs ?
"""
def code3():
    dicoProfs = {"SI": "Eiffel", "Phys": " Einstein", "Espagnol": "Dali", "Anglais": "Shakespeare",
                 "EPS": ["Bolt", "Mbappé"], "H-G": "Michelet"}
    print("Code 3:", dicoProfs["EPS"][1])


"""
Code 4 :
Écrivez un code qui crée la liste suivante : [[1, 2], [2, 2], [3, 2], ... [9, 2]]
"""
def code4():
    L = []
    for i in range(1, 10):
        L.append([i, 2])
    print(L)


"""
Code 5 :
Écrivez un code qui crée la liste suivante par compréhension : [[1, 2], [2, 2], [3, 2], ... [9, 2]]
"""
def code5():
    L = [[i, 2] for i in range(1, 10)]
    print(L)


"""
Code 6 :
Écrivez un code qui créé la liste L suivante à partir des listes L1 et L2 de même taille : 
L=[0,1,2,'d','e','f','g','h','i','j']
"""
def code6():
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    L = []
    i = 0
    for value in L2:
        if L1[i] < 3:
            L.append(L1[i])
        else:
            L.append(value)
        i += 1
    print(L)


"""
Code 7 :
Écrivez un code qui créé la liste L suivante par compréhension à partir des listes L1 et L2 de même taille : 
L=[0,1,2,'d','e','f','g','h','i','j']
"""
def code7():
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    L = [L1[i] if i < 3 else L2[i] for i in range(len(L2))]
    print(L)

def code7_AI():
    """
    J'ai trouvé le code 7 difficile.
    Après avoir fini le code 7, j'ai pris votre consigne et l'ai inscrite dans le 'Chat OPEN AI' (chat.openai.com).
    Je vous propose également de le faire, car cette IA explique comment s'exécute le code.
    Voilà le code qu'il m'a donné :
    """
    L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    L = [x if i < 3 else y for i, (x, y) in enumerate(zip(L1, L2))]
    print(L)


# Code principal:
loop = True
while loop:
    dicoCode = {1: code1,
                2: code2,
                3: code3,
                4: code4,
                5: code5,
                6: code6,
                7: code7,
                7.5: code7_AI}

    for i in range(1, 8):
        print(f"{i}. Code {i}")

    print(f"7.5. Code 7 AI")
    number = float(input("Choisissez le code à afficher en entrant son numéro: "))
    dicoCode[number]()

    check = True
    while check:
        run = input("Continuer ? o/n\n")
        run = run.lower()
        if run == 'o':
            check = False
        elif run == 'n':
            check = False
            loop = False
