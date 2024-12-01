#!/usr/bin/env python3

with open('Input.03') as f:
    Data = f.readlines()

R = 0
for i in range(len(Data)//3):
    T1 = []
    T2 = []
    T3 = []
    for x in range(3):
        A,B,C = Data[(i*3)+x].split()
        T1.append(int(A))
        T2.append(int(B))
        T3.append(int(C))
    if (T1[0]+T1[1]+T1[2]-max(T1)) > max(T1) : 
        R+= 1
    if (T2[0]+T2[1]+T2[2]-max(T2)) > max(T2) :
        R+= 1
    if (T3[0]+T3[1]+T3[2]-max(T3)) > max(T3) : 
        R+= 1

print(R)


