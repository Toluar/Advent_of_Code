#!/usr/bin/env python3

with open('Input.14') as f:
    Data = [x.strip() for x in f.readlines()]

def Winner(d):
    Max = 0
    W = 0
    for X in Rennes :
        D = Rennes[X]["DA"]
        R = Rennes[X]["Repos"]
        V = Rennes[X]["Vit"]
        Ind = int(Rennes[X]["Ind"])
        A = int(d) // (D+R)
        Reste = d - (A*(D+R))
        if Reste > D :
            S = (A*V*D) + (D*V)
        else:
            S = (A*V*D) + (V*Reste)
        Distances[Ind] = S
        if S > Max :
            W = Ind
            Max = S
    Points[W] += 1


Rennes = {}
Distances = []
Points = []
Max = 0
Duree = 2504
i = 0

for Lines in Data :
    L = Lines.split()
    R = {}
    R["Vit"] = int(L[3])
    R["DA"] = int(L[6])
    R["Repos"] = int(L[13])
    R["Nom"] = L[0]
    R["Ind"] = i
    Rennes[L[0]]=R
    i += 1
    Distances.append(0)
    Points.append(0)

for i in range(1,Duree):
    Winner(i)

print(max(Points))
