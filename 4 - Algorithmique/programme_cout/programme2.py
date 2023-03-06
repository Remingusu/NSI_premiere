import numpy as np
import matplotlib.pyplot as plt
import random
import math

def parcours(L):
    NBinstructions=0
    for i in range(len(L)):
        L[i]=0
        NBinstructions+=1
    return NBinstructions

def test1():
    A=0
    NBinstructions=1
    A+=1
    NBinstructions+=1
    A+=1
    NBinstructions+=1
    return NBinstructions

def test2(L):
    NBinstructions=0
    NBinstructions+=parcours(L)
    return NBinstructions

taille=300
L=[0 for i in range(taille)]
pas=21
x1=np.linspace(0,taille,pas)

instructions1=[]
instructions2=[]
instructions3=[]

for i in range(pas):
    limite=int(x1[i])
    resultat1=test1()
    resultat2=test2(L[0:limite])
    instructions1.append(resultat1)
    instructions2.append(resultat2)

fig=plt.figure()

ax1=fig.add_subplot(211)
plt.xlabel('taille')
plt.ylabel('coût')
plt.grid(True)
ax1.plot(x1,instructions1)
ax1.plot(x1,instructions2)

plt.show()