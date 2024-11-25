#!/usr/bin/env python3

with open('Input.02') as f:
    Data = f.readlines()

Pos = [1,1]
Clavier=[[1,2,3],[4,5,6],[7,8,9]]

for L in Data:
    for C in L :
        if C == 'R' : 
            Pos[0] = min(Pos[0] +1 , 2)
        elif C == 'L' :
            Pos[0] = max(Pos[0] -1 , 0)
        elif C == 'U' :
            Pos[1] = max(Pos[1] -1 , 0)
        elif C == 'D' :
            Pos[1] = min(Pos[1] +1 , 2)
    print(Clavier[Pos[1]][Pos[0]])

