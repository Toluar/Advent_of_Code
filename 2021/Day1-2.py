#!/usr/bin/env python3

filin = open("Input.1", "r")

Result = 0

#Valeur = [int(l) for l in filin]
#print(Valeur)

for i,Ligne in enumerate(filin):
  #print(Ligne.strip())
  if i == 0 :
    Val1 = int(Ligne)
  if i == 1 :
    Val2 = int(Ligne)
  if i == 2 :
    Val3 = int(Ligne)
    Somme1 = Val1 + Val2 + Val3 
  if i > 2 :
    #print("Val1 : %s,Val2 : %s,Val3 : %s,Somme1 : %s"%(Val1,Val2,Val3,Somme1))
    Val1 = Val2
    Val2 = Val3
    Val3 = int(Ligne)
    Somme2 = Val1 + Val2 + Val3
    if Somme2 > Somme1 :
      Result +=1
    Somme1 = Somme2
filin.close()

print(f" Le resultat : {Result}")
