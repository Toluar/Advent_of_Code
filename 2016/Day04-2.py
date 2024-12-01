#!/usr/bin/env python3
import re
from collections import Counter

with open('Input.04') as f:
    Data = f.readlines()

for T in Data :
    M = re.match('(.*)-(\d*)\[(\w{5})\]',T)
    Check = M.groups(0)[2]
    Code = int(M.groups(0)[1])
    Sold = M.groups(0)[0]

    S = ""
    for c in Sold :
        NewCode = (ord(c) - 97 + Code) %26
        NewC = chr(NewCode + 97)
        S += NewC
    if 'north' in S:
        print(f"{S} => {Code}")

