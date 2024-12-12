#!/usr/bin/env python3
import re

with open('Input.03') as f:
    Data = f.read()

Somme = 0
Enable = True
for T,x,y in re.findall( "(mul\((\d+),(\d+)\)|do\(\)|don't\(\))" , Data ):
    if T == "do()":
        Enable = True
    elif T == "don't()":
        Enable = False
    elif Enable == True :
        Somme += int(x) * int(y)

print(Somme)

