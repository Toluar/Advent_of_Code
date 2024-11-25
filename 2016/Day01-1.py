#!/usr/bin/env python3

with open('Input.01') as f:
    Data = f.read().replace(' ','')

Chemin = Data.split(',')

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
    Position[0] = Position[0] + (X * Pas)
    Position[1] = Position[1] + (Y * Pas)

print(f"{abs(Position[0]) + abs(Position[1])}")

