#!/usr/bin/env python3

with open('Input.05') as f:
    Data = f.readlines()


def Test_Interdit(s):
    r = True
    for i in range(len(s)-1):
        T = s[i]+s[i+1]
        if T == 'ab' or T == 'cd' or T == 'pq' or T == 'xy':
            r = False
    return r

def Test_Voyelles(s):
    NbV = 0
    for C in s:
        if C == 'a' or C == 'e' or C == 'i' or C == 'o' or C == 'u' :
            NbV += 1
    return NbV > 2

def Test_Doubles(s):
    R = False
    for i in range(len(s) -1):
        if s[i] == s[i+1] :
            R = True
    return R



Somme = 0
for L in Data :
    if Test_Interdit(L) and Test_Voyelles(L) and Test_Doubles(L) :
        Somme += 1

print(Somme)
