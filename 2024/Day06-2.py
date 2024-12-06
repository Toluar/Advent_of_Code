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
#On parcours la grille tant que l on est dans la grille
while Position in Grille:
    Parcours.add(Position)
    if Position + Direction in Stop:
        Direction *= -1j
        continue
    Position += Direction

#On a rempli le parcours initial
#On va regarder pour chaque point du parcours si on peut placer un nouvel obstacle
#Et si en placant ce point on repasse par notre chemin en empruntant la meme direction
#Si on sort de la grille, le point n est pas bon.
#Il suffira de compter le nombre de points qui sont ok
#On va passer par une fonction test et utiliser map pour appeler chaque point du parcours
def Test_P(Point):
    Obstruction = Stop | {Point}
    Position = Debut
    Direction = -1
    P = set() #Je change juste le nom de la variable contenant le parcours pour etre plus clean
    while Position in Grille:
        if (Position, Direction) in P:
            return True
        P.add((Position, Direction))
        if Position + Direction in Obstruction:
            Direction *= -1j
            continue
        Position += Direction
    return False


print(sum(map(Test_P, Parcours)))
