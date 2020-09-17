import numpy as np 
import math
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
#Semaine 2, Equation d'onde 1D
c=300 #m/s
L=100 #m
n=100 #nombre de cellules dans le maillage sans compter les cellules fantome
DeltaX=L/n
CFL=1
DeltaT=DeltaX/c*CFL
# 1. Lecture d'un maillage et mise en donnee d'un maillage
# Calcul du nombre de pas de temps necessaire pour faire une boucle
nbrpasdetemps=round((L/c)/(DeltaT))
# --------------------------------------------------------------------------
# Backward
# Initialisation de la matrice U
n_fantome=2
nb_cellules=n+n_fantome
U=np.zeros((nb_cellules,nbrpasdetemps))

# Conditions initiales
indice=41
for i in range(21):
    U[indice+i,0]=100

    
for i in range(nbrpasdetemps-1):
    for j in range(n):
        U[j+1,i+1]=U[j+1,i]-c*DeltaT/DeltaX*(U[j+1,i]-U[j,i])
        U[0,i+1]=U[n,i+1]
        U[-1,i+1]=U[1,i+1]

        
X=np.linspace(0,100,100)
U_backward=np.delete(U,0,0)
U_backward=np.delete(U_backward,-1,0)
t_interet=5/60
indice_interet=round(t_interet/DeltaT)
#Graphique
plt.figure(figsize=(15,10))
plt.plot(X,U_backward[:,indice_interet],label='Backward',color='blue')
plt.show()