# -*- coding: utf-8 -*-
"""
Spyder Editor

R207 Exercice 2.3 2.4

This is a temporary script file.
"""
from numpy import *

def Trans1(M) :
    k=shape(M)[0]           # Nombre de lignes du tableau M. len(M) fonctionne si M est de type array.
    N=M                     # Initialisation de la somme des M^k
    P=M                     # Initialisation des puissances de M
    for i in range(k-1) :   # Calcul de sum M**k
        P=dot(M,P)
        N=N+P
    for i in range(k):      # réduction des coeff non nuls à 1
        for j in range(k):
            N[i,j]=min(N[i,j],1)
    return(N)

M=array([[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,1,0,0],[0,1,0,0,0]])
print(Trans1(M))

""" 
    Le code ci-dessus n'est fonctionnel que pour des matrices inférieures à 15x15: la taille des nombres entiers 
    obtenus (à croissance exponentielle) dépasse la limite de l'interpréteur Python. 

    Trois solutions:
    - les coefficients négatifs aberrants sont nécessairement des coefficients non nuls 
    donc on les remplace aussi par des 1 avec un if à la place du min; 
    (Pas très bon: on sature les mémoires par des grands nombres....)
    - On fait les calculs en booléen (1+1=1): beaucoup mieux, mais pas facile à implémenter en calcul matriciel. 
    - On réduit les calculs à chaque étape au lieu de le faire à la fin. 
    Cette solution donne:
"""

def Red(M):             # Fonction Réduction qui met les coefficients non nuls de M à 1
    k=shape(M)[0]
    N=M
    for i in range(k):
        for j in range(k):
            N[i,j]=min(N[i,j],1)
    return(N)

def Trans1(M) :
    k=shape(M)[0]           # nbre de lignes du tableau M
    N=M                     # initialisation de la somme des M^k
    P=M                     # initialisation des puissances de M
    for i in range(k-1) :
        P=Red(dot(M,P))     # on réduit à chaque étape de la boucle
        N=Red(N+P)
    return(N)

M=array([[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,1,0,0],[0,1,0,0,0]])
print(Trans1(M))



# 1- Génération aléatoire d'une matrice de graphe
import numpy.random as rd
M=rd.randint(0,2,(20,20))  # voir la description de cette fonction sur le polycop
print(M)
print(Trans1(M))

"""Remarque: le résultat de la fermeture transitive est très souvent le graphe plein (que des 1): 
    le graphe de départ a trop de flèches et on peut aller de n'importe quel point 
    à n'importe quel autre point. Il faudrait tester sur un graphe avec peu de 1 en générant une matrice
    avec une loi autre que la loi uniforme (10% de 1, 90% de 0 par exemple:)"""
    
M=rd.binomial(1,1/10,(20,20))
print(M)
print(Trans1(M))


# 2- temps de calcul de sa fermeture transitive
import time 
start=time.perf_counter()   # La fonction clock ne fonctionne plus en Python3!
Trans1(M)
stop=time.perf_counter()
print(stop-start)


# 3- Temps de calcul en fonction de la taille n
def temps(n):
    M=rd.randint(0,2,(n,n)) 
    # ou M=rd.binomial(1,2/n,(n,n)) si on veut faire varier les proportions.
    start=time.perf_counter()
    Trans1(M)
    stop=time.perf_counter()
    return(stop-start)

# 4- Dessin de son graphe
import matplotlib.pyplot as plt
X=arange(10,100,1)
Y=[temps(x) for x in X]  #   Y=temps(X) ne fonctionne pas car la fonction temps ne s'applique pas à une liste.
plt.figure(1)            # permet d'afficher les graphes sur des figures différentes
plt.plot(X,Y,'s')       # graphe en coordonnées normales, 's' donne des points 
plt.figure(2)
plt.loglog(X,Y,'s')     # graphe ne coordonnées log-log
    

# 5- recherche de l'exposant a tel que temps(n)=ct**a
""" On constate que la représentation graphique en log-log est approximativement linéaire entre 50 et 100. Donc 
la fonction était approximativement polynomiale : ct**a. L'exposant a est la pente de la représentation log-log, donc:"""

a=(log(temps(100))-log(temps(50)))/(log(100)-log(50))
print(a)


# Le resultat est environ 3, alors que la valeur théorique attendue est plutôt 4...
