#!/usr/bin/env python3

with open('Input.04') as f:
    Data = [x.strip() for x in f.readlines()]

Somme = 0

L = len(Data)
C = len(Data[0])

for i in range(1,L-1) :
    for j in range(1,C-1):
        if Data[i][j] == "A" :
#Diagonale
            if Data[i+1][j+1] == "M" and Data[i-1][j-1] == "S" and Data[i+1][j-1] == "M" and Data[i-1][j+1] == "S" :
                Somme += 1
            if Data[i+1][j+1] == "M" and Data[i-1][j-1] == "S" and Data[i+1][j-1] == "S" and Data[i-1][j+1] == "M" :
                Somme += 1
            if Data[i-1][j-1] == "M" and Data[i+1][j+1] == "S" and Data[i+1][j-1] == "M" and Data[i-1][j+1] == "S" :
                Somme += 1
            if Data[i-1][j-1] == "M" and Data[i+1][j+1] == "S" and Data[i+1][j-1] == "S" and Data[i-1][j+1] == "M" :
                Somme += 1

print(Somme)
