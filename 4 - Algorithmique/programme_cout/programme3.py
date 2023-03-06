import numpy as np
import matplotlib.pyplot as plt
import random
import math


def parcours(L):
    NBinstructions = 0
    for i in range(len(L)):
        L[i] = 0
        NBinstructions += 1
    return NBinstructions


def test1():
    A = 0
    NBinstructions = 1
    A += 1
    NBinstructions += 1
    A += 1
    NBinstructions += 1
    return NBinstructions


def test2(L):
    NBinstructions = 0
    NBinstructions += parcours(L)
    return NBinstructions


def test3(L):
    nb = 0
    NBinstructions = 0
    nb = +1
    # L[0]+=1
    NBinstructions += 1
    nb = +1
    # L[0]+=1
    NBinstructions += 1
    NBinstructions += parcours(L)
    return NBinstructions


def test4(L):
    NBinstructions = 0
    for i in range(len(L)):
        NBinstructions += parcours(L)
    return NBinstructions


def test5(L):
    NBinstructions = 0
    NBinstructions += parcours(L)
    NBinstructions += parcours(L)
    NBinstructions += parcours(L)
    return NBinstructions


taille = 300
L = [0 for i in range(taille)]
pas = 21
x1 = np.linspace(0, taille, pas)

instructions1 = []
instructions2 = []
instructions3 = []
instructions4 = []
instructions5 = []

for i in range(pas):
    limite = int(x1[i])
    resultat1 = test1()
    resultat2 = test2(L[0:limite])
    resultat3 = test3(L[0:limite])
    resultat4 = test4(L[0:limite])
    resultat5 = test5(L[0:limite])
    instructions1.append(resultat1)
    instructions2.append(resultat2)
    instructions3.append(resultat3)
    instructions4.append(resultat4)
    instructions5.append(resultat5)

fig = plt.figure()

ax1 = fig.add_subplot(211)
plt.xlabel('taille')
plt.ylabel('coût')
plt.grid(True)
ax1.plot(x1, instructions1)
ax1.plot(x1, instructions2)
ax1.plot(x1, instructions3)
ax1.plot(x1, instructions4)
ax1.plot(x1, instructions5)

plt.show()
