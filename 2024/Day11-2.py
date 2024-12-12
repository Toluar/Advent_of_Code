#!/usr/bin/env python3

with open("Input.11") as f:
    Data = list(map(int, f.read().strip().split()))

NB_STEP = 75

Historique = {}
def Step(N,t):
    #Pour l historique on va souvent chercher 0,1,2024,2,0,2,4, .... Ca va eviter de tout recalculer
    if (N,t) in Historique:
        return Historique[(N,t)]
    if t == 0:
        return 1
    else:
        if N == 0:
            R = Step(1,t-1)
        elif (len(str(N))%2) == 0:
            S = str(N)
            M = len(S)//2
            R1 = Step(int(S[:M]),t-1)
            R2 = Step(int(S[M:]),t-1)
            R = R1+R2
        else:
            R = Step(N*2024,t-1)
    Historique[(N,t)] = R
    return R

Somme = 0
for D in Data:
    Somme += Step(D,NB_STEP)
print(Somme)

