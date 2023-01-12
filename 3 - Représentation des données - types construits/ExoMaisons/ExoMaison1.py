# écrivez la fonction taille() qui sera égale à la fonction len()

def taille(mot_loc):
    i=0
    for char in mot_loc:
        i+=1
    return i
mot="Bonjour"
print("Le nombre de caractères de la chaine mot est:", taille(mot))
