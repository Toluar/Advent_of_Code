#!/usr/bin/env python3
import re
from collections import Counter

with open('Input.04') as f:
    Data = f.readlines()

R = 0
for T in Data :
    M = re.match('(.*)-(\d*)\[(\w{5})\]',T)
    Check = M.groups(0)[2]
    Code = int(M.groups(0)[1])
    S = sorted(M.groups(0)[0].replace('-',''))
    C = Counter(S).most_common(5)

    CheckSum = "".join([X[0] for X in C])

    if CheckSum == Check :
        R += Code

print(R)
