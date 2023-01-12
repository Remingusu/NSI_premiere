while True:
    mois_naissance=int(input("Quel est votre mois de naissance ? "))

    if (mois_naissance==9) or (mois_naissance==11):
        nb_jours=30
    elif mois_naissance==2:
        nb_jours=28
    elif mois_naissance%2==1 or mois_naissance==8 or mois_naissance==10 or mois_naissance==12:
        nb_jours=31
    elif mois_naissance%2==0:
        nb_jours=30

    print(f"Votre mois de naissance contient {nb_jours} jours")
