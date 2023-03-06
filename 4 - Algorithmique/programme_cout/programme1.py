import time


def tri_insertion(L):
    for i in range(1, len(L)):
        memo = L[i]
        j = i
        while memo < L[j-1] and j > 0:
            L[j] = L[j-1]
            L[j-1] = memo
            j = j-1


debut = time.process_time()
taille = 1000000
L = [i for i in range(taille, 0, -1)]
temps = time.process_time()-debut
print(L)
print("Tableau créé en", temps, "secondes")

debut = time.process_time()
tri_insertion(L)
temps = time.process_time()-debut
print(L)
print("Tableau trié en", temps, "secondes")
