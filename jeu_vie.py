# -*- coding : utf-8 -*-

# Header
"""
Porgramme principal du jeu de la vie console
Fait par Delaplaine Romain
27/11/2020
To do : rien
"""

import librairie as lib

generation_max = int(input("veuillez entrer la generation max :"))
grid_width = int(input("veuillez entrer la largeur de la grille :"))
grid_height = int(input("veuillez entrer la hauteur de la grille :"))
grid = lib.fSet_grid(grid_width,grid_height)
grid = lib.fRandom_grid(grid)
generation = 0
while generation < generation_max :
    print("generation "+str(generation))
    lib.fAffichage_console(grid,grid_width,grid_height)
    for cell in grid:
        rep = lib.fSurvive(grid,cell,grid_width,grid_height)
        if rep == True :
            cell.change_state()
    generation += 1
