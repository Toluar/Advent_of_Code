#!/usr/bin/env python3
from collections import Counter


#On recupere les donnees initiales
with open('Input.7') as file:
    Data = [i for i in file.read().strip().split("\n")]

Hand = []
Pts = []
mytable = str.maketrans("23456789TJQKA","ABCDEFGHIJKLM")

for D in Data :
	H,P = D.split()
	M = H.translate(mytable)
	HS = sorted(H)
	C = sorted((Counter(HS)).values())
	C5 = C.count(5)
	C4 = C.count(4)
	C3 = C.count(3)
	C2 = C.count(2)
	C1 = C.count(1)
	Rang = 0
	if C5 == 1 :
		Rang = 7
	elif C4 == 1 : 
		Rang = 6
	elif C3 == 1 and C2 == 1 :
		Rang = 5
	elif C3 == 1 and C1 == 2 :
		Rang = 4
	elif C2 == 2 : 
		Rang = 3
	elif C2 == 1 :
		Rang = 2
	else :
		Rang = 1
	NM = str(Rang) + M
	Hand.append((H,P,NM))
	Pts.append(int(P))

Hand.sort(key=lambda x: x[2])
i = 0
Somme = 0
for Elm in Hand :
	i = i+1
	Somme = Somme + ( i * int(Elm[1]) )

print(Somme)	
