#!/usr/bin/env python3

with open('Input.01') as f:
    Data = f.read()

Max = Data.count('(') - Data.count(')')

SousSol = 0
Position = 0
for i in range(len(Data)) :
    if Data[i] == '(':
        Position += 1
    else :
        Position += -1
    if Position == -1 and SousSol == 0:
        SousSol = i + 1

print(SousSol)

