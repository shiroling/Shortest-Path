# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:40:21 2022

@author: nathan, quentin, iannis
"""
import math as math    # pour inf
import numpy as np     # pour absolument tout :)

inf = math.inf
infin  = math.inf

def getSuivants(s0, M, Lsommets):
    suivants = []
    for i in Lsommets:
        if not s0:
            if not math.isinf(M[s0, i]):
                suivants.append(i)
    return suivants

def isValid(M, s0):
    n = len(M)
    MBis = M
    for u in range(n):
        for v in range(n):
            if M[u, v] < 0 :
                return False
    return True

def Djikstra(m, s0):
    # Précondition : M doit avoir des poids uniquement positifs
    if not isValid(m, s0):
        print("La matrice donné ne conviens pas à l'utilisation de Djikstra, tentez avec BellmanFord !")
        raise SystemExit()

    # Init
    n, pred, d, toVisit = len(m), [], [], []

    sommets= {}
    for i in range(n):
        sommets[i] = chr(ord('a')+i)

    for i in range(len(m)):
        d.append(inf)
        pred.append(None)
        toVisit.append(i)
    d[s0], pred[s0] = 0, s0
    u = 0
        
    # Iteration
    while len(toVisit) > 0:
        dist = inf
        for i in toVisit:
            if dist > d[i]:
                dist = d[i]
                u = i
        for v in range(n):
            if not math.isinf(m[u, v]):
                temDist = d[u] + m[u, v]
                if temDist < d[v]:
                    d[v] = temDist
                    pred[v] = u
        toVisit.remove(u)
    return s0, d, pred, sommets        
        
