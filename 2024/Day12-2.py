#!/usr/bin/env python3

with open("Input.12") as f:
    Data = f.read().strip().split("\n")
    
Grille = {(i,j) : x for i, D in enumerate(Data) for j, x in enumerate(D)}

Visite = set()
Regions = []


def Compte_Bord(B,IND):
    Cotes = 0
    T = [x for x in B]
    T = sorted(T , key=lambda tup: tup[(IND+1)%2] )
    while T:
        Premier = T.pop(0)
        if len(T) == 0:
            Cotes += 1
            continue
        Identique = False
        for E in T:
            if Premier[IND] == E[IND] :
                if  (Premier[(IND+1)%2] +1 == E[(IND+1)%2] ):
                    Identique = True
        if Identique == False:
            Cotes += 1
    return Cotes                
    

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
for i,Region in enumerate(Regions):
    Aire = len(Region)
    Cotes = 0
    Perimetre = {"Haut":set(),"Bas":set(),"Gauche":set(),"Droite":set()}
    for y,x in Region:
        HY = y - 1
        BY = y + 1
        GX = x - 1
        DX = x + 1
        if (y-1,x) not in Region :
            Perimetre["Haut"].add((y,x))
        if (y+1,x) not in Region :
            Perimetre["Bas"].add((y,x))
        if (y,x-1) not in Region :
            Perimetre["Gauche"].add((y,x))
        if (y,x+1) not in Region :
            Perimetre["Droite"].add((y,x))
    H = Compte_Bord(Perimetre["Haut"],0)
    B = Compte_Bord(Perimetre["Bas"],0)
    G = Compte_Bord(Perimetre["Gauche"],1)
    D = Compte_Bord(Perimetre["Droite"],1)
    Cotes = H + B + G + D
    Somme += Aire * Cotes

print(Somme)

