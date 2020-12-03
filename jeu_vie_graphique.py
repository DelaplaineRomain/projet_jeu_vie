# -*- coding : utf-8 -*-

# Header
"""
Porgramme principal du jeu de la vie graphique
Fait par Delaplaine Romain
27/11/2020
To do : tout
"""

import tkinter as tkinter
import librairie as lib

def fLancement():
    for cell in grid:
        rep = lib.fSurvive(grid,cell,grid_width,grid_height)
        if rep == True :
            cell.change_state()
    generation += 1

def fArret():
    for cell in grid:
        rep = lib.fSurvive(grid,cell,grid_width,grid_height)
        if rep == True :
            cell.change_state()
    generation += 1

#creation de ma fenetre
mywindow = tkinter.Tk()
mywindow.title('Jeu de la vie')
mywindow['bg'] = 'black'

#creation du widget pr la grille
Largeur = 500
Hauteur = 500
canevas = tkinter.Canvas(mywindow,width = Largeur , height = Hauteur, bg = 'white')
canevas.pack(side = 'left',padx=10,pady=10)

#creation d'un bouton pr lancer et arreter la simulation
Bouton = tkinter.Button(mywindow, text = 'lancer' , command = fLancement)
Bouton.pack(side = 'left',padx=10,pady=10)
Bouton = tkinter.Button(mywindow, text = 'arreter' , command = fArret)
Bouton.pack(side = 'left',padx=10,pady=10)

#creation d'un champ d'entre pr redimansionner la grille
Label = tkinter.Label(mywindow, text = 'Dimension :').pack(side = 'left',padx=10,pady=10)
dimension = tkinter.StringVar()
champ = tkinter.Entry(mywindow,textvariable = dimension)
champ.focus_set()
champ.pack(side = 'left',padx=10,pady=10)

mywindow.mainloop()