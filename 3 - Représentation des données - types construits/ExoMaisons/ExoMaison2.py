# Code1* : créez D_match_1={"1:"Samira",2:"Léa",3:"Lucie"} à partir L_match_1=["Samira","Léa","Lucie"]
L_match_1 = ["Samira", "Léa", "Lucie"]
D_match_1 = {}
i = 0
for name in L_match_1:
    i += 1
    D_match_1[i] = name
print(D_match_1)

# Code2** : créez D_match_1={"joueuse1":"Samira","Joueuse2":"Léa","Joueuse3":"Lucie"}
# à partir L_match_1=["Samira","Léa","Lucie"]
L_match_2 = ["Samira", "Léa", "Lucie"]
D_match_2 = {}
i = 0
for name in L_match_2:
    i += 1
    D_match_2[f'Joueuse {i}'] = name
print(D_match_2)
