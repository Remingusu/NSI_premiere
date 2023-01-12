"""
# Code 3
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(ma_liste))
print(ma_liste[5])
ma_liste.append(10)
print(ma_liste)
print(ma_liste[-2])
ma_liste.remove(5)
print(ma_liste)
ma_liste.remove(ma_liste[7])
print(ma_liste)

# Code 4
note = int(input("Ajouter une note: "))
liste_note=[]
while 0 <= note <= 20:
    liste_note.append(note)
    note = int(input("Ajouter une note: "))
print(liste_note)

# Code 5
ma_liste = [5, 6, 7, 8, 9]
ma_liste.reverse()
print(ma_liste)


# Code 5 bis
ma_liste = [5, 6, 7, 8, 9]
ma_liste_inverse=[]
for i in range(1, len(ma_liste)+1):
    ma_liste_inverse.append(ma_liste[-i])
print(ma_liste_inverse)


# Code 6
ma_liste=[18, 13, 10, 7, 19, 19, 18, 0, 8, 12, 0, 15, 2, 8, 4, 4, 18, 5, 3, 18, 6, 12, 12, 15, 11, 8, 12, 13, 10, 20, 2, 15, 11, 11, 4, 18, 17, 0, 17, 19, 13, 7, 14, 5, 2, 13, 7, 13, 17, 9, 1, 7, 7, 3, 3, 7, 3, 4, 11, 7, 9, 2, 17, 2, 3, 5, 0, 15, 18, 0, 7, 7, 7, 15, 11, 11, 20, 8, 3, 17, 3, 18, 20, 16, 10, 18, 8, 7, 9, 17, 18, 19, 14, 11, 13, 12, 20, 12, 19, 15]
nombre = int(input("Choisir un nombre: "))
occurrence=0
for element in ma_liste:
    if element == nombre:
        occurrence+=1
print("Le nombre d'occurrence de", nombre, "dans ma_liste est", occurrence)
"""