#!/usr/bin/env python3
from collections import Counter

with open('Input.01') as f:
    Data = [x.strip() for x in f.readlines()]

Col1,Col2 = zip(*[map(int, x.split()) for x in Data])

A = sorted(Col1)
B = sorted(Col2)

C = Counter(B)
R = 0
for i in range(len(A)):
    R += A[i] * C[A[i]]

print(R)
