#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.4') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0

for L in Data:
	Solutions = 0
	Result = 0
	Texte,Cartes = L.split(":")
	Win,Mine = Cartes.split("|")
	Win = Win.strip().split(" ")
	Mine = Mine.strip().split(" ")

	for Carte in Mine:
		if Carte.isdigit() and Win.count(Carte) > 0:
			Solutions = Solutions + 1
			Result = 1
	for i in range(Solutions -1) :
		Result = Result * 2
	Somme = Somme + Result

print(Somme)
