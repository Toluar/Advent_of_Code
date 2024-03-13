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
Seeds = []
Seed = Seed.split(":")[1].strip().split(" ")
for i in range(0,int(len(Seed)/2)+1,2):
	Seeds.append((int(Seed[i]),(int(Seed[i+1]) + int(Seed[i]) -1)))

#On construit ensuite la liste des regles
ListeR = []
for Regle in Regles :
	ListeR.append(Regle.split(":")[1].split("\n")[1:])

Min = max(Seed)

for Regle in ListeR :
	A = []
	while Seeds: 
		Min = int(Seeds[0][0])
		Max = int(Seeds[0][1])
		Change = False
		for LigneR in Regle:
			if Change == False:
				Dest,Deb,Scope = LigneR.split(" ")
				Dest = int(Dest)
				Deb = int(Deb)
				Scope = int(Scope)
				Fin = Deb + Scope - 1
				if Min >= Deb and Min <= Fin :
					TMin = Transformation(Min,Dest,Deb,Scope)
					if Max <= Fin :
						TMax = Transformation(Max,Dest,Deb,Scope)
						A.append((int(TMin),int(TMax)))
						Change = True
					else :
						TMax = Transformation(Fin,Dest,Deb,Scope)
						A.append((int(TMin),int(TMax)))
						Seeds.append((int(Fin + 1),int(Max)))
						Change = True
				elif Max >= Deb and Max <= Fin :
					TMax = Transformation(Max,Dest,Deb,Scope)
					TMin = Dest
					A.append((int(TMin),int(TMax)))
					Change = True
					Seeds.append((int(Min),int(Deb -1)))
				elif Max > Fin and Min < Deb :
					Tmin = Dest
					Tmax = Transformation(Fin,Dest,Deb,Scope)
					A.append((int(Tmin),int(Tmax)))
					Change = True
					Seeds.append((int(Min),int(Deb-1)))
					Seeds.append((int(Fin+1),int(Max)))
			
		if Change == False:
			A.append(Seeds[0])		
		Seeds.pop(0)
	Seeds = A
Min = int(Seeds[0][0])
for S in Seeds :
	if S[0] < Min :
		Min = S[0]
print(Min)


