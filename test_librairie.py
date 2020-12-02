# -*- coding : utf-8 -*-

# Header
"""
test de la librairie pour le jeu de la vie
Fait par Delaplaine Romain
27/11/2020
To do : faire des tests plus particuliers pr voir si tt les cas fonctionnent 
"""

import librairie as lib

test1 = lib.fSet_grid(2,2)
# print ("Resultat attendu:[cellule1, cellule1, cellule1, cellule1], Resulat:",test1)

# print ("Resultat attendu:[0, 0, 0, 0], Resulat:")
# test2 = lib.fAffichage_console(test1,2,2)

grille = lib.fSet_grid(6,5)
grille[3].state = 1
grille[9].state = 1
grille[11].state = 1
grille[18].state = 1
grille[19].state = 1
grille[24].state = 1
grille[25].state = 1
grille[26].state = 1
lib.fAffichage_console(grille,6,5)
# test3 = lib.fSurvive(grille,grille[10],6,5)
# print("Resultat attendu:True, Resulat:",test3)
# test3 = lib.fSurvive(grille,grille[19],6,5)
# print("Resultat attendu:True, Resulat:",test3)
# test3 = lib.fSurvive(grille,grille[0],6,5)
# print("Resultat attendu:False, Resulat:",test3)
# test3 = lib.fSurvive(grille,grille[24],6,5)
# print("Resultat attendu:False, Resulat:",test3)

grille2 = lib.fSet_grid(4,4)
grille2 = lib.fRandom_grid(grille2)
lib.fAffichage_console(grille2,4,4)