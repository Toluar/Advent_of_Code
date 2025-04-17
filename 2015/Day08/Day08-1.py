#!/usr/bin/env python3

with open('Input.08') as f:
    Data = [x.strip() for x in f.readlines()]

Somme = 0
for Lines in Data :
    Somme += 2
    Escaped = False
    for C in Lines :
        if not Escaped and C == '\\':
            Escaped = True
        elif Escaped :
            if C == '\\' or C == '"':
                Somme += 1
            elif C == 'x' :
                Somme += 3
            Escaped = False

print(Somme)
