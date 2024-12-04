#!/usr/bin/env python3

with open('Input.04') as f:
    Data = [x.strip() for x in f.readlines()]

Somme = 0

L = len(Data)
C = len(Data[0])

for i in range(L) :
    for j in range(C):
        if Data[i][j] == "X" :
#Horizontal
            if j < (C - 3 ):
                if Data[i][j+1] == "M" and Data[i][j+2] == "A" and Data[i][j+3] == "S" :
                    Somme += 1
            if j > 2 :
                if Data[i][j-1] == "M" and Data[i][j-2] == "A" and Data[i][j-3] == "S" :
                    Somme += 1
#Vertical
            if i < (L - 3 ):
                if Data[i+1][j] == "M" and Data[i+2][j] == "A" and Data[i+3][j] == "S" :
                    Somme += 1
            if i > 2 :
                if Data[i-1][j] == "M" and Data[i-2][j] == "A" and Data[i-3][j] == "S" :
                    Somme += 1
#Diagonale
            if i <(L - 3 ) and j < (C - 3 ) :
                if Data[i+1][j+1] == "M" and Data[i+2][j+2] == "A" and Data[i+3][j+3] == "S" :
                    Somme += 1
            if i <(L - 3 ) and j > 2 :
                if Data[i+1][j-1] == "M" and Data[i+2][j-2] == "A" and Data[i+3][j-3] == "S" :
                    Somme += 1
            if i > 2 and j < (C - 3 ) :
                if Data[i-1][j+1] == "M" and Data[i-2][j+2] == "A" and Data[i-3][j+3] == "S" :
                    Somme += 1
            if i > 2 and j > 2 :
                if Data[i-1][j-1] == "M" and Data[i-2][j-2] == "A" and Data[i-3][j-3] == "S" :
                    Somme += 1




print(Somme)
