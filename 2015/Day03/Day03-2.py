#!/usr/bin/env python3

with open('Input.03') as f:
    Data = f.read()

Maison = {(0,0):"1"}
PosXA = 0
PosYA = 0
PosXB = 0
PosYB = 0

PN = False
for C in Data :
    PN = not(PN)
    if PN :
        if C == '^':
            PosYA += 1
        elif C == '>':
            PosXA += 1
        elif C == '<':
            PosXA += -1
        else:
            PosYA += -1
        Maison[(PosXA,PosYA)] = 1
    else :
        if C == '^':
            PosYB += 1
        elif C == '>':
            PosXB += 1
        elif C == '<':
            PosXB += -1
        else:
            PosYB += -1
        Maison[(PosXB,PosYB)] = 1
        

print(len(Maison))
