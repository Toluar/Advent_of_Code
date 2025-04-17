#!/usr/bin/env python3
from itertools import permutations

with open('Input.09') as f:
    Data = [x.strip() for x in f.readlines()]
    
Villes = []
Trajets = {}
Mini = 0

for Lines in Data :
    L = Lines.split()
    V1 = L[0]
    if not(V1 in Villes):
        Villes.append(V1)
    V2 = L[2]
    if not(V2 in Villes):
        Villes.append(V2)
    D = int(L[4])
    Mini += D
    Trajets[(V1,V2)] = D
    Trajets[(V2,V1)] = D

for V in permutations(Villes):
    Somme = 0
    for i in range(len(V)-1):
        Dist = Trajets[(V[i],V[i+1])]
        Somme += Dist
    if Somme < Mini :
        Mini = Somme
print(Mini)
