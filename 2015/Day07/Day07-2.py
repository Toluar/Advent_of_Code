#!/usr/bin/env python3

with open('Input.07') as f:
    Data = [x.strip() for x in f.readlines()]

index = {l.split()[-1]: l for l in Data}
index['b'] = "16076 -> b"

vals = {}

def f(r):
    if r in vals:
        return vals[r]
    l = index[r]
    w = l.split()
    if w[1] == '->':
        ret = int(w[0]) if w[0].isdigit() else f(w[0])
    elif w[0] == 'NOT':
        ret = ~f(w[1])
    elif w[1] == 'AND':
        v1 = int(w[0]) if w[0].isdigit() else f(w[0])
        ret = v1 & f(w[2])
    elif w[1] == 'OR':
        ret = f(w[0]) | f(w[2])
    elif w[1] == 'RSHIFT':
        ret = f(w[0]) >> int(w[2])
    elif w[1] == 'LSHIFT':
        ret = f(w[0]) << int(w[2])
    vals[r] = ret
    return ret


R = f('a')
print(R)
