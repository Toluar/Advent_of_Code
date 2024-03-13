#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.2') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0

for Lignes in Data :
    IndLigne,Ligne = Lignes.split(":")
    Ligne = Ligne.split(";")

    MaxDesRed = 0
    MaxDesGreen = 0
    MaxDesBlue = 0
    for Sets in Ligne:
        Tirages = Sets.split(",")
        for Des in Tirages :
            if Des.count("red") > 0:
                NbDesRed = int(Des.replace("red","").replace(" ",""))
                if NbDesRed > MaxDesRed :
                    MaxDesRed = NbDesRed
            if Des.count("green") > 0:
                NbDesGreen = int(Des.replace("green","").replace(" ",""))
                if NbDesGreen > MaxDesGreen :
                    MaxDesGreen = NbDesGreen
            if Des.count("blue") > 0:
                NbDesBlue = int(Des.replace("blue","").replace(" ",""))
                if NbDesBlue > MaxDesBlue :
                    MaxDesBlue = NbDesBlue
    Produit = MaxDesRed * MaxDesGreen * MaxDesBlue
    Somme = Somme + Produit

print(Somme)
