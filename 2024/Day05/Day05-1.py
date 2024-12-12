#!/usr/bin/env python3

with open("Input.05") as f:
    Data = f.read().strip().split("\n\n")

Rules = [tuple(map(int, x.split("|"))) for x in Data[0].split("\n")]
Updates = [tuple(map(int, x.split(","))) for x in Data[1].split("\n")]
    
def Test_Valid(U):
    Valid = True
    for i in range(len(U) -1):
        if (U[i+1],U[i]) in Rules:
            Valid = False
    return Valid

Somme = 0
for Update in Updates :
    if Test_Valid(Update) :
        Somme += Update[len(Update)//2]

print(Somme)
