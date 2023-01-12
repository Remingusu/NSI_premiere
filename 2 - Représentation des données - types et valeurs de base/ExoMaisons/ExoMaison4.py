if mois_naissance > mois_actuel or (mois_naissance == mois_actuel and jour_naissance > jour_actuel):
    age = an_actuel - an_naissance - 1
else:
    age = an_actuel - an_naissance