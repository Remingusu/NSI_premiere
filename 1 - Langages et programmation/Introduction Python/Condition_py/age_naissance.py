from datetime import date


print("Bonjour") # affiche "Bonjour"
prenom = input("Quel est ton prénom ? ") # entrer le prénom + affiche la question
print("Bonjour", prenom) # afficher "Bonjour" + le prénom

an_naissance = int(input("Quelle est ton année de naissance ? ")) # entrer l'année de naissance + affiche la question
mois_naissance = int(input("Quel est ton mois de naissance ? ")) # entrer le mois de naissance + affiche la question
jour_naissance = int(input("Quel est ton jour de naissance ? ")) # entrer le jour de naissance + affiche la question

aujourdhui = date.today() # récupère la date d'aujourd'hui
an_actuel = aujourdhui.year # enregistre l'année actuel
mois_actuel = aujourdhui.month # enregistre le mois actuel
jour_actuel = aujourdhui.day # enregistre le jour actuel


if mois_naissance<=mois_actuel and jour_naissance<=jour_actuel:
    an = an_actuel-an_naissance
else:
    an = an_actuel-an_naissance-1

print(prenom, "vous avez", an, "ans") # affiche prenom + age
