#!/usr/bin/env python3

with open('Input.02') as f:
    Data = f.readlines()

Somme = 0
for Lines in Data:
    a,b,c = Lines.strip().split("x")
    S = (2*int(a)*int(b)) + (2*int(b)*int(c)) + (2*int(c)*int(a)) + int((int(a)*int(b)*int(c))/max(int(a),int(b),int(c)))
    Somme += S

print(Somme)
