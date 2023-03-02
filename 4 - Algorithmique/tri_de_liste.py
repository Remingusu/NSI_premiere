from random import sample

L1 = sample(range(1, 50), 5)
print("Référence:", L1)

# Code 1
def tri_selection_v1(liste):
    L2 = []
    for i in range(len(liste)):
        L2.append(min(liste))
        liste.remove(min(liste))
    return L2


print("Lise triée sélection V1:", tri_selection_v1(L1.copy()))


# Code 2
def tri_selection_v2(liste):
    for i in range(len(liste)):
        i_min = liste.index(min(liste[i:]))
        n = liste[i]
        liste[i] = liste[i_min]
        liste[i_min] = n
    print("Liste triée sélection V2:", liste)


tri_selection_v2(L1.copy())


# Code 2 bis
def tri_selection_v2_bis(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[j] == min(liste[i:]):
                i_min = j
        n = liste[i]
        liste[i] = liste[i_min]
        liste[i_min] = n
    print("Liste triée sélection V2 bis:", liste)


tri_selection_v2_bis(L1.copy())


# Code 3
def tri_insertion_v1(liste):
    for i in range(len(liste)):
        val_min = min(liste[i:])
        liste.remove(val_min)
        liste.insert(i, val_min)
    print("Liste triée insertion V1:", liste)


tri_insertion_v1(L1.copy())


# Code 4
def tri_insertion_v2(liste):
    len_list = len(liste)
    for i in range(len_list):
        liste.append(min(liste[0:len_list-i]))
        liste.remove(min(liste[0:len_list-i]))
    print("Liste triée insertion V2:", liste)


tri_insertion_v2(L1.copy())


# Code 5
def tri_insertion_v3(liste):
    len_list = len(liste)
    for i in range(len_list):
        liste.append(max(liste[0:len_list-i]))
        liste.remove(max(liste[0:len_list-i]))
    print("Liste triée insertion V2 Inverse:", liste)


tri_insertion_v3(L1.copy())
