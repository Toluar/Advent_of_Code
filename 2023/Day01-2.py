#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.1') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0
for Ligne in Data:
    LigneTmp = Ligne
    LigneTmp = LigneTmp.replace("one","one1one")
    LigneTmp = LigneTmp.replace("two","two2two")
    LigneTmp = LigneTmp.replace("three","three3three")
    LigneTmp = LigneTmp.replace("four","four4four")
    LigneTmp = LigneTmp.replace("five","five5five")
    LigneTmp = LigneTmp.replace("six","six6six")
    LigneTmp = LigneTmp.replace("seven","seven7seven")
    LigneTmp = LigneTmp.replace("eight","eight8eight")
    LigneTmp = LigneTmp.replace("nine","nine9nine")

    FirstNum = False
    LastNum = False
    FN = 0
    LN = 0
    for Lettre in LigneTmp :
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
