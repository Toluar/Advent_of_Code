#!/usr/bin/env python3

with open('Input.16') as f:
    Data = [x.strip().replace(':','').replace(',','') for x in f.readlines()]

Tante = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for Lines in Data :
    L = Lines.split()
    if (Tante[L[2]] == int(L[3])) and (Tante[L[4]] == int(L[5])) and (Tante[L[6]] == int(L[7])):
        print(L[1])




    
