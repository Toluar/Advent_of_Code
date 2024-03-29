#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.8') as file:
    Data = file.read().strip()

Trajet,Base = Data.split("\n\n")
BaseT = Base.split("\n")

def Euclide(A,B):
	Fin = False
	while Fin == False :
		CT = B % A
		CU = B // A
		if CT == 0 :
			Fin = True
		else :
			B = A
			A = CT
			
	return(A)

def IndiceSuivant(Direction, Position, GrilleT):
	if Direction == "L" :
		Next = GrilleT[Position][0]
	else : 
		Next = GrilleT[Position][1]
	return(Next)

Grille = {}
Depart = []
for Ligne in BaseT :
	Indice,Duo = Ligne.split("=")
	Droite,Gauche = Duo.replace("(","").replace(")","").split(",")
	Indice = Indice.strip()
	if Indice.endswith("A"):
		Depart.append(Indice)
	Droite = Droite.strip()
	Gauche = Gauche.strip()	
	Grille[Indice] = (Droite,Gauche)

NbParcours = len(Depart)
Fin = False
Step = 0
R=[]
for i in Depart:
	R.append(0)
while Fin == False:
	for D in Trajet :
		Step = Step + 1
		Fin = True
		for i in range(NbParcours) :
			NextStep = IndiceSuivant(D,Depart[i],Grille)
			if NextStep.endswith("Z") == False:
				Fin = False
			if R[i-1] == 0 and NextStep.endswith("Z"):
				R[i-1] = Step
		Produit = 1	
		for i in range(len(Depart)) :
			Produit = Produit * R[i]
		if Produit != 0:
			Fin = True	
		if Fin ==False:
			for i in range(NbParcours) :
				Depart[i] = IndiceSuivant(D,Depart[i],Grille)
for j in range(1 ,len(R)):
	if R[0] > R[j] :
		E = Euclide(R[j],R[0])
	else :
		E = Euclide(R[0],R[j])
	Produit = int(Produit/E)	
print(Produit)			
		 





