#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.1') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0
for Ligne in Data:
    FirstNum = False
    LastNum = False
    FN = 0
    LN = 0
    for Lettre in Ligne :
        if Lettre.isdigit():
            if FirstNum == False :
                FirstNum = True
                FN = str(Lettre)
                LN = str(Lettre)
            else : 
                LN = str(Lettre)
    Nb = int(FN + LN)
    Somme = Somme + Nb

print(Somme)
