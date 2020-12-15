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
matrix_grid = lib.fMatrix_grid(grid,grid_width,grid_height)
generation = 0
while generation < generation_max :
    grid_0 = grid
    liste = []
    print("generation "+str(generation))
    lib.fAffichage_console(grid,grid_width,grid_height)
    # lib.fAffichage_console_V2(matrix_grid)
    for i,cell in enumerate(grid_0):
        rep = lib.fSurvive(grid_0,cell,grid_width,grid_height)
        liste.append(rep)
    for i,val in enumerate(liste):
        if rep :
            grid[i].change_state()
    generation += 1
