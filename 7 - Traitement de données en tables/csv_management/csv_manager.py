from csv import reader, writer
from operator import itemgetter


def import_table(fichier):
    liste = []
    dico = {}
    with open(fichier, 'r') as csv_open:
        csv_read = reader(csv_open, delimiter=';')
        for row in csv_read:
            liste.append(row)
    for i in range(len(liste[0])):
        dico[liste[0][i]] = []
        for row in liste[1:]:
            dico[liste[0][i]].append(row[i])
    return dico


def recherche_eleves(fichier, note_ref, cours):
    l_noms_eleves = []
    dico = import_table(fichier)
    for note in dico[cours]:
        if float(note) >= note_ref:
            l_noms_eleves.append(dico['Nom'][dico[cours].index(note)])
    return l_noms_eleves


def table_liste(fichier):
    liste = []
    with open(fichier, 'r') as csv_open:
        csv_read = reader(csv_open, delimiter=';')
        for row in csv_read:
            liste.append(row)
    for row in liste:
        for element in row:
            if element.isdigit():
                row[row.index(element)] = int(element)
    return liste


def tri_nsi(liste):
    liste = sorted(liste[1:], key=itemgetter(1))
    return liste


def creation_csv(fichier, liste):
    with open(fichier, 'w', newline='') as file:
        ligne = writer(file, delimiter=';')
        ligne.writerow(['Nom', 'NSI', 'Maths', 'Français'])
        for row in liste:
            ligne.writerow(row)


def supprimer_doublon(liste):
    for row in liste:
        if liste.count(row) > 1:
            liste.remove(row)
    return liste


def supprimer_doublon2(liste):
    l = liste[1:]
    i_del = None
    noms = []
    for row in l:
        noms.append(row[0])
    for i in range(len(noms)):
        if noms.count(noms[i]) > 1:
            i_del = i
    l.remove(l[i_del])
    return l


note = 10
cours = 'NSI'
print(f"Eleves avec une note supérieur à {note} en {cours}: {recherche_eleves('table.csv', note, cours)}")
creation_csv('table_tri.csv', tri_nsi(table_liste('table.csv')))
creation_csv('table_sans_doublons.csv', supprimer_doublon(table_liste('table_avec_doublons.csv')))
creation_csv('table_sans_doublons2.csv', supprimer_doublon2(table_liste('table_avec_doublons2.csv')))
