#!/usr/bin/env python3
import re

with open('Input.03') as f:
    Data = f.read()

Somme = 0
for x,y in re.findall( "mul\((\d+),(\d+)\)" , Data ):
    Somme += int(x) * int(y)

print(Somme)

