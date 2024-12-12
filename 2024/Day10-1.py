#!/usr/bin/env python3
from collections import deque

with open("Input.10") as f:
    Data = f.read().strip().split("\n")

Grille = [[int(x) for x in D] for D in Data]

def Chemin(L,C):
    Somme = 0
    Parcours = set()
    MaFile = deque([(L,C)])
    while MaFile :
        l,c = MaFile.popleft()
        if (l,c) in Parcours:
            continue
        Parcours.add((l,c))
        if Grille[l][c] == 9 :
            Somme += 1
        for ll,cc in [(-1,0),(0,-1),(1,0),(0,1)]:
            PL = l + ll
            PC = c + cc
            if (PL >= 0) and (PL < len(Data)) and (PC >= 0) and (PC < len(Data[0])) and (Grille[PL][PC] == Grille[l][c] + 1):
                MaFile.append((PL,PC))
    return Somme

SommeF = 0
for L in range(len(Data)):
    for C in range(len(Data[0])):
        if Grille[L][C] == 0:
            SommeF += Chemin(L,C)

print(SommeF)
