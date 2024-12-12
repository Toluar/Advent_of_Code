#!/usr/bin/env python3

with open("Input.09") as f:
    Data = list(map(int, f.read().strip()))

Blocks = []
for i,D in enumerate(Data):
    Blocks += [None if i%2 else i//2] * D

Position = Data[0]
while Position < len(Blocks):
    if Blocks[Position] :
        Position += 1
    else:
        Dernier = Blocks.pop()
        if Dernier :
            Blocks[Position] = Dernier

print(sum(i*B for i,B in enumerate(Blocks)))
