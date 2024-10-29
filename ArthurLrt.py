# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy as np
import matplotlib.pyplot as plt
import xcover as x


# +
def tableau (n,m):
    T=np.zeros((n,m))
    return T

def obstacle (tableau,L):
    for v in L :
        l=v[0]
        c=v[1]
        tableau[l][v]==False 
    return tableau

pieces=[[[1, 1, 0], [0, 1, 1], [0, 1, 0]],[[1, 1, 1, 1, 1]],[[1, 0, 0, 0], [1, 1, 1, 1]], [[1, 1, 0, 0], [0, 1, 1, 1]],[[1, 1, 1], [1, 1, 0]],[[1, 1, 1], [0, 1, 0], [0, 1, 0]],[[1, 1, 1], [1, 0, 1]],[[1, 1, 1], [1, 0, 0], [1, 0, 0]],[[1, 0, 0], [1, 1, 0], [0, 1, 1]],[[0, 1, 0], [1, 1, 1], [0, 1, 0]],[[0, 1, 0, 0], [1, 1, 1, 1]],[[1, 1, 0], [0, 1, 0], [0, 1, 1]]]
dimensions=(6,10)


# +
# x?
# -

def supprimer_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons


def variante(piece):
    transformations=[piece]
    transformations.append(np.fliplr(piece).tolist())
    rotation=piece
    for i in range (3):
        rotation = np.rot90(rotation, -1)
        symétrie = np.fliplr(rotation)
        transformations.append(rotation.tolist())
        transformations.append(symétrie.tolist())
    return supprimer_doublons(transformations)


# +
import numpy as np

def emplacement(piece, tableau, idx):
    L = variante(piece)
    T = []
    (l, c) = tableau.shape
    j = np.zeros(12)
    j[idx] = 1

    for t in L:
        (i, j_shape) = (len(t),len(t[0]))
        for m in range(l - i + 1):
            for n in range(c - j_shape + 1):
                tableau_prime = tableau.copy()  # Faire une copie pour éviter de modifier le tableau original
                # Placer la pièce dans le tableau
                tableau_prime[m:m+i, n:n+j_shape] = 1  # Remplacer les valeurs par 1
                T.append((np.concatenate((j, tableau_prime.flatten()))).tolist())  # Ajouter le tableau à la liste

    return T
    

    
# -






# +
def tableau_final(tableau, pieces):
    idx=0
    L=[]
    for p in pieces :
        L = L + emplacement(p, tableau, idx)
        idx+=1
    return L
        
        
    
# -

pattern = tableau_final(tableau(12,5), pieces)
len(pattern)

len(pattern[0])

solutions = x.covers_bool(np.array(pattern))

#print(tableau_final(tableau(6,10), pieces))
next(solutions)


def Tableau_sol(matrice, sol, dimensions):
    Tableau = np.zeros((dimensions))
    nombre_de_cases = len(matrice[0]) - len(sol)
    for indice in sol:
        Ligne = matrice[indice]
        for i in range (0, nombre_de_cases - len(sol)):
            if Ligne[i + len(sol)] == 1: 
                c = i//dimensions[1]
                l = i%dimensions[1]
                Tableau[c, l] = indice
    plt.imshow(Tableau)


Tableau_sol(tableau_final(tableau(dimensions), pieces),sol,dimensions)


