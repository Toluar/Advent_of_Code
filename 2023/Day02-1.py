#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.2') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0

NbDes = 39
NbMaxRed = 12
NbMaxGreen = 13
NbMaxBlue = 14

for Lignes in Data :
    Possible = True
    IndLigne,Ligne = Lignes.split(":")
    IndLigne = int(IndLigne.replace("Game ",""))
    Ligne = Ligne.split(";")
    for Sets in Ligne:
        Tirages = Sets.split(",")
        for Des in Tirages :
            if Des.count("red") > 0:
                NbDesRed = int(Des.replace("red","").replace(" ",""))
                if NbDesRed > NbMaxRed:
                    Possible = False
            if Des.count("green") > 0:
                NbDesGreen = int(Des.replace("green","").replace(" ",""))
                if NbDesGreen > NbMaxGreen:
                    Possible = False
            if Des.count("blue") > 0:
                NbDesBlue = int(Des.replace("blue","").replace(" ",""))
                if NbDesBlue > NbMaxBlue :
                    Possible = False
    if Possible :
        Somme = Somme + IndLigne

print(Somme)
