"""
# Code 3
mon_tuple = ("Angers", "Beacouzé", "Avrillé", "Trélazé")
for i in range(len(mon_tuple)):
    print(f"élément {i}:", mon_tuple[i])

# Code 4
def deux_nombres():
    dec1 = float(input("Entrez un premier nombre décimal: "))
    dec2 = float(input("Entrez un deuxième nombre décimal: "))
    mon_tuple=(dec1, dec2)
    return mon_tuple
print(deux_nombres())

# Code 5
def milieu(A_loc, B_loc):
    coo_milieu = ((A_loc[0] + B_loc[0])/2, (A_loc[1] + B_loc[1])/2)
    return coo_milieu

tuple_coo1 = (4,8)
tuple_coo2 = (-2,5)

print(milieu(tuple_coo1, tuple_coo2))
"""