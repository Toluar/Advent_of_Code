#!/usr/bin/env python3

Data = '1321131112'
NbLoop = 40


def TPascal(s):
    new_s = ''
    c = 0
    curr = s[0]
    for i in range(len(s)):
        if (i > 0 and s[i] != curr):
            new_s += f'{c}{s[i-1]}'
            curr = s[i]
            c = 0
        c += 1
    new_s += f'{c}{curr}'
    return new_s           

            
for _ in range(NbLoop):
    Data = TPascal(Data)

print(len(Data))


