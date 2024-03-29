#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.8') as file:
    Data = file.read().strip()

Trajet,Base = Data.split("\n\n")
BaseT = Base.split("\n")
Grille = {}

for Ligne in BaseT :
	Indice,Duo = Ligne.split("=")
	Droite,Gauche = Duo.replace("(","").replace(")","").split(",")
	Indice = Indice.strip()
	Droite = Droite.strip()
	Gauche = Gauche.strip()	
	Grille[Indice] = (Droite,Gauche)

Position = "AAA"
Fin = False
Saut = 1
while Fin == False :
	for Direction in Trajet :
		if Direction == "L" :
			NextIndice = Grille[Position][0]
		else :
			NextIndice = Grille[Position][1]
		if NextIndice == "ZZZ" :
			Somme = Saut
			Fin = True
		elif Fin == False :
			Saut = Saut + 1
			Position = NextIndice

print(Somme)




