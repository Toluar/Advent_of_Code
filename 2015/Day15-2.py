#!/usr/bin/env python3
from itertools import permutations

with open('Input.15') as f:
    Data = [x.strip() for x in f.readlines()]

def Calcul(a,b,c,d):
    P = 1
    C = int(a*I[0]["c"] + b*I[1]["c"] + c*I[2]["c"] + d*I[3]["c"] )
    if C < 0:
        C = 0
    D = int(a*I[0]["d"] + b*I[1]["d"]  + c*I[2]["d"] + d*I[3]["d"] )
    if D < 0:
        D = 0
    F = int(a*I[0]["f"] + b*I[1]["f"] + c*I[2]["f"] + d*I[3]["f"] )
    if F < 0:
        F = 0
    T = int(a*I[0]["t"] + b*I[1]["t"] + c*I[2]["t"] + d*I[3]["t"] )
    if T < 0:
        T = 0
    P = C*D*F*T
    return P

I = {}
ind = 0

for Lines in Data :
    L = Lines.replace(',','').split()
    Nom = L[0].replace(':','')
    R = {}
    R["c"] = int(L[2])
    R["d"] = int(L[4])
    R["f"] = int(L[6])
    R["t"] = int(L[8])
    R["z"] = int(L[10])
    I[ind]=R
    ind += 1

Max = 0
for w in range(101):
    for x in range(101-w):
        for y in range(101-w-x):
            z = 100 - w - x - y
            if ((w*I[0]["z"]) + (x*I[1]["z"]) + (y*I[2]["z"]) + (z*I[3]["z"])) == 500:
                R = int(Calcul(w,x,y,z))
                if Max < R:
                    Max = R
print(Max)
