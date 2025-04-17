#!/usr/bin/env python3

with open('Input.14') as f:
    Data = [x.strip() for x in f.readlines()]
    
Rennes = {}
Distances = []
Max = 0
Duree = 2503

for Lines in Data :
    L = Lines.split()
    R = {}
    R["Vit"] = int(L[3])
    R["DA"] = int(L[6])
    R["Repos"] = int(L[13])
    R["Nom"] = L[0]
    Rennes[L[0]]=R
    

for X in Rennes :
    D = Rennes[X]["DA"]
    R = Rennes[X]["Repos"]
    V = Rennes[X]["Vit"]
    A = int(Duree) // (D+R)
    Reste = Duree - (A*(D+R))
    if Reste > D :
        S = (A*V*D) + (D*V)
    else:
        S = (A*V*D) + (V*Reste)
    Distances.append(S)

print(max(Distances))
