#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.5') as file:
    Data = file.read().strip()


Seed, *Regles = Data.split("\n\n")

def Transformation(S,Dest,Deb,Scope):
	if int(S) >= int(Deb) and int(S) < (int(Deb) + int(Scope)):
		S = int(Dest) - int(Deb) + int(S)
	return(S)

#On construit la liste des graines
Seed = Seed.split(":")[1].strip().split(" ")

#On construit ensuite la liste des regles
ListeR = []
for Regle in Regles :
	ListeR.append(Regle.split(":")[1].split("\n")[1:])

#Et on fait passer chaque 
for i in range(len(Seed)) :
	print(f"Graine {Seed[i]}")
	for Regle in ListeR : 
		Change = False
		S = Seed[i]
		for LigneR in Regle:
			Dest,Deb,Scope = LigneR.split(" ")
			T = Transformation(S,Dest,Deb,Scope)	
			if T != S: 
				Seed[i] = int(T)
				Change = True
				
Min = int(Seed[0])
for S in Seed :
	if int(S) < Min:
		Min = int(S)
		
print(Min)


