#!/usr/bin/env python3

with open('Input.16') as f:
    Data = [x.strip().replace(':','').replace(',','').split() for x in f.readlines()]

D = {}
for l in Data:
    D[int(l[1])] = {l[2]: int(l[3]), l[4]: int(l[5]), l[6]: int(l[7])}

Tante = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

Inferieur = {'cats','trees'}
Superieur = {'pomeranians','goldfish'}

for Aunt,Items in D.items():
    Trouve = True
    for (Item,Count) in Items.items():
        if Item in Inferieur :
            if Count <= Tante[Item]:
                Trouve = False
                break
        elif Item in Superieur :
            if Count >=  Tante[Item]:
                Trouve = False
                break
        else :
            if Count != Tante[Item]:
                Trouve = False
                break
    if Trouve :
        print(Aunt)
        break



    
