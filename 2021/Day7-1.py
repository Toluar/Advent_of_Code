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
    Min=Min+Crabs[i]

print(f"le crabs le plus loin : {Max}")
print(f"init Min : {Min}")

#Boucle pour les steps
for Step in range(Nb_crabs):
    Somme=0
    for i in range(Nb_crabs):
        if Crabs[i] > Step:
            Sommetmp = Crabs[i] - Step

        else:
            Sommetmp = Step - Crabs[i]
        Somme = Somme + Sommetmp
    if Somme < Min:
        Min = Somme

print(f"Fuel utilise au Min : {Min}")
