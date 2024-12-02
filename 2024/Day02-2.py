#!/usr/bin/env python3
import re

with open('Input.02') as f:
    Data = [x.strip() for x in f.readlines()]

#Conversion en liste de int de toutes les lignes
Lines = [[int(i) for i in re.findall(r'\d+', x)] for x in Data]

def Is_Valid(Line):
    R = False
    Decrease = True
    Increase = True
    Difference = True
    for i in range(len(Line) -1):
        if abs(Line[i+1]-Line[i]) > 3 or Line[i] == Line[i+1] :
            Difference = False
        if int(Line[i+1]) > int(Line[i]):
            Decrease = False
        if int(Line[i+1]) < int(Line[i]):
            Increase = False
    if Difference == True and (Increase == True or Decrease == True):
        R = True
    return R

Somme = 0
for Line in Lines:
    Test = False
    for i in range(len(Line)) :
        L = Line[:i] + Line[i+1:]
        if Is_Valid(L):
            Test = True
    if Test :
        Somme += 1
    
print(Somme)
