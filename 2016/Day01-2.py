#!/usr/bin/env python3

with open('Input.01') as f:
    Data = f.read().replace(' ','')

Chemin = Data.split(',')

MAXX = 1000
RX = 0
Grille = []

for i in range(MAXX) :
    L = []
    for j in range(MAXX) :
        L.append(0)
    Grille.append(L)

#On regarde au Nord 
X = 0
Y = 1
Position=[0,0]

for Step in Chemin :
    if Step[0] == 'R' :
        if X == 0 :
            X = Y
            Y = 0
        else :
            Y = -X
            X = 0
    else:
        if X == 0 :
            X = -Y
            Y = 0
        else:
            Y = X
            X = 0
    Pas = int(Step[1:])
    for i in range(Pas):
        GX = Position[0] + (X * i)
        GY = Position[1] + (Y * i)
        Grille[GX][GY] += 1
        if Grille[GX][GY] == 2 and RX == 0:
            RX = abs(GX) + abs(GY)
            print(RX)

    Position[0] = Position[0] + (X * Pas)
    Position[1] = Position[1] + (Y * Pas)

