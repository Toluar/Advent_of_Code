#!/usr/bin/env python3

Profondeur = 0
Position = 0

filin = open("Input.2", "r")
for i,line in enumerate(filin) :
    Deplacement,_V = line.split()
    Valeur = int(_V)
    if Deplacement == "forward" :
        Position += Valeur
    if Deplacement == "down" :
        Profondeur += Valeur
    if Deplacement == "up" :
        Profondeur -= Valeur
filin.close

print(f"Profondeur : {Profondeur} et Position : {Position}")
Resultat = Profondeur * Position
print(f"Le resultat est : {Resultat}")


