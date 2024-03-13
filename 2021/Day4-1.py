#!/usr/bin/env python3


Filin1 = open("Input.4.2","r")
tirages = Filin1.readlines()
Filin1.close()
#On cree un tableau avec la liste des chiffres composant le tirage
tirage = tirages[0].replace("\n","").split(",")

#On recupere ensuite l ensemble des grilles
TailleGrille = 5
Nb_Grilles = 0
Liste_Grille = {} #Dictionnaire contenant l ensemble des grilles
Grille = [[0] * TailleGrille for i in range(TailleGrille)]  #Grille de base
IndLigne = 0 #Va contenir l indice de la ligne que l on va ajouter


filin = open("Input.4.1","r")
for i,ligneG in enumerate(filin):
    if len(ligneG) > 1:
        #C est une ligne qui doit etre ajouter a la grille
        TableTMP = ligneG.replace("  "," ").split()
        for x in range(len(TableTMP)):
            Val = int(TableTMP[x])
            Grille[IndLigne][x]=Val
        IndLigne += 1
    else:
        #Grille terminee. On passe a une autre grille
        IndLigne = 0
        Liste_Grille[Nb_Grilles]=Grille
        Nb_Grilles +=1
        Grille = [[0] * TailleGrille for i in range(TailleGrille)]
filin.close
Liste_Grille[Nb_Grilles]=Grille
Nb_Grilles +=1

def Number_in_grille(Grille,Nbr):
    for x in range(0,int(TailleGrille)):
        for y in range(0,TailleGrille):
            if Grille[x][y] == Nbr:
                Grille[x][y] = "X"
                i = 0
                crX = True
                crY = True
                while i < TailleGrille :
                    if (Grille[i][y] != "X"):
                        crX = False
                    if (Grille[x][i] != "X"):
                        crY = False
                    i += 1
                if ((crX == True) or (crY == True)):
                    return True
                    
    return False

BINGO = False
for t in range(len(tirage)):
    for i in range(Nb_Grilles):
        if Number_in_grille(Liste_Grille[i],int(tirage[t])):
            BINGO = True
            ind = i
            NbT = int(tirage[t])
            break
    if BINGO == True:
        break
        
Somme = 0
for x in range(0,TailleGrille):
    for y in range(0,TailleGrille):
        if Liste_Grille[ind][x][y] != "X":
            Somme = Somme + Liste_Grille[ind][x][y]

Resultat = Somme * NbT
print(f"Resultat : {Somme} * {NbT} : {Resultat} ")

# Connaitre le type d une variable : print(type(tirages))


