#!/usr/bin/env python3

with open('Input.02') as f:
    Data = f.readlines()

Somme = 0
for Lines in Data:
    a,b,c = Lines.strip().split("x")
    A = int(a)
    B = int(b)
    C = int(c)
    S = A*B*C + 2*(A+B+C-max(A,B,C)) 
    Somme += S

print(Somme)
