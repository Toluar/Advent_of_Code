#!/usr/bin/env python3

import copy


Nb_jours=256



#On recupere les donnees initiales
filin = open("Input.6","r")
data = [int(x) for x in filin.read().split(",")]
filin.close()

#On cree le tableaux
poissons = []
for i in range(9):
    poissons.append(0)

somme=0
for poisson in data:
    poissons[poisson]=poissons[poisson]+1
    somme=somme+1 



poissonsOld=copy.copy(poissons)
for Day in range(Nb_jours):
    poissons[8]=poissonsOld[0]
    poissons[7]=poissonsOld[8]
    poissons[6]=poissonsOld[7]+poissonsOld[0]
    poissons[5]=poissonsOld[6]
    poissons[4]=poissonsOld[5]
    poissons[3]=poissonsOld[4]
    poissons[2]=poissonsOld[3]
    poissons[1]=poissonsOld[2]
    poissons[0]=poissonsOld[1]
    poissonsOld=copy.copy(poissons)

somme=0
for i in range(9):
    somme=somme+poissons[i]

print(f"Somme : {somme} <= {poissons}")
