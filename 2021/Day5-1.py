#!/usr/bin/env python3

TailleGrille = 10
Plaine = [[0] * TailleGrille for i in range(TailleGrille)]

Filin = open("Input.5","r")
for Vent in Filin:

    if len(Vent) > 5:
        indAx = int(Vent.replace(" -> ",",").replace("\n","").split(",")[0])
        indAy = int(Vent.replace(" -> ",",").replace("\n","").split(",")[1])
        indBx = int(Vent.replace(" -> ",",").replace("\n","").split(",")[2])
        indBy = int(Vent.replace(" -> ",",").replace("\n","").split(",")[3])
        
        MaxX = indAx
        MaxY = indAy
        MinX = indBx
        MinY = indBy

        if indBx > indAx:
            MaxX = indBx
            MinX = indAx
        if indBy > indAy:
            MaxY = indBy
            MinY = indAy

        if indAx == indBx :
            for i in range(MinY,MaxY+1):
                Plaine[indAx][i] += 1
        if indAy == indBy :
            for i in range(MinX,MaxX+1):
                Plaine[i][indAy] += 1
Filin.close()

Zone = 0
for x in range(TailleGrille):
    for y in range(TailleGrille):
        if Plaine[x][y] > 1:
            Zone += 1
print(f"Resultat : {Zone}")
