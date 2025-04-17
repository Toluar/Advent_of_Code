#!/usr/bin/env python3

with open('Input.01') as f:
    Data = f.read()

Up = Data.count('(')
Down = Data.count(')')

r = Up - Down
print(r)

