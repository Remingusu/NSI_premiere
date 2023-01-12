"""Code 3 :
Ecrivez un programme qui demande à l’utilisateur d’entrer un nombre (qui sera sous forme de chaine de caractères) et qui calcule la somme des chiffres qui le compose.
Si la somme des chiffres est égale à 10 alors le programme affichera "Bravo" sinon il affichera "Perdu, la somme des chiffres de votre nombre fait : ?? ".
Exemple d’exécution :
Entrez un nombre : 361
Bravo
Entrez un nombre : 362
Perdu, la somme des chiffres de votre nombre fait : 11

nombre=input("Entrez un nombre: ")
somme=0
for i in range(len(nombre)):
    somme=somme+int(nombre[i])
if somme==10:
    print("Bravo")
else:
    print("Perdu, la somme des chiffres de votre nombre fait:",somme)
"""
# Ecrivez un programme qui fait la même chose en faisant les opérations suivantes sur le nombre : // et %
# // : quotient
# % : reste

nombre=input("Entrez un nombre: ") # demande un nombre
taille=len(nombre) # le nombre de chiffre
div = 1*(10**taille) # diviseur = 10 puissance le nombre de chiffre
result=0 # resultat à 0
dif=0 # différence a 0
for i in range(taille):
    div=div/10
    nombre=int(nombre)-dif
    number = nombre//div
    result+=number
    dif=number*div
if result==10:
    print("Bravo")
else:
    print("Perdu, la somme des chiffres de votre nombre fait:", result)