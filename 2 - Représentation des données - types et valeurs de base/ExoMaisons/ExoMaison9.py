# transformer le programme suivant en créant la fonction :
# votreAge(jour_nais_loc,mois_nais_loc,an_nais_loc)
# la fonction renvoie la variable age que vous renommerez dans la fonction : age_loc
from datetime import date


aujourdhui = date.today()
an_actuel = aujourdhui.year
mois_actuel = aujourdhui.month
jour_actuel = aujourdhui.day

def votreAge(jour_nais_loc, mois_nais_loc, an_nais_loc):    
    if(mois_nais_loc>mois_actuel):
        age_loc = an_actuel-an_nais_loc-1
    elif(mois_nais_loc==mois_actuel):
        if (jour_nais_loc>jour_actuel):
            age_loc = an_actuel-an_nais_loc-1
        else:
            age_loc = an_actuel-an_nais_loc
    else:
        age_loc = an_actuel-an_nais_loc
    return age_loc

jour_nais = int(input("Quelle est ton jour de naissance: "))
mois_nais = int(input("Quelle est ton mois de naissance: "))
an_nais =int(input("Quelle est ton année de naissance: "))

print("Votre age est", votreAge(jour_nais, mois_nais, an_nais), "ans")
