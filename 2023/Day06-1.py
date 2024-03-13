#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.6') as file:
    DataT,DataD = [i for i in file.read().strip().split("\n")]

Time = [int(x) for x in DataT.split(":")[1].split()]
Distance = [int(x) for x in DataD.split(":")[1].split()]

Produit = 1
for i in range(len(Time)) :
	Duree = Time[i]
	Somme = 0
	for T in range(1,Duree,1):
		D = (Duree - T) * T
		if D > Distance[i] :
			Somme = Somme +1
	Produit = Produit * Somme

print(Produit)
