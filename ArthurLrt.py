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


# +
def tableau (n,m):
    T=np.one((n,m))
    return T

def obstacle (tableau,L):
    for v in L :
        l=v[0]
        c=v[1]
        tableau[l][v]==False 
    return tableau


    

# +
import numpy as np

def emplacement(piece, tableau, idx):
    L = variante(piece)
    T = []
    (l, c) = tableau.shape
    j = np.zeros(12)
    j[idx] = 1

    for t in L:
        (i, j_shape) = t.shape
        for m in range(l - i + 1):
            for n in range(c - j_shape + 1):
                tableau_prime = tableau.copy()  # Faire une copie pour éviter de modifier le tableau original
                # Placer la pièce dans le tableau
                tableau_prime[m:m+i, n:n+j_shape] = 1  # Remplacer les valeurs par 1
                T.append(np.concatenate((j, tableau_prime.flatten())))  # Ajouter le tableau à la liste

    return T
    

    
# -

t=np.array([[1],[1]])
piece = [t]
tableau =np.array([[0,0,0],[0,0,0]])


emplacement(piece,tableau,3) 


# +
def tableau_final(tableau, pieces):
    idx=0
    L=[]
    for p in pieces :
        L.append(emplacement(p, tableau, idx))
        idx+=1
    return L
        
        
    
# -




