def import_table(fichier):
    L=[]
    f=open(fichier,'r')
    for ligne in f:
        ligne=ligne.strip()
       	Nom,NSI,Maths,Francais = ligne.split(';')
        L.append(Nom)
        L.append(NSI)
        L.append(Maths)
        L.append(Francais)
    return(L)
    f.close()
L=import_table('table.csv')
#print(L)

def recherche_eleves(fichier, note_ref):
    LnomsEleves=[]
    f=open(fichier,'r')
    lignes_sans_premiere = f.readlines()[1:]
    for ligne in lignes_sans_premiere:
        ligne=ligne.strip()
       	Nom,NSI,Maths,Francais = ligne.split(';')
        if float(NSI)>10:
            LnomsEleves.append(Nom)
    return(LnomsEleves)
    f.close()
LnomsEleves=recherche_eleves('table.csv', 10)
#print(LnomsEleves)

def table_listes(fichier):
    LL=[]
    f=open(fichier,'r')
    lignes_sans_premiere = f.readlines()[1:]
    for ligne in lignes_sans_premiere:
       	Nom,NSI,Maths,Francais = ligne.split(';')
        L=[]
        L.append(Nom)
        L.append(float(NSI))
        L.append(float(Maths))
        L.append(float(Francais))
        LL.append(L)
        #LL.append([Nom,float(NSI),float(Maths),float(Francais)])
    return(LL)
    f.close()
#LL=table_listes('table.csv')
#print(LL)

from operator import itemgetter
#LL=sorted(LL,key=itemgetter(1))

import csv
def creation_csv(fichier, LL):
    f=open(fichier,'w',newline='')
    ligne = csv.writer(f, delimiter=';')
    ligne.writerow(['Nom', 'NSI', 'Maths', 'Francais'])
    for liste in LL:
        ligne.writerow(liste)
    f.close()
#creation_csv('table_tri3.csv',LL)

LL=table_listes('table_avec_doublon.csv')
print(LL)

def supprimer_doublon(LL):
    for liste in LL:
        if LL.count(liste)>1:
            LL.remove(liste)
#supprimer_doublon(LL)
#print(LL)
#creation_csv('table_sans_doublon3.csv',LL)

def supprimer_doublon2(LL):
    noms=[]
    for i in range(len(LL)):
        noms.append(LL[i][0])
    print(noms)
    for i in range(len(noms)):
        if noms.count(noms[i])>1:
            indiceSuppr=i
    LL.remove(LL[indiceSuppr])
supprimer_doublon2(LL)
print(LL)
