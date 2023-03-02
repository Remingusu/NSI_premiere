import random as rdm

L = rdm.sample([p for p in range(1, 1024)], 64)


def parcours(L, val):
    L.sort()
    cp = 0
    i = 0
    loop = True
    while loop:
        if val == L[i]:
            loop = False
        cp += 1
        i += 1
    return i-1, cp


def dichotomie(L, val):
    L.sort()
    i_min = 0
    i_max = len(L)
    i_milieu = (i_min + i_max) // 2
    coup = 0
    while L[i_milieu] != val and i_milieu != 0:
        print("loop")
        if L[i_milieu] > val:
            i_max = i_milieu + 1
        else:
            i_min = i_milieu - 1
        coup += 1
        i_milieu = (i_min + i_max) // 2
    return i_milieu, coup


L.sort()
print(L)

val = int(input("Valeur recherchée: "))

result = parcours(L, val)
print(f"L'indice du nombre est {result[0]}. "
      f"Il a été trouvé en {result[1]} coups.\n")

result_dicho = dichotomie(L, val)
print(f"L'indice du nombre est {result_dicho[0]}. "
      f"Il a été trouvé en {result_dicho[1]} coups.")
