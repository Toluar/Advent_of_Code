#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.9.t') as file:
    Data = [i for i in file.read().strip().split("\n")]

Somme = 0


for Lines in Data:
#On rempli le tableau
    Tableau = []
    Chiffres = Lines.split(" ")
    Ligne = []
    for chiffre in Chiffres :
        Ligne.append(int(chiffre))
    Tableau.append(Ligne)


#On vient faire la difference et on stocke tout dans le tableau
    LigneNulle = False
    Ind = 0
    while LigneNulle == False:
        LigneNulle = True
        LigneTmp = []
        for i in range(len(Tableau[Ind])-1):
            LigneTmp.append(int(Tableau[Ind][i+1])-int(Tableau[Ind][i]))
            if ( int(Tableau[Ind][i+1]) -int(Tableau[Ind][i]) ) != 0:
                LigneNulle = False
        Tableau.append(LigneTmp)
        Ind = Ind + 1
    
#La dernière ligne du tableau est vide. Du coup, on remonte pour trouver le dernier element
    LastElemnt = 0
    for i in range(len(Tableau),0,-1):
        LastElemnt = Tableau[i-1][len(Tableau[i-1]) -1] + LastElemnt
#        print(f"{i} : {Tableau[i-1]} => {LastElemnt} ")
#    print(f"{LastElemnt} ")
    Somme = Somme + LastElemnt

print(Somme)


