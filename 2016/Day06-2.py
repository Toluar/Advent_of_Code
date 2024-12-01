#!/usr/bin/env python3
from collections import Counter

with open('Input.06') as f:
    Data = [x.strip() for x in f.readlines()]

Grille = []
Long = len(Data[0])

#Initialisation de la grille de tableau
for i in range(Long):
    T = []
    Grille.append(T)

#On rempli la grille de tableau
for Line in Data : 
    for i in range(len(Line)):
        Grille[i].append(Line[i])

for Tab in Grille:
    Ct = Counter(Tab).most_common()
    C = Ct[len(Ct)-1]
    print(C[0][0])

