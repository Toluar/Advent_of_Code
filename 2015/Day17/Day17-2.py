#!/usr/bin/env python3
from itertools import combinations

with open('Input.17') as f:
    Data = [int(x) for x in f.readlines()]

TOTAL = 150

R = 0
MINI = len(Data)
for i in range(2,len(Data)):
    for Test in combinations(Data,i):
        if sum(Test) == TOTAL :
            if i < MINI : 
                MINI = i
                R = 0
            if i == MINI :
                R += 1

print(R)    
