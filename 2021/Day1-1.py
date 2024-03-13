#!/usr/bin/env python3

filin = open("Input.1", "r")

Result = 0

#Valeur = [int(l) for l in filin]
#print(Valeur)

for i,Ligne in enumerate(filin):
  #print(Ligne.strip())
  if i == 0 :
    Val2 = int(Ligne)
  if i > 0 :
    #print("Val1 : %s,Val2 : %s,Val3 : %s,Somme1 : %s"%(Val1,Val2,Val3,Somme1))
    Val1 = Val2
    Val2 = int(Ligne)
    if Val2 > Val1 :
      Result +=1
filin.close()

print(f" Le resultat : {Result}")
