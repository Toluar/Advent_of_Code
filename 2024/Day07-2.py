#!/usr/bin/env python3

with open("Input.07") as f:
    Data = f.read().strip().split("\n")


def Is_Valid (R,O):
    if len(O) == 1 :
        return( O[0] == R)
    else:
        TA = [O[0]+O[1]] + O[2::]
        TB = [O[0]*O[1]] + O[2::]
        TC = [int(str(O[0]) + str(O[1]))] + O[2::]
        if Is_Valid(R,TA):
            return True
        if Is_Valid(R,TB):
            return True
        if Is_Valid(R,TC):
            return True
    return False

Somme = 0
for Line in Data :
    Resultat,Op = Line.split(':')
    Resultat = int(Resultat)
    Operandes = [int(x) for x in Op.split()]
    if Is_Valid(Resultat,Operandes) :
        Somme += Resultat

print(Somme)
