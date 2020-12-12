# -*- coding : utf-8 -*-

# Header
"""
Librairie pour le jeu de la vie version console
Fait par Delaplaine Romain
27/11/2020
To do : faire une fonction pr gerer la saisie de l'utilisateur 
"""

import random as ran

#creation de ma classe cellule
''' avec en attribut le numero de la cellule et son etat'''
class Cell:
    def __init__ (self,num,state = 0):
        self.num = num
        self.state = state

    def change_state(self) :
        if self.state == 0 :
            self.state = 1
        else :
            self.state = 0
    
    def get_state(self):
        return self.state

    def get_num(self):
        return self.num

    def __str__ (self):
        return str(self.state)

#fonction qui redimensionne une grille
''' en parametre les dimensions et en sortie la grille qui est une liste de cellule '''
def fSet_grid(pWidth,pHeight):
    grille = []
    for i in range(1,pWidth*pHeight+1):
        grille.append(Cell(i))
    return grille

def fMatrix_grid (pGrid,pWidth,pHeight):
    rep = pGrid        #rep est la liste contenant toute les cellules dans l'ordre
    grille = []     #grille est la liste de liste correspondant  notre grille
    for i in range(1,pHeight+1):
        grille.append(rep[:pWidth])
        rep = rep[pWidth:]
    return grille

#fonction qui nous dit si une cellule meurt ou vit au prochain tour
''' en parametre la grille, la cellule courante,la largeur/hauteur et en sortie True(changement d'etat)ou False(pas de cgt) '''
def fSurvive(pGrid,pCell,pWidth,pHeight):
    '''environment est la liste des numero de celulle autour de la cellule courante '''
    cell_num = pCell.get_num()
    cell_state = pCell.get_state()
    environment = []
    if cell_num % pWidth == 1 :
        if cell_num == 1:
            environment = [cell_num+1,cell_num+pWidth,cell_num+pWidth+1]
        elif cell_num == pWidth*pHeight-pWidth+1 :
            environment = [cell_num+1,cell_num-pWidth,cell_num-pWidth+1]
        else :
            environment = [cell_num+1,cell_num+pWidth+1,cell_num+pWidth,cell_num-pWidth+1,cell_num-pWidth]
    elif cell_num % pWidth == 0 :
        if cell_num == pWidth : 
            environment = [cell_num-1,cell_num+pWidth-1,cell_num+pWidth]
        elif cell_num == pWidth*pHeight :
            environment = [cell_num-1,cell_num-pWidth,cell_num-pWidth-1]
        else :
            environment = [cell_num-1,cell_num+pWidth-1,cell_num+pWidth,cell_num-pWidth-1,cell_num-pWidth]
    elif  1 < cell_num < pWidth :
        environment = [cell_num-1,cell_num+1,cell_num+pWidth-1,cell_num+pWidth,cell_num+pWidth+1]
    elif pWidth*pHeight-pWidth+1 < cell_num < pWidth*pHeight :
        environment = [cell_num-1,cell_num+1,cell_num-pWidth-1,cell_num-pWidth,cell_num-pWidth+1]
    else :
        environment = [cell_num-1,cell_num+1,cell_num-pWidth-1,cell_num-pWidth,cell_num-pWidth+1,cell_num+pWidth-1,cell_num+pWidth,cell_num+pWidth+1]
    """rep renvoie true si la cellule doit changer d'etat et false sinn"""
    rep = False
    ''' res est le nombre de cellule vivante autour de la cellule courante '''
    res = 0
    if cell_state == 0 :
        for i in environment:
            res += pGrid[i-1].get_state()
        # print("res =",res)
        if res == 3 :
            rep = True
    else :
        for i in environment:
            res += pGrid[i-1].get_state()
        # print("res =",res)
        if res != 2 and res != 3 :
            rep = True
    return rep

#fonction qui creer une grille aleatoire
''' en parametre la grille par defaut (tt les etats sont a 0) et en sortie la nouvelle grille'''
def fRandom_grid(pGrid):
    for val in pGrid :
        val.state = ran.randint(0,1)
    return pGrid

#fonction permetant un affichage comprehensible sur console
''' en parametre la grille et ses dimensions et en sortie rien juste l'affichage de la grille '''
def fAffichage_console(pListe,pWidth,pHeight):
    test = []
    for val in pListe :
        state = val.get_state()
        test.append(state)
    for i in range(1,pHeight+1):
        print(test[:pWidth])
        test = test[pWidth:]

#fonction permetant un affichage comprehensible sur console
''' en parametre la grille et ses dimensions et en sortie rien juste l'affichage de la grille '''
def fAffichage_console_V2(pListe):
    for val in pListe:
        print (val)

#fonction pour verifier la saisie
''' en parametre la saisie et en sortie true ou false '''
def fValidite_saisie (pEntre):
    rep = False
    if pEntre.isdigit() :
        rep =  True
    return rep