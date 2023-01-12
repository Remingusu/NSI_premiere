"""
# Code 1 + 2
word=input("Entrez un mot: ")
print("Votre mot est composé de", len(word), "caractères")
i=0
for letter in word:
    print(f"Le caractère n°{i} est", letter, "son code ASCII en décimal est", ord(letter))
    i+=1

# Code 3
nbr = input("Entrez un nombre: ")
result = 0
for letter in nbr:
    result = result+int(letter)
if result == 10:
    print("Bravo")
else:
    print("Perdu, la somme des chiffres de votre nombre fait", result)

# Code 4
mot=" "
sentence=""
while mot!="":
    mot = input("Entrez un mot: ")
    sentence = sentence + mot + " "
print(sentence)

# Code 5
mot=input("Entrez un mot: ")
for i in range(len(mot)):
    print(chr(ord(mot[i])-8))
"""
# Code 6 + 7
mot_mi=input("Entrez un mot: ")
mot_ma=""
for letter in mot_mi:
    if 65<=ord(letter)<=90:
        mot_ma=mot_ma+chr(ord(letter)+32)
    elif 97<=ord(letter)<=122:
        mot_ma=mot_ma+chr(ord(letter)-32)
print(mot_ma)