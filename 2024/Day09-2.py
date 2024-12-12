#!/usr/bin/env python3

with open("Input.09") as f:
    Data = list(map(int, f.read().strip()))

Blocks = []
Dernier = 0
for i, D in enumerate(Data):
    if not i % 2:
        Blocks.append((i // 2, Dernier, Dernier + D))
    Dernier += D


for TestBlock in range(i // 2, -1, -1):
    Block = next(B for B in Blocks if B[0] == TestBlock)
    _, Start, End = Block
    Espace = End - Start
    for i, ((_, _, End1), (_, Start2, _)) in enumerate(zip(Blocks, Blocks[1:])):
        if End1 == End:
            break
        if Start2 - End1 >= Espace:
            Blocks.insert(i + 1, (TestBlock, End1, End1 + Espace))
            Blocks.remove(Block)
            break

print(
    sum(
        Block_id * Index
        for Block_id, Start, End in Blocks
        for Index in range(Start, End)
    )
)

