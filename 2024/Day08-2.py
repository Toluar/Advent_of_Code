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

Antinodes = []
for C in Caracteres.values() :
    for Droite in permutations(C,2):
        if not (Droite[0] in Antinodes ):
            Antinodes.append(Droite[0])
        if not (Droite[1] in Antinodes ):
            Antinodes.append(Droite[1])
        Diff = Droite[0] - Droite[1]
        P = Droite[1]
        while True:
            Antinode = P - Diff
            if Antinode in Grille:
                if not(Antinode in Antinodes):
                    Antinodes.append(Antinode)
            else :
                break
            P = P - Diff

print(len(Antinodes))
