# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ### Compréhension de l'algorythme Xcover

# %%
import xcover as x
import numpy as np
import matplotlib.pyplot as plt

# %%
# x?

# %%
# x.covers?

# %%
A = np.array([[0, 1, 0],
     [1, 0, 1],
     [0, 0, 1],
     [1, 1, 1],
     [0, 0, 0]], dtype = bool)
solutions = x.covers_bool(A)
for s in solutions :
    print(s)


# %% [markdown]
# Il semblerait que x.covers retourne une liste d'indice qui potentiellement serait une solution
# Ici, le 3ème élément est valide car il a tout les 1

# %% [markdown]
# Ainsi, on crée un tableau spécifique de 0 et de 1, et il faut réussir à dessiner la solution à partir d'une solution donnée par xcover

# %% [markdown]
# On veut donc recréer et dessiner la solution qu'on trouvera à partir de la solution que xcover nous donnera, ainsi, on veut d'abord savoir quelle pièce on va dessiner. 

# %%
def Dessine_sol(matrice, sol, dimensions):
    # On crée d'abord un tableau vide qui sera destiné à être colorié
    Tableau = np.zeros((dimensions))  
    #On va avoir besoin plus tard du nombre de cases, qui correspond aux valeurs après les premières qui sont au nombre du nombre de pièces,
    #Le nombre de pièces correspond à la taille de sol
    nombre_de_cases = len(matrice[0]) - len(sol)
    #On va maintenant regarder un élément qui correspond à la solution et mettre à la place des 0 un numero là où il faut
    for indice in sol:
        Ligne = matrice[indice]
        #On veut parcourir les informations correspondant à la couleur pour cette ligne
        for i in range (0, nombre_de_cases):
            if Ligne[i + len(sol)] == 1: 
                #Ici le problème est que on reçoit un indice qu'on veut transcrire en une position dans le tableau
                #Il suffit donc de faire la division euclidienne par le nombre de colonnes pour avoir la position dans le tableau
                c = i//dimensions[1]
                l = i%dimensions[1]
                Tableau[c, l] = indice
    plt.imshow(Tableau)

        
    
    
