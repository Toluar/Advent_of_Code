#!/usr/bin/env python3

Profondeur = 0
Position = 0
Aim = 0

filin = open("Input.2", "r")
for i,line in enumerate(filin) :
    Deplacement,_V = line.split()
    Valeur = int(_V)
    if Deplacement == "forward" :
        Position += Valeur
        Profondeur = Profondeur + (Aim*Valeur)
    if Deplacement == "down" :
        Aim += Valeur
    if Deplacement == "up" :
        Aim -= Valeur
filin.close

print(f"Profondeur : {Profondeur} et Position : {Position}")
Resultat = Profondeur * Position
print(f"Le resultat est : {Resultat}")


