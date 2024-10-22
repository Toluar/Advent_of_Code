#!/usr/bin/env python3

Data = 'vzbxkghb'

def Test_ABC(s):
    R = False
    for i in range(len(s)-2):
        if (ord(s[i]) == (ord(s[i+1]) -1 )) and (ord(s[i]) == (ord(s[i+2]) -2)):
            R = True
    return R

def Test_IOL(s):
    R = True
    for i in range(len(s)):
        if s[i] in {'i','o','l'}:
            R = False
    return R

def Test_Double(s):
    R = False
    Count = 0
    for i in range(len(s)-2):
        if (s[i+1] == s[i+2]) and (s[i] != s[i+1]) :
            Count += 1
    if Count >1 :
        R = True
    return R

def Increase( s , i ):
    if s[i] == 'z':
        s[i] = 'a'
        Increase( s , i-1 )
    else:
        s[i] = chr(ord(s[i]) + 1)

R = False
D = list(Data)
while R == False:
    Data = Increase( D, len(D)-1 )
    if Test_ABC(D) and Test_IOL(D) and Test_Double(D) : 
        R = True

print(D)


