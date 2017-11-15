#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys
    from tkinter import *

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)


Canevas = None
posClic = {'x':0, 'y':0}
def BMotion(event):
    """ Gestion de l'événement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    rect = canvas.find_closest(x, y)[0]
    Canevas.coords(rect, x-posClic['x'], y-posClic['y'], x+30-posClic['x'], y+30-posClic['y'])

def BClic(event, arg):
    print(arg)
    canvas = event.widget
    _x = canvas.canvasx(event.x)
    _y = canvas.canvasy(event.y)
    rect = canvas.find_closest(_x, _y)[0]
    [xmin,ymin,xmax,ymax] = Canevas.coords(rect)
    posClic['x'] = event.x-xmin
    posClic['y'] = event.y-ymin

def Effacer():
    """ Efface la zone graphique """
    Canevas.delete(ALL)

if __name__ == '__main__':

    # Création de la fenêtre principale
    Mafenetre = Tk()
    Mafenetre.title('Carre')

    # Création d'un widget Canvas
    Largeur = 480
    Hauteur = 320
    Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
    img = Canevas.create_rectangle(20, 20, 50, 50, outline='black',fill='green')
    # La méthode bind() permet de lier un événement avec une fonction :
    # un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
    Canevas.tag_bind(img, '<B1-Motion>', BMotion)
    Canevas.tag_bind(img, '<Button-1>', lambda e:BClic(e,'ok'))
    Canevas.pack(padx =5, pady =5)

    # Création d'un widget Button (bouton Effacer)
    Button(Mafenetre, text ='Effacer', command = Effacer).pack(side=LEFT,padx = 5,pady = 5)

    # Création d'un widget Button (bouton Quitter)
    Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

    Mafenetre.mainloop()


    sys.exit(0)