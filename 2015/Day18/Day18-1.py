#!/usr/bin/env python3
from collections import defaultdict

with open('Input.18') as f:
    Data = [x.strip() for x in f.readlines()]

STEP = 100

L = len(Data)
C = len(Data[0])
D = defaultdict(int)
for i in range(L):
    for j in range(C):
        D[j,i] = 1 if Data[i][j] == '#' else 0


def Shift(DA):
    DR = defaultdict(int)
    for i in range(L):
        for j in range(C):
            NB = DA[i-1,j-1] + DA[i-1,j] + DA[i-1,j+1] + DA[i,j-1] + DA[i,j+1] + DA[i+1,j-1] + DA[i+1,j] + DA[i+1,j+1]
            if DA[i,j] == 1 :
                DR[i,j] = 1 if NB == 2 or NB == 3 else 0
            else :
                DR[i,j] = 1 if NB == 3 else 0
    return DR

for _ in range(STEP):
    D = Shift(D)

print(sum(D.values()))
