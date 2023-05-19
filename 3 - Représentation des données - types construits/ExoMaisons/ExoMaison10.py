""" Code1* : 0,5 point
Créez un code, avec une boucle, permettant d'afficher toutes les cartes de coeur :
1 de ♡
...
Valet de ♡
Reine de ♡
Roi de ♡
Aide : pour afficher le symbole du coeur : print(chr(0x2661))
"""
for i in range(10):
    print(f'{i+1} de {chr(0x2661)}')
print(f'Valet de {chr(0x2661)}')
print(f'Dame de {chr(0x2661)}')
print(f'Roi de {chr(0x2661)}')

""" Code2** : 0,5 point
Créez un code, avec une boucle, permettant de créer la liste de tuples suivante :.
[(1,'♡'),(2,'♡'),(3,'♡'),(4,'♡'),(5,'♡'),(6,'♡'),(7,'♡'),(8,'♡'),(9,'♡'),('Valet','♡'),('Reine','♡'),('Roi','♡')]
"""
card_list = []
for i in range(10):
    card_tuple = (i+1, chr(0x2661))
    card_list.append(card_tuple)
card_list.append(('Valet', chr(0x2661)))
card_list.append(('Dame', chr(0x2661)))
card_list.append(('Roi', chr(0x2661)))
print(card_list)
