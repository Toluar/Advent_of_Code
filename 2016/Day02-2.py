#!/usr/bin/env python3

with open('Input.02') as f:
    Data = f.readlines()

X = 0
Y = 2
Clavier=[['.','.',1,'.','.'],['.',2,3,4,'.'],[5,6,7,8,9],['.','A','B','C','.'],['.','.','D','.','.']]

for L in Data:
    for C in L :
        if C == 'R' : 
            XR = min(X+1,4)
            if Clavier[Y][XR] != '.' :
                X = XR
        elif C == 'L' :
            XR = max(X-1,0)
            if Clavier[Y][XR] != '.' :
                X = XR
        elif C == 'U' :
            YR = max(Y-1,0)
            if Clavier[YR][X] != '.' :
                Y = YR
        elif C == 'D' :
            YR = min(Y+1,4)
            if Clavier[YR][X] != '.' :
                Y = YR
    print(Clavier[Y][X])

