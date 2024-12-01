#!/usr/bin/env python3

with open('Input.07') as f:
    Data = [x.strip() for x in f.readlines()]

def Test_IP(Str):
    InCrochet = False
    i = 0
    ABA = []
    BAB = []

    for i in range(len(Str)):
        if Str[i] == '[' :
            InCrochet = True
        elif Str[i] == ']' :
            InCrochet = False
        elif not InCrochet:
            if i > 1:
                if Str[i] == Str[i-2] and not (Str[i] == Str[i-1]) :
                    ABA.append((Str[i],Str[i-1]))
        elif InCrochet:
            if i > 1 :
                if Str[i] == Str[i-2] and not (Str[i] == Str[i-1]) :
                    BAB.append((Str[i-1],Str[i]))
    T = bool(set(ABA).intersection(BAB))
    return (T)

Sum = 0
for Line in Data:
    T = Test_IP(Line)
    if T == True:
        Sum += 1

print(Sum)
