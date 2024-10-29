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
# On veut donc recréer et dessiner la solution qu'on trouvera à partir de la solution que xcover nous donnera, ainsi, on veut d'abord savoir quelle pièce on va dessiner. Cette information est contenue dans les (nombre de pièces) premiers chiffres des lignes.
# On crée donc une fonction qui nous donne le numero de la pièce dont on est en train de lire la ligne

# %%
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
    return(Tableau)

        
    
    
