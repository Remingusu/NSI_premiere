L_notes = [11.5, 10, 14.5, 13, 7, 16, 9]

# Code 1
def calcul_moyenne(L_notes_loc):
    moyenne = 0
    for note in L_notes_loc:
        moyenne = moyenne+note
    moyenne = moyenne/len(L_notes_loc)
    return moyenne

# Code 2
def note_plus_1(L_notes_loc):
    moyenne = calcul_moyenne(L_notes_loc)
    if moyenne < 12:
        for i  in range(len(L_notes_loc)):
            L_notes_loc.append(L_notes_loc[0]+1)
            L_notes_loc.remove(L_notes_loc[0])
        moyenne = calcul_moyenne(L_notes_loc)
    return moyenne

# Code 3
def semestres(L_notes_loc):
    semestre1 = []
    if len(L_notes_loc)%2 == 0:
        for i in range(len(L_notes_loc)/2):
            semestre1.append(L_notes_loc[0])
            L_notes_loc.pop(0)
        semestre2 = L_notes_loc
    else:
        for i in range(int(len(L_notes_loc)//2)):
            semestre1.append(L_notes_loc[0])
            L_notes_loc.pop(0)
        semestre2 = L_notes_loc
    tuple_semestre = (semestre1, semestre2)
    return tuple_semestre
semestres = semestres(L_notes.copy())

# Code 4
def semestres_bis(L_notes_loc):
    print(int(len(L_notes_loc)/2-0.5))
    semestre1 = [L_notes_loc[i] for i in range(0, int(len(L_notes_loc)//2))]
    semestre2 = [L_notes_loc[i] for i in range(int(len(L_notes_loc)//2),len(L_notes_loc))]
    tuple_semestres = (semestre1, semestre2)
    return tuple_semestres

semestres_bis = semestres_bis(L_notes.copy())
print(f"Les notes du semestre 1: {semestres_bis[0]}\nLes notes du semestre 2: {semestres_bis[1]}")