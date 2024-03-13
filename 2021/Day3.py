#!/usr/bin/env python3

import copy
filin = open("Day3.input", "r")

Grille = [l.strip() for l in filin]
work = copy.copy(Grille)

filin.close()


def compute(grille, col):
    print(grille)
    count = 0
    for raw in grille:
        if raw[col] == "1":
            count +=1
    Nb0 = len(grille) - count
    print(f"Nb 1 : {count} / Nb 0 : {Nb0}")
    if count >= Nb0:
        return [R for R in grille if R[col] == "1"]
    else: 
        return [R for R in grille if R[col] == "0"]

for i in range(len(Grille[0])) :
    work = compute(work,i)
    if len(work) == 1 :
        break

print(work)

