#!/usr/bin/env python3

with open('Input.03') as f:
    Data = f.readlines()

R = 0
for L in Data:
    A,B,C = L.split()
    A = int(A)
    B = int(B)
    C = int(C)
    if (A+B+C-max(A,B,C)) > max(A,B,C) :
        R += 1

print(R)
