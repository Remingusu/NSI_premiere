# Créé par LEWEEN.MASSIN, le 23/03/2023 en Python 3.7

from csv import reader as read


file = '49-prenoms-2013-22.csv'
name = 'Aaron'
gender = 'F'
year = 2019


def import_table(file):
    l=[]
    with open(file, 'r') as csv_open:
        csv_read = read(csv_open, delimiter=';')
        for row in csv_read:
            l.append(row)
    return l


def easier_table(file):
    l = import_table(file)
    l.pop(0)
    for row in l:
        for i in range(2):
            row.pop(0)
    return l


def nbr_enfants(file, name):
    l = easier_table(file)
    nbr = 0
    for row in l:
        if row[1] == name:
            nbr+=int(row[2])
    return nbr


def nbr_gender(file, gender, year):
    l = easier_table(file)
    occur = 0
    for row in l:
        if row[0] == gender and int(row[3]) == year:
            occur += 1
    return occur


print(f"{name}: {nbr_enfants(file, name)}")
print(f"{gender} en {year}: {nbr_gender(file, gender, year)}")
