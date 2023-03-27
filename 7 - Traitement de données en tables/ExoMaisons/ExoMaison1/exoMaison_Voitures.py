# Règle pour avoir 1/1 sur les exos maison : réussir au moins un code demandé.
# Il y aura à chaque fois un code facile à faire.

from csv import reader

""" 
--- Code1* :
Créez un code permettant de compter le nombre de voitures dans le fichier voitures.csv codé en utf-8
Exemple :
    Entrée : L=[2,3,4,1]
    Sortie : L=[1,2,3,4]

--- Code2** :
Créez un code permettant de donner le type de chaque voiture du fichier voitures.csv codé en utf-8
On va considérer que :
    si Hauteur > 1597 : la voiture est de type SUV
    si Hauteur < 1353 : la voiture est de type sportive
    si 1353 <= Hauteur <= 1597 : la voiture est de type citadine
"""
nbr_cars = 0
with open('voitures.csv', 'r', encoding='utf-8') as file:
    car_list = list(reader(file, delimiter=','))
    for row in car_list[1:]:
        if int(row[1]) > 1597:
            print(f"{row[0]}: SUV")
        elif 1353 < int(row[1]) < 1597:
            print(f"{row[0]}: Citadine")
        elif 1353 > int(row[1]):
            print(f"{row[0]}: Sportive")
        nbr_cars += 1
print(nbr_cars)
