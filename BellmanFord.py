# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:40:21 2022

@author: nathan, quentin, iannis
"""
import random
import numpy as np     # pour absolument tout :)
import math as math    # pour inf


def BellmanFord(m, s0):
    
    #Initialisation
    M = np.matrix(m)            # Cast de la matrice d'entrée
    n = len(M)                  # Variable de taile de la matrice
    d = np.full(n, math.inf)    # Liste pour stoker les longueures des chemin de s0 à u (u correspondant a la variable d'ittération)
    pred = [None] * n           # Liste pour stoker les prédécéseurs de chaque arréte pour plus court chemin de s0 à u
    d[s0], pred[s0] = 0, s0     # La longueure du sommet de départ a lui méme est manuellement mise à 0 de plus il est son propre prédécéseur
    sommets= {}
    for i in range(n):
        sommets[i] = chr(ord('a')+i)
        
        
        
    for i in range(1, n-1):             # On ittére uniquement le nombre de fois nécéssaire (soit n)
        for u in range(n):                  
            for v in range(n):
                if d[v] > d[u]+M[u,v]:
                    d[v] = d[u]+M[u,v]  
                    pred[v] = u
                    
    for u in range(n):                  
        for v in range(n):
            if d[v] > d[u]+ M[u,v]:
                print("Il existe un cycle de poids négatif entre:")
                print(sommets[v], sommets[u])
                raise SystemExit()
           
#   prettyPrint(s0, d, pred, sommets)
    return s0, d, pred, sommets
  
