# Créez la liste suivante par compréhension : [3.14, 6.28, 9.42, ... 28.26]
float_list = [a*3.14 for a in range(1,10)]
print(float_list)

# Créez la liste suivante par compréhension : [[1, 2], [2, 2], [3, 2], ... [9, 2]]
list_of_2 = [[n]+[2] for n in range(1, 10)]
print(list_of_2)

# Créez la liste suivante par compréhension : ['MMM', 'OOO', ... 'NNN']
word = "MOULIN"
word_list = [3*l for l in word]
print(word_list)
