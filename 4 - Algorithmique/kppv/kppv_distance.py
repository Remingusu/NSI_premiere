from math import sqrt


# Code 1
def distance_2f(pos_a: tuple, pos_b: tuple) -> float:
    dist = sqrt((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)
    return dist


ax = 5
ay = 5
list_points = [(1, 6), (3, 6), (3, 3), (3, 5), (6, 1), (6, 3)]
for point in list_points:
    print(f"Distance position A({ax}, {ay}) et B({point[0]}, {point[1]}): {distance_2f((ax, ay), point)}")


# Code 2
def distance_3f(features_a: dict, features_b: dict) -> float:
    dist = sqrt((features_a["age"]-features_b["age"])**2 +
                (features_a["taille"]-features_b["taille"])**2 +
                (features_a["poids"]-features_b["poids"])**2)
    return dist


a = {"age": 50.0, "taille": 168.0, "poids": 59.0}
b = {"age": 51.0, "taille": 183.0, "poids": 80.0}
print(f"Distance caractéristiques A et B: {distance_3f(a, b)}")
