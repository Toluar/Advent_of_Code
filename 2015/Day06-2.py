#!/usr/bin/env python3

with open('Input.06') as f:
    Data = f.readlines()

MaxGrille = 1000

Cube = []
for i in range(MaxGrille):
    Z = []
    for j in range(MaxGrille):
        Z.append(0)
    Cube.append(Z)
    
for Lines in Data :
    W = Lines.split()
    if W[0] == "toggle":
        SWITCH = "switch"
        MinX = int(W[1].split(",")[0])
        MinY = int(W[1].split(",")[1])
        MaxX = int(W[3].split(",")[0])
        MaxY = int(W[3].split(",")[1])
    else:
        SWITCH = W[1]
        MinX = int(W[2].split(",")[0])
        MinY = int(W[2].split(",")[1])
        MaxX = int(W[4].split(",")[0])
        MaxY = int(W[4].split(",")[1])
    for i in range(MinX,MaxX+1):
        for j in range(MinY,MaxY+1):
            if SWITCH == "on" :
                Cube[i][j] += 1
            elif SWITCH == "off":
                Cube[i][j] = Cube[i][j] -1
                if Cube[i][j] < 0 :
                    Cube[i][j] = 0
            else :
                Cube[i][j] = Cube[i][j] +2

Somme = 0
for i in range(1000):
    for j in range(1000):
        Somme = Somme + Cube[i][j]

print(Somme)
        

