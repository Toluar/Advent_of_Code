#!/usr/bin/env python3

with open('Input.05') as f:
    Data = f.readlines()

lower_case = list(map(chr, range(65+32, 65+32+26)))

def Test_Paire(s):
    R = False
    for i in range(len(s) - 2):
        if s[i:i+2] in s[i+2:]:
            R = True
    return R

def Test_B(s):
    R = False
    for i in range(len(s) -2):
        if s[i] == s[i+2] :
            R = True
    return R

Somme = 0
for L in Data :
    if (Test_Paire(L) == True) and (Test_B(L) == True):
        Somme += 1

print(Somme)
