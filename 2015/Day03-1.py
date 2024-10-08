#!/usr/bin/env python3

with open('Input.03') as f:
    Data = f.read()

Maison = {(0,0):"1"}
PosX = 0
PosY = 0

for C in Data :
    if C == '^':
        PosY += 1
    elif C == '>':
        PosX += 1
    elif C == '<':
        PosX += -1
    else:
        PosY += -1
    Maison[(PosX,PosY)] = 1

print(len(Maison))
