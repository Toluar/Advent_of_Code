#!/usr/bin/env python3

import copy

#On recupere les donnees initiales
filin = open("Input.7","r")
Crabs = [int(x) for x in filin.read().split(",")]
filin.close()

Nb_crabs=len(Crabs)
print(f"Nombre de crabes : {Nb_crabs}")

Max=0
Min=0
for i in range(Nb_crabs):
    if Crabs[i] > Max:
        Max=Crabs[i]
    Calc = int((Crabs[i] * (Crabs[i] +1)) / 2)
    Min = Min + Calc

print(f"le crabs le plus loin : {Max}")
print(f"init Min : {Min}")

#Boucle pour les steps
for Step in range(Nb_crabs):
    Somme=0
    for i in range(Nb_crabs):
        if Crabs[i] > Step:
            Diff = Crabs[i] - Step
        else:
            Diff = Step - Crabs[i]
        Sommetmp=int((Diff*(Diff+1))/2)
        Somme = Somme + Sommetmp
    if Somme < Min:
        Min = Somme

print(f"Fuel utilise au Min : {Min}")
