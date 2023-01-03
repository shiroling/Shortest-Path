import random
import numpy as np     # pour absolument tout :)
import math as math    # pour inf
import time
import matplotlib.pyplot as plt 

import genMatrix as gm
import BellmanFord as bf
import Djikstra as dj


infin = math.inf

M = np.matrix([[infin,    8,    6,infin],
               [infin,infin,infin,infin],
               [infin,    3,infin,infin],
               [infin,    5,    1,infin]
              ])

def prettyPrint(s0, d, pred, sommets):
  for i in range(len(d)):
    chemin = []
    chemin.append((sommets[i]))
    if pred[i] == None:
      print("Le sommet '"+ sommets[i] + "' est inaccessible")
    else:
      print("Le chemin d'accés à '" + sommets[i] + "' est ", end="")
      j= i
      while j != s0:
        j= pred[j]
        chemin.append(sommets[j])
      chemin.reverse()
      print(chemin, end="")
      print(", sa taille totale est: ",end="")
      print(d[i])



def getArrows(sommets, M):
  n = len(M)
  listArrétes = []
  for u in range(n):
    for v in range(n):
      if not np.isinf(M[u,v]):
        listArrétes.append((sommets[u], sommets[v]))
  return listArrétes



for i in range(3):
  print("Matrice ", str(i))
  M = gm.genMatrix(6, 0, 15, 40)
  print(M)


""" Décommentez si vous voulez afficher un exemple de chaque algo
print("BellmanFord:")
s0, d, pred, sommets = bf.BellmanFord(M, 0)
print(pred)
#print(sommets[s0] + "\n" + str(d) + "\n" + str(pred))
prettyPrint(s0, d, pred, sommets)

print("Djikstra:")
s0, d, pred, sommets = dj.Djikstra(M, 0)
print(pred)
#print(sommets[s0] + "\n" + str(d) + "\n" + str(pred))
prettyPrint(s0, d, pred, sommets)
"""


def Dij(n):
        M = gm.genMatrix(n, 0, 15, 50)
        return dj.Djikstra(M, 0)

def BF(n):
        M = gm.genMatrix(n, 0, 15, 50)
        return bf.BellmanFord(M, 0)

""" Décommentez pour tester la vitessed'execution et afficher les courbes de leurs temps réspectifs
tempsDj, tempsBf, indices = [], [], []
start=time.perf_counter()  
for n in range(1, 100):
  # print("test pour n : ",n)
  Dij(n)
  indices.append(n)
  stop=time.perf_counter()

  print("Temps Algorithme de Djikstra :")
  print(stop-start)

  tempsDj.append(stop-start)
  start=time.perf_counter()  
  Dij(n)
  stop=time.perf_counter()

  print("\n")
  print("Temps Algorithme de BellMan Ford :")
  print(stop-start)

  tempsBf.append(stop-start)
print(np.sum(tempsDj))
print(np.sum(tempsBf))

plt.figure(1)
plt.loglog(indices, tempsDj, label = "Temps Djikstra")
plt.loglog(indices, tempsBf, label = "Temps BellmanFord")
plt.legend()
plt.show()
"""
