""" Code 1* : 0,5 point
Réalisez un programme qui donne le nombre de parenthèses "(" et ")" dans une expression arithmétique
    Entrée : Lexpression=['(',')','(','(',')',')',')']
    Sortie : nbOuvr=3 et nbFerm=4
"""
Lexpression = ['(', ')', '(', '(', ')', ')', ')']
print(f'nbOuvr={Lexpression.count("(")} et nbFerm={Lexpression.count(")")}')

""" Code 2*** : 0,5 point
Réalisez une fonction qui nous indique si le parenthésage d'une expression arithmétique est correct ou incorrect
Expression arithmétique correctement parenthésée : (2 + 3) × (18/(4 + 2))
Expression arithmétique incorrectement parenthésée : (2 + 3) × (18/(4 + 2)
Pour vérifier le parenthésage, on peut utiliser la variable controleur=0 qui :
-augmente de 1 si l’on rencontre une parenthèse ouvrante "("
-diminue de 1 si l’on rencontre une parenthèse fermante ")"
Exemple 1 :
    Entrée : Lexpression=['(',')','(','(',')',')'] représentant l'expression : (2 + 3) × (18/(4 + 2))
    Sortie : Le parenthésage est correct (la variable contrôleur aura pris successivement pour valeur 1, 0, 1, 2, 1, 0)
Exemple 2 :
    Entrée : Lexpression=['(',')','(','(',')'] représentant l'expression : (2 + 3) × (18/(4 + 2)
    Sortie : Le parenthésage est incorrect (la variable contrôleur aura pris successivement pour valeur 1, 0, 1, 2, 1)
Exemple 3 :
    Entrée : Lexpression=['(',')','(',')',')','(',')'] représentant l'expression : (2 + 3) × (18/4)) + (2 - 1)
    Sortie : Le parenthésage est incorrect (la variable contrôleur aura pris successivement pour valeur 1, 0, 1, 0, -1, 0, -1)
"""
LexpressionA = ['(', ')', '(', '(', ')', ')']  # correcte
LexpressionB = ['(', ')', '(', '(', ')']  # incorrecte
LexpressionC = ['(', ')', '(', ')', ')', '(', ')']  # incorrecte


def parenthesage_correct(Lexpression):
    controller = 0
    for element in Lexpression:
        if element == '(':
            controller += 1
        elif element == ')':
            controller -= 1
    if controller != 0:
        print('Le parenthésage est incorrecte')
    else:
        print('Le parenthésage est correcte')


parenthesage_correct(LexpressionC)
