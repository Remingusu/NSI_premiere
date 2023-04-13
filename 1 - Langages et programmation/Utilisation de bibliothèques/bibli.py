def caseImage(colonne, ligne, im1, im2):
    for x in range(500):
        for y in range(500):
            p = im1.getpixel((x, y))
            R = p[0]
            V = p[1]
            B = p[2]
            if colonne == 0 and ligne == 0:  # photo 1
                im2.putpixel((x, y), (R, V, B))
            elif colonne == 0 and ligne == 1:  # photo 2
                im2.putpixel((x, y + 500), (R, V, B))
            elif colonne == 1 and ligne == 0:  # photo 3
                im2.putpixel((x + 500, y), (R, V, B))
            elif colonne == 1 and ligne == 1:  # photo 4
                im2.putpixel((x + 500, y + 500), (R, V, B))
