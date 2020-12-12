# -*- coding : utf-8 -*-

# Header
"""
Porgramme principal du jeu de la vie graphique
Fait par Delaplaine Romain
27/11/2020
To do : tout
"""

#mes imports

import tkinter as tkinter
import librairie as lib

#mes fonctions propres a la version graphique

def fValidite_dim(pSaisie1 , pSaisie2 , pSaisie3):
    dim1 = lib.fValidite_saisie(pSaisie1)
    dim2 = lib.fValidite_saisie(pSaisie2)
    speed = lib.fValidite_saisie(pSaisie3)
    if dim1 and dim2 and speed:
        return True    #la saisie est correct
    else :
        return False     #la saisie est incorrect

def fCreate_cell (pX,pY,pNum):
    canevas.create_rectangle(pX[0] , pX[1] , pY[0] , pY[1] , tags = "cell_"+str(pNum) , outline = '#4b3819' , fill = "black")
    tag = "cell_"+str(pNum)
    callback = lambda event, tag=tag: fGenerate_by_user(event, tag)
    canevas.tag_bind(tag, '<Button-1>', callback)

def fCreate_grid ():
    global grid
    canevas.delete("all")
    test = fValidite_dim (dimension_x.get(),dimension_y.get(),vitesse.get())
    if test :
        liste_coord = []
        for j in range(0,int(dimension_y.get())):
            for i in range(0,int(dimension_x.get())):
                X = [0+i*(900/int(dimension_x.get())),0+j*(900/int(dimension_y.get()))]
                Y = [0+(i+1)*(900/int(dimension_x.get())),0+(j+1)*(900/int(dimension_y.get()))]
                liste_coord.append([X,Y])
        for i,val in enumerate (liste_coord) :
            fCreate_cell (val[0],val[1],i+1)
        grid = lib.fSet_grid(int(dimension_y.get()),int(dimension_x.get()))
    else :
        info.set("Saisie incorrect")

def fChange_color_cell_alive (pCell_tag):
    canevas.itemconfig (pCell_tag , fill = "white")

def fChange_color_cell_death (pCell_tag):
    canevas.itemconfig (pCell_tag , fill = "black")

def fModif_couleur ():   
    global grid
    for val in grid :         
        state = val.get_state()
        if state == 0 :
            fChange_color_cell_death("cell_"+str(val.get_num()))
        else :
            fChange_color_cell_alive("cell_"+str(val.get_num()))

def fGenerate ():
    global grid     
    grid = lib.fRandom_grid(grid)           #grid est une liste de cellule d'etat 1 ou 0
    for val in grid :
        state = val.get_state()
        if state == 0 :
            fChange_color_cell_death("cell_"+str(val.get_num()))
        else :
            fChange_color_cell_alive("cell_"+str(val.get_num()))

def fGenerate_by_user (event, pTag):
    global grid
    state = canevas.itemcget(pTag,'fill')
    indice = int(pTag.split("_")[1])-1
    if state == 'black' :
        fChange_color_cell_alive(pTag)
        grid[indice].change_state()
    elif state == 'white':
        fChange_color_cell_death(pTag)
        grid[indice].change_state()

def fAnnimation ():
    global grid
    global run
    grid_0 = grid
    liste = []      # liste de true ou false pr les modif sur la generation suivante
    for val in grid_0 :
        rep = lib.fSurvive(grid_0,val,int(dimension_y.get()),int(dimension_x.get()))
        liste.append(rep)
    for i,val in enumerate(liste):
        if val :
            grid[i].change_state()
    fModif_couleur()                        
    if not run :
        mywindow.after(int(vitesse.get()),fAnnimation)

def fStart ():
    global run
    if run == True:
        run = False
        fAnnimation()

def fStop ():
    global run
    run = True


#mes widgets tkinter

"""creation de ma fenetre"""
mywindow = tkinter.Tk()
mywindow.title('Jeu de la vie')
mywindow['bg'] = 'grey'

"""creation du widget pr la grille"""
Largeur = 900
Hauteur = 900
canevas = tkinter.Canvas(mywindow,width = Largeur , height = Hauteur, bg = 'black' )
canevas.grid(row = 1 , column = 1 , rowspan = 2 , columnspan = 2 , padx = 10 , pady = 10)

"""creation d'une frame pour les deux boutons"""
frame1 = tkinter.Frame(mywindow , padx = 10, pady = 10 , bg = 'grey')
frame1.grid(row = 2 , column = 3  , columnspan = 2 , padx = 10 , pady = 10)

"""creation d'un bouton pr lancer et arreter la simulation"""
Bouton = tkinter.Button(frame1, text = 'lancer' , font = ('Times' , '25') , command = fStart)
Bouton.grid(row = 2 , column = 2 , padx = 10 , pady = 10)
Bouton = tkinter.Button(frame1, text = 'arreter' , font = ('Times' , '25') , command = fStop)
Bouton.grid(row = 2 , column = 5 , padx = 10 , pady = 10)

"""creation d'un bouton pour generer une grille random"""
Bouton = tkinter.Button(frame1, text = 'generer' , font = ('Times' , '25') , command = fGenerate )
Bouton.grid(row = 1 , column = 3 , columnspan = 2 , padx = 10 , pady = 10)

"""creation d'une frame info"""
frame3 = tkinter.Frame(frame1 , bg = "grey" , relief = 'groove' )
frame3.grid(row = 3 , column = 2 , columnspan = 4 , padx = 10 ,pady = 10)

info = tkinter.StringVar()
tkinter.Label(frame3, textvariable = info , bg = "grey").grid(row = 1 , columnspan = 2 , padx = 10 ,pady = 10)

"""creation d'une frame pour les saisies"""
frame2 = tkinter.Frame(mywindow , padx = 10, pady = 10 , bg = 'grey')
frame2.grid(row = 1 , column = 3  , columnspan = 2 , padx = 10 , pady = 10)

"""creation des champs de saisie"""
frame2_x = tkinter.Frame(frame2 , padx = 10, pady = 10 , bg = 'grey')
frame2_x.grid(row = 1 , column = 2 , padx = 10 , pady = 10)

frame2_y = tkinter.Frame(frame2 , padx = 10, pady = 10 , bg = 'grey')
frame2_y.grid(row = 1 , column = 3 , padx = 10 , pady = 10)

tkinter.Label(frame2, text = 'Dimension :' , bg = 'grey' , font = ('Times' , '25')).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

tkinter.Label(frame2_x, text = 'x :' , bg = 'grey' , font = ('Times' , '25')).grid(row = 1 , padx = 10 , pady = 10)
dimension_x = tkinter.StringVar()
champ1 = tkinter.Entry(frame2_x,textvariable = dimension_x , font = ('Times' , '15') )
champ1.grid(row = 1 , column = 2 , rowspan = 2 , columnspan = 2 , padx = 10 , pady = 10)

tkinter.Label(frame2_y, text = 'y :' , bg = 'grey' , font = ('Times' , '25')).grid(row = 1 , padx = 10 , pady = 10)
dimension_y = tkinter.StringVar()
champ2 = tkinter.Entry(frame2_y,textvariable = dimension_y , font = ('Times' , '15') )
champ2.grid(row = 1 , column = 2 , padx = 10 , pady = 10)

tkinter.Label(frame2, text = 'Vitesse (en ms):' , bg = 'grey' , font = ('Times' , '25')).grid(row = 2 , column = 1 , padx = 10 , pady = 10)
vitesse = tkinter.StringVar()
champ3 = tkinter.Entry(frame2,textvariable = vitesse ,  font = ('Times' , '15') )
champ3.grid(row = 2 , column = 2 , padx = 10 , pady = 10)

""""creation d'un bouton pour valider la saisie"""
Bouton = tkinter.Button(frame2, text = 'valider' , font = ('Times' , '25') , command = fCreate_grid )
Bouton.grid(row = 3 , column = 2 , padx = 10 , pady = 10)

#mon code principal

run = True

#je lance ma fenetre

mywindow.mainloop()