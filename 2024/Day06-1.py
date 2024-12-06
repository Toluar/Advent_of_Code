#!/usr/bin/env python3

with open("Input.06") as f:
    Data = f.read().strip().split("\n")

#Creation d'une grille au format dictionnaire avec les coordonnées en tuples
Grille = {i + 1j * j: x for i, D in enumerate(Data) for j, x in enumerate(D)}

#On recupere la position de depart
Debut = next( Item for Item, Value in Grille.items() if Value == "^")

#On créé pareil un dico de tuples contenant la liste des "murs"
Stop = { Item for Item , Value in Grille.items() if Value == "#"}

Parcours = set()
Position = Debut
Direction = -1

while Position in Grille:
    Parcours.add(Position)
    if Position + Direction in Stop:
        Direction *= -1j
        continue
    Position += Direction

print(len(Parcours))

