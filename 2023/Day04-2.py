#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.4') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0
Tab = []
for i in range(0,len(Data)):
	Tab.append(0)	
for L in Data:
	Solutions = 0
	Texte,Cartes = L.split(":")
	Win,Mine = Cartes.split("|")
	Win = Win.strip().split(" ")
	Mine = Mine.strip().split(" ")
	Ind = int(Texte.replace("Card","").strip())
	for Carte in Mine:
		if Carte.isdigit() and Win.count(Carte) > 0:
			Solutions = Solutions + 1
	Tab[Ind -1] = Tab[Ind -1] + 1
	if Solutions > 0 :
		for j in range(Solutions):
			Tab[Ind + j] = Tab[Ind + j] + Tab[Ind -1]
Somme = sum(Tab)	
print(f"Solution : {Somme}")
