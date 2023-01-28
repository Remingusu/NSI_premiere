def o_list():
    e_list = input("Entrez une suite de nombre séparé par un '?': ")
    e_list = e_list.split('?')
    for index in range(len(e_list)):
        e_list[index] = float(e_list[index])
    print(f"\nVoici votre liste: {e_list}")
    return e_list


o_list = o_list()
e_occur = float(input("\nEntrez un nombre, pour trouver le nombre d'occurrence dans la liste précédemment entrée: "))

"""
Code1* :
Comptage du nombre d'occurrences (répétitions) dans une liste non triée.
Ne pas utiliser count()
Exemple :
Entrées : L=[3?2?7?1?3?3?4?5?6?3?7?2] et 3
Sortie : 4
"""
i = 0
for element in o_list:
    if element == e_occur:
        i += 1
if i == 1:
    print(f"\n{i}", "occurrence inférieure à", e_occur, "trouvée")
else:
    print(f"\n{i}", "occurrences inférieures à", e_occur, "trouvées")


""" 
Code2* :
Comptage du nombre d'occurrences inférieures à l'occurrence choisie dans une liste non triée
Ne pas utiliser count()
Exemple :
Entrée : L=[3?2?7?1?3?3?4?5?6?3?7?2] et 4
Sortie : Il y a 7 occurrences inférieures à l'occurrence 4 dans la liste
"""

i = 0
for element in o_list:
    if element < e_occur:
        i += 1
if i == 1:
    print(f"\n{i}", "occurrence inférieure à", e_occur, "trouvée")
else:
    print(f"\n{i}", "occurrences inférieures à", e_occur, "trouvées")
