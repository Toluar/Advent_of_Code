#!/usr/bin/env python3
from itertools import permutations

with open('Input.13') as f:
    Data = [x.strip() for x in f.readlines()]
    
Personnes = []
Happiness = {}
Max = 0

for Lines in Data :
    L = Lines.split()
    P1 = L[0]
    if not(P1 in Personnes):
        Personnes.append(P1)
    P2 = L[10].replace(".","")
    if not(P2 in Personnes):
        Personnes.append(P2)
    H = int(L[3])
    if L[2] == "gain" :
        Happiness[(P1,P2)] = H
    else: 
        Happiness[(P1,P2)] = -H

for P in Personnes :
    Happiness[(P,"Moi")] = 0
    Happiness[("Moi",P)] = 0
Personnes.append("Moi")


for P in permutations(Personnes):
    S = 0
    for i in range(len(P)-1):
        S += Happiness[(P[i],P[i+1])]
        S += Happiness[(P[i+1],P[i])]
    S += Happiness[(P[len(P)-1],P[0])]
    S += Happiness[(P[0],P[len(P)-1])]
    if S > Max:
        Max = S

print(Max)
