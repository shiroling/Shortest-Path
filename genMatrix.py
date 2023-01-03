import numpy as np
import random

#Fonction générant une liste correspondant au indice des cases de la future matrice notés de O a n^2-1
def getMatrixIndexes(n):
   return list(range(0, n**2-1))

# La fonction permet de générer une matrice de taille n*n avec 'ratio' le pourcentage de case à définir avec des nombres aléatoires entre 's' et 'e'
def genMatrix(n, s, e, ratio):
  Mg = np.full((n, n), np.inf)  #on déclare une matrice (float) et la remplie d'infini 
  
  list = getMatrixIndexes(n)    # On déclare une liste correspondant au cases de la matrice

  # On définit le nombre d'ittération comme étant un pourcentage de la matrice affin de choisit le nombre de chiffres générés par rapport au nombre d'infini
  for i in range((n*n) *ratio//100):
    x = random.choice(list)               # Choix d'une case au hasard
    list.remove(x)                        # Suppresion de l'indice de la liste pour ne pas le rechoisir plus tard
    Mg[x//n][x%n] = random.randint(s, e)  # affectation d'un nombre aléatoire entre 's' et 'e' dans la case courante

  return Mg


genMatrix(5, -10.0, 12.0, 50)

