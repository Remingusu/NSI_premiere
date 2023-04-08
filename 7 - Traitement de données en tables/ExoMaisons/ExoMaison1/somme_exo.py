from csv import reader

""" Code1* : 0,5 point
Créez un code pour que chaque valeur de la table devienne un élément de la liste L sauf la première ligne
Entrée : table.csv
Sortie : L=['Ada', '19', '10', '8', 'Grace', '7', '11', '15', 'Alan', '12', '12', '18', 'Bill', '8', '13', '12']
"""
with open('somme.csv', 'r') as file:
    liste = []
    first = True
    csv_read = reader(file, delimiter=';')
    for row in csv_read:
        if first:
            first = False
        else:
            liste.extend(row)
print(liste)

""" Code2** : 0,5 point
Créez un code qui donne la somme des notes de NSI à partir de la liste L précédente
Entrée : L
Sortie : 46
"""
somme = 0
i2 = 1
for i1 in range(len(liste)//4):
    somme += int(liste[i2])
    i2 += 4
print(somme)
