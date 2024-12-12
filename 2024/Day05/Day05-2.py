#!/usr/bin/env python3
from collections import defaultdict,deque

with open("Input.05") as f:
    Data = f.read().strip().split("\n\n")

Rules = [tuple(map(int, x.split("|"))) for x in Data[0].split("\n")]
Updates = [tuple(map(int, x.split(","))) for x in Data[1].split("\n")]

#Les regles sont de la forme (X|Y)
#A contient la liste des X pour un Y donne
#B contient la liste des Y pour un X donne
A = defaultdict(set)
B = defaultdict(set)

for Line in Rules:
    x = Line[0]
    y = Line[1]
    A[y].add(x)
    B[x].add(y)

def Test_UnValid(U):
    Valid = False
    for i in range(len(U) -1):
        if (U[i+1],U[i]) in Rules:
            Valid = True
            break
    return Valid

Somme = 0
for Update in Updates :
    if Test_UnValid(Update) :
        Correct = [] #contiendra la solution
        MaFile = deque([]) #contiendra la liste des nombres corrects avant de les ajouter a Correct
        #On créé un dico qui contient la liste des nombres avec le nombres d'iteration en seconde position
        ITERATION = {N:len(A[N] & set(Update)) for N in Update}
        #On initialise la file
        for NB in Update:
            if ITERATION[NB] == 0:
                MaFile.append(NB)
        while MaFile: #Tant que la file contient un element
            #On sort l element qui est correct
            OK = MaFile.popleft()
            Correct.append(OK)
            for N in B[OK] : #On regarde ensuite les possibles en Y dans les regles
                if N in ITERATION: #Si le possible est dans les pages.
                    ITERATION[N] -= 1 #On le rapproche de la sortie
                    if ITERATION[N] == 0: 
                        MaFile.append(N) #Si le nombre est correct on l ajoute a la file pour le sortir
        Somme += Correct[len(Correct)//2]
         
print(Somme)
