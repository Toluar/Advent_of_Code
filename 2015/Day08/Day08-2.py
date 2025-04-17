#!/usr/bin/env python3

with open('Input.08') as f:
    Data = [x.strip() for x in f.readlines()]

Somme = 0
for Lines in Data :
    Somme += 2
    for C in Lines :
        if C == '\\' or C == '"':
            Somme += 1

print(Somme)
