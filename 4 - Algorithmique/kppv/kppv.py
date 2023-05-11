from math import sqrt


def lecture(fichier) -> tuple:
    with open(fichier, 'r', encoding='utf8') as f:
        firstLine = f.readline()
        feat = firstLine.strip().split(',')
        features = feat[:len(feat) - 1]
        vectors = []
        labels = []
        for ligne in f:  # la première ligne ne sera pas lue
            vect = {}
            li = ligne.strip().split(',')
            for i in range(len(features)):
                vect[features[i]] = float(li[i])
            vectors.append(vect)
            labels.append(str(li[-1]))
    return features, vectors, labels


features, vectors, labels = lecture("iris.csv")
print("features :\n", features)
print("vectors :\n", vectors)
print("labels :\n", labels)

premier_iris = {'sepalLength': 5.1, 'sepalWidth': 3.5, 'petalLength': 1.4, 'petalWidth': 0.2}


def distance(A, B, features) -> float:
    dist = 0
    for i in range(len(features)):
        dist += (A[features[i]] - B[features[i]]) ** 2
    dist = sqrt(dist)
    return dist


def distanceAll(new_iris, samples, features) -> list:
    L_distances = []
    for sample in samples:
        L_distances.append(distance(new_iris, sample, features))
    return L_distances


L_distances = distanceAll(premier_iris, vectors, features)


def k_plus_proches(L_distances, k) -> list:
    k_indices_plus_proches = []
    l_distances_triee = sorted(L_distances)
    for i in range(k):
        k_indices_plus_proches.append(L_distances.index(l_distances_triee[i]))
    return k_indices_plus_proches


k_indices_plus_proches = k_plus_proches(L_distances, 5)


def classification(labels, k_indices_plus_proches) -> int:
    label = int()
    return label


print(classification(labels, ['2','3','3','1','3','1','3','2']))
print(classification(labels, k_indices_plus_proches))
