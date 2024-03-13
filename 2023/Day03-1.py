#!/usr/bin/env python3

#On recupere les donnees initiales
with open('Input.3') as file:
    Data = [i for i in file.read().strip().split("\n")]


Somme = 0
for i in range(len(Data)):
    Lignes = Data[i]
    Capture = False
    Nb = ""
    for j in range(len(Data[i])):
        #On test si c est un nombre et on le recupere
        if Capture == False :
            if Data[i][j].isdigit() : 
                Capture = True
                AGarder = False
                Nb = Data[i][j]
        else :
            if Data[i][j].isdigit() :
                Nb = Nb + Data[i][j]
            else : 
                Capture = False
                if AGarder == True :
                    Somme = Somme + int(Nb)
        if Capture :
            #On test si il y a un caractere autour 
            if i > 0 :
                if Data[i-1][j] != "." and not Data[i-1][j].isdigit():
                    AGarder = True
            if i < (len(Data) -1) :
                if Data[i+1][j] != "." and not Data[i+1][j].isdigit():
                    AGarder = True
            if j > 0 :
                if Data[i][j-1] != "." and not Data[i][j-1].isdigit():
                    AGarder = True
            if j < (len(Data[i]) -1) :
                if Data[i][j+1] != "." and not Data[i][j+1].isdigit():
                    AGarder = True
            if i > 0 and  j > 0 :
                if Data[i-1][j-1] != "." and not Data[i-1][j-1].isdigit():
                    AGarder = True
            if i > 0 and j < (len(Data[i]) -1) :
                if Data[i-1][j+1] != "." and not Data[i-1][j+1].isdigit():
                    AGarder = True
            if i < (len(Data) -1) and j > 0 :
                if Data[i+1][j-1] != "." and not Data[i+1][j-1].isdigit():
                    AGarder = True
            if i < (len(Data) -1) and j < (len(Data[i]) -1) :
                if Data[i+1][j+1] != "." and not Data[i+1][j+1].isdigit():
                    AGarder = True
            if j == (len(Data[i]) -1) and AGarder == True :
                Somme = Somme + int(Nb)    
#        print(f"{i} / {j} - {Data[i][j]} - Capture : {Capture} - AGarder : {AGarder}")

            
print(Somme)







