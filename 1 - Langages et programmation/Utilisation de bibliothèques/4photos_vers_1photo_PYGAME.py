# 4 photos en 500x500 pix --> affichage dans une fenêtre pygame pour visualiser 1000x1000 pix
# explications : https://he-arc.github.io/livre-python/pygame/index.html

import pygame
from pygame.locals import QUIT

# from pygame.locals import*


pygame.init()
fenetre = pygame.display.set_mode((1000, 1000))

fond1 = pygame.image.load("Angers_1.jpg").convert()
fond2 = pygame.image.load("Angers_2.jpg").convert()
fond3 = pygame.image.load("Angers_3.jpg").convert()
fond4 = pygame.image.load("Angers_4.jpg").convert()

# BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:  # QUIT=croix de la fenêtre pygame
            continuer = 0

    fenetre.blit(fond1, (0, 0))
    fenetre.blit(fond2, (0, 500))
    fenetre.blit(fond3, (500, 0))
    fenetre.blit(fond4, (500, 500))

    pygame.display.update()

pygame.quit()
