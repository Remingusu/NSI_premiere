L = [27, 15, 10, 7, 5, 12, 4, 17, 20, 2, 31]


def parcours(L, val):
    L.sort()
    i_min = 0
    i_max = len(L)
    i_milieu = (i_min + i_max) // 2
    coup = 0
    while L[i_milieu] != val or i_milieu != 0:
        if L[i_milieu] > val:
            i_max = i_milieu + 1
        else:
            i_min = i_milieu - 1
        coup += 1
        i_milieu = (i_min + i_max) // 2
    return i_milieu, coup


return_value = parcours(L, 1)
print(f"L'indice du nombre est {return_value[0]}. "
      f"Il a été trouvé en {return_value[1]} coups.")
