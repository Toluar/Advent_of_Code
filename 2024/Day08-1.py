#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations

with open("Input.08") as f:
    Data = f.read().strip().split("\n")

Grille = defaultdict(set)
Caracteres = defaultdict(set)
for a in range(len(Data)):
    for b in range(len(Data[0])):
        Grille[b+1j *a ] = Data[a][b]
        if Data[a][b] != ".":
            Caracteres[Data[a][b]].add((b + 1j*a))

Somme = 0
Antinodes = []
for C in Caracteres.values() :
    for Droite in permutations(C,2):
        Antinode = Droite[1] - Droite[0] + Droite[1]
        if Antinode in Grille and not(Antinode in Antinodes):
            Antinodes.append(Antinode)
            Somme += 1

print(Somme)
