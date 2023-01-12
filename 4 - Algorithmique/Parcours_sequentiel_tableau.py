L=[p for p in range(21)]

def recherche_note(L_loc, note_loc):
    occur = False
    for element in L_loc:
        if element == note_loc:
            occur = True
    return occur

note = int(input("Entrer la note à chercher dans la liste: "))
print(recherche_note(L, note))
