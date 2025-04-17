#!/usr/bin/env python3
from collections import defaultdict

with open('Input.19') as f:
    Rules,Celulle = f.read().strip().split("\n\n")

Long = len(Celulle)
R = []

for Rule in Rules.split("\n") : 
    Avant = Rule.split()[0]
    Apres = Rule.split()[2]
    for i in range(Long):
        if Avant == Celulle[ i : ( len(Avant) + i)  ] and i > 0 :
            NewC = Celulle[:i] + Apres + Celulle[i+len(Avant):]
            if not(NewC in R) :
                R.append(NewC)
        if Avant == Celulle[ i : ( len(Avant) + i)  ] and i == 0:
            NewC = Apres + Celulle[len(Avant):]
            if not(NewC in R) :
                R.append(NewC)

print(len(R))
