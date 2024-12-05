#!/usr/bin/env python3
from collections import Counter

with open('Input.01') as f:
    Data = [x.strip() for x in f.readlines()]

Col1,Col2 = zip(*[map(int, x.split()) for x in Data])

T1 = sorted(Col1)
T2 = sorted(Col2)

C = Counter(T2)
R = 0
for i in range(len(T1)):
    R += T1[i] * C[T1[i]]

print(R)
