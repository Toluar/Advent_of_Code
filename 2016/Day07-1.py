#!/usr/bin/env python3

with open('Input.07') as f:
    Data = [x.strip() for x in f.readlines()]

def Test_IP(Str):
    InCrochet = False
    i = 0
    ABBA = False
    MessageHS = False
    for i in range(len(Str)):
        if Str[i] == '[' :
            InCrochet = True
        if Str[i] == ']' :
            InCrochet = False
        if i > 2 :
            if Str[i] == Str[i-3] and Str[i-1] == Str[i-2] and not (Str[i] == Str[i-1]) :
                if InCrochet == False:
                    ABBA = True
                if InCrochet == True:
                    MessageHS = True
    return (ABBA and not MessageHS)

Sum = 0
for Line in Data:
    T = Test_IP(Line)
    if T == True:
        Sum += 1

print(Sum)
