#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.6') as file:
    DataT,DataD = [i for i in file.read().strip().split("\n")]

Time = int(DataT.split(":")[1].replace(" ",""))
Distance = int(DataD.split(":")[1].replace(" ",""))

Somme = 0
for i in range(Time):
	D = (Time - i) * i
	if D > Distance :
		Somme = Somme +1 
print(Somme)

