import numpy as np
import pandas as pd


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


variante([[1, 1, 1, 1, 1]])

