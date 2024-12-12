#!/usr/bin/env python3

with open("Input.12") as f:
    Data = f.read().strip().split("\n")
    
Grille = {(i,j) : x for i, D in enumerate(Data) for j, x in enumerate(D)}

Visite = set()
Regions = []

for Position, Plantes in Grille.items():
    if Position in Visite:
         continue
    Region = set()
    File = [Position]
    while File:
        Position = File.pop()
        if Position in Visite:
            continue
        Visite.add(Position)
        Region.add(Position)
        x, y = Position
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            Suivants = (x + dx, y + dy)
            if Suivants in Grille and Grille[Suivants] == Plantes:
                File.append(Suivants)
    Regions.append(Region)

Somme = 0
for Region in Regions:
    Aire = len(Region)
    Perimetre = 0
    for x,y in Region:
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (x+dx,y+dy) not in Region:
                Perimetre += 1
    Somme += Aire * Perimetre

print(Somme)
