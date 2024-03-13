#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.3') as file:
    Data = [i for i in file.read().strip().split("\n")]

def Recup_Nombre(l , c):
    Nombre = True
    R = ""
    while Nombre:
        if c == 0 :
            Nombre = False
        if c > 0 and Data[l][c-1].isdigit() == False:
            Nombre = False
        if c > 0 and Data[l][c-1].isdigit():
            c = c-1
    Nombre = True
    while Nombre :
        R = R + Data[l][c]
        CMax = len(Data[l]) -1
        if c == CMax:
            Nombre = False
        if c < CMax and Data[l][c+1].isdigit() == False:
            Nombre = False
        if c < CMax and Data[l][c+1].isdigit() :
            c = c + 1
    return int(R)
            


Somme = 0
for i in range(len(Data)):
    Lignes = Data[i]
    if Lignes.count("*") > 0 :
        for j in range(len(Lignes)) :
            Elmt = Lignes[j]
            if Elmt == "*" :
                Nb1 = 0
                Nb2 = 0
                #On regarde au dessus
                if i >0 :
                    if Data[i-1][j].isdigit() :
                        #Nombre au milieu
                        Nb1 = Recup_Nombre(i-1,j)
                    else :
                        if j > 0 :
                            if Data[i-1][j-1].isdigit() :
                                Nb2 = Recup_Nombre(i-1,j-1)
                                if Nb1 == 0 :
                                    Nb1 = Nb2
                                    Nb2 = 0
                        if j < (len(Data[i-1]) -1) :
                            if Data[i-1][j+1].isdigit() :
                                Nb2 = Recup_Nombre(i-1,j+1)
                                if Nb1 == 0:
                                    Nb1 = Nb2
                                    Nb2 = 0
                #On regarde au meme niveau
                if j > 0 : 
                    if Data[i][j-1].isdigit() :
                        Nb2 = Recup_Nombre(i,j-1)
                        if Nb1 == 0 :
                            Nb1 = Nb2
                            Nb2 = 0
                if j < (len(Data[i]) -1) :
                    if Data[i][j+1].isdigit() :
                        Nb2 = Recup_Nombre(i,j+1)
                        if Nb1 == 0:
                            Nb1 = Nb2
                            Nb2 = 0
                #On regarde au dessous
                if i < len(Data) :
                    if Data[i+1][j].isdigit() :
                        Nb2 = Recup_Nombre(i+1,j)
                        if Nb1 == 0:
                            Nb1 = Nb2
                            Nb2 = 0
                    else:
                        if j > 0 :
                            if Data[i+1][j-1].isdigit() :
                                Nb2 = Recup_Nombre(i+1,j-1)
                                if Nb1 == 0:
                                    Nb1 = Nb2 
                                    Nb2 = 0
                        if j < (len(Data[i+1]) -1) :
                            if Data[i+1][j+1].isdigit() :
                                Nb2 = Recup_Nombre(i+1,j+1)
                                if Nb1 == 0:
                                    Nb1 = Nb2
                                    Nb2 = 0
                Somme = Somme + ( int(Nb1) * int(Nb2) )

print(Somme)



