#!/usr/bin/env python3

with open('Input.08.t') as f:
    Data = [x.strip() for x in f.readlines()]

XMAX = 7
YMAX = 3
Grille = []

for i in range(YMAX):
    L = []
    for j in range(XMAX):
        L.append(0)
    Grille.append(L)

for Line in Data :
    print(Line)
    Cmd = Line.split()[0]
    if Cmd == "rect" :
       X,Y = Line.split()[1].split("x")
       for i in range(int(Y)) :
           for j in range(int(X)):
               Grille[i][j] = 1
    elif Cmd == "rotate":
        Sens = Line.split()[1]
        if Sens == "column":
            Numero = int(Line.split()[2].replace("x=",""))
            Swift = int(Line.split()[4])
            print(f"X : {Numero} et {Swift}")
            for i in range(YMAX):
                
                Grille[i][Numero] = Grille[(i+Swift)%YMAX][Numero]

    print(Grille)            


