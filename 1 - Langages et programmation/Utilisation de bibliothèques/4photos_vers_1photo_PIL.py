# 4 photos en 500x500 pix --> collage --> 1 photo 1000x1000 pix
# explications : https://he-arc.github.io/livre-python/pillow/index.html

from PIL import Image
from bibli import *

# programme principal
im2 = Image.new("RGB", (1000, 1000))  # image 1000*1000
liste_noms = ['Angers_1.jpg', 'Angers_2.jpg', 'Angers_3.jpg', 'Angers_4.jpg']
cpt = 0
for colonne in range(2):
    for ligne in range(2):
        im1 = Image.open(liste_noms[cpt])  # image 500*500
        caseImage(colonne, ligne, im1, im2)
        cpt += 1
im2.save('Angers.jpg')
