import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

F1 = pygame.image.load('Formule_1_Bleue.png')  # 700 * 274 pix
FondScore = pygame.image.load('FondScore.jpg')
FondGO = pygame.image.load('GameOver.jpg')
FondGagne = pygame.image.load('Gagné.jpg')

Chiffres = [pygame.image.load('ico_0.png'), pygame.image.load('ico_1.png'), pygame.image.load('ico_2.png'),
            pygame.image.load('ico_3.png'), pygame.image.load('ico_4.png'), pygame.image.load('ico_5.png'),
            pygame.image.load('ico_6.png'), pygame.image.load('ico_7.png'), pygame.image.load('ico_8.png'),
            pygame.image.load('ico_9.png')]


def Formule_1():
    xF1 = 0
    yF1 = 75
    xRoute = 0
    collision = False

    global vies  # global pour permettre à la fonction de modifier la variable vie (pas seulement la lire),
    #               sinon, il faudrait passer vies en paramètre et la retourner
    global score
    global GameOver

    while not collision:

        screen.blit(pygame.image.load('Route_0.jpg'), (xRoute, 0))
        screen.blit(F1, (xF1, yF1))
        pygame.display.update()

        for event in pygame.event.get():  # écoute des touches appuyées
            print('?')
        touche = pygame.key.get_pressed()

        if touche[K_UP] and yF1 >= 50:  # touche "flèche haut" → faire "monter" la voiture
            yF1 = yF1 - 25
        elif ...:  # touche "flèche bas" → faire "descendre" la voiture
            ...

        xRoute = xRoute - 40  # -10 : lent

        if -3200 < xRoute < (-3200 + 2 * 700) and 20 < yF1 < (
                274 + 20):  # zone de collision voiture 1 sur Route_0, il faut compter la largeur de 2 F1
            collision = True
        elif ...:  # zone de collision voiture 2 de Route_0, il faut compter la largeur de 2 F1
            ...
        elif ...:  # zone de collision voiture 3 sur Route_0, il faut compter la hauteur de 2 F1
            ...

        elif xRoute < -8500:  # extrémité de la route atteinte : 8500pix + largeur écran = 10000pix
            score = ...
            vies = ...  # +2 vies, car ensuite collision=True -> vie=vie-1
            collision = ...

        if collision:  # en cas de collision, le score n'augmente pas et on perd une vie
            vies -= 1
            screen.blit(FondScore, (0, 0))
            screen.blit(Chiffres[score], (600, 500))
            screen.blit(Chiffres[vies], (1175, 500))
            pygame.display.update()
            pygame.time.wait(2000)

        if vies == 0:  # perdu
            GameOver = True
            screen.blit(FondGO, (0, 0))
            pygame.display.update()
            pygame.time.wait(2000)

        if score == 3:  # gagné
            GameOver = True
            ...
            ...
            ...


vies = 1  # pour permettre à vies de repartir à 1 à chaque fois que la fonction Formule_1() est appelée
score = 0
GameOver = False
continuer = True

while continuer:
    Formule_1()
    if GameOver:
        continuer = False
pygame.quit()
