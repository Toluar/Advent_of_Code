#!/usr/bin/env python3

import copy

#On recupere les donnees initiales
filin = open("Input.8","r")

Somme = 0
for i,Ligne in enumerate(filin):
    Entree = Ligne.strip().split("|")[0].split()
    Affichage = Ligne.strip().split("|")[1].split()
#    print(Affichage)
    for Digit in Affichage :
        Longueur = len(Digit)
        if Longueur == 2 or Longueur == 3 or Longueur == 4 or Longueur == 7 :
            Somme = Somme +1

print(Somme)

