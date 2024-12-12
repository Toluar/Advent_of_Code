#!/usr/bin/env python3

with open('Input.01') as f:
    Data = [x.strip() for x in f.readlines()]

Col1,Col2 = zip(*[map(int, x.split()) for x in Data])

T1 = sorted(Col1)
T2 = sorted(Col2)

R = 0
for i in range(len(Col1)) :
    R += abs(T1[i] - T2[i])

print(R)
