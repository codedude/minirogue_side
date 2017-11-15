#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import font
    from abc import ABCMeta, abstractmethod
    from PIL import Image, ImageTk

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)

"""
    Init main window (title + grid mode)
    Init all font (type + size in a dict)
    Init default self strategy
"""
class App(tk.Tk):
    fonts = dict()

    def __init__(self, name="Main window"):
        #Init window
        super().__init__()
        self.title(name)

        #Init fonts -> put in singleton
        self.fonts["default"] = dict()
        self.fonts["default"]["18"] = font.Font(size=18)
        self.fonts["default"]["12"] = font.Font(size=12)

        #Init main frame
        self.__screen = tk.Frame(self)
        self.__screen.pack(side="top", fill="both", expand=True)
        self.__screen.grid_rowconfigure(0, weight=1)
        self.__screen.grid_columnconfigure(0, weight=1)

        #Init sub frames (pages)
        self.frames = {}
        pages = {Splash, Char, Game}
        for K in pages:
            frame = K(parent=self.__screen, ctrl=self)
            self.frames[K.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Default frame
        self.showFrame("Char")

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def loop(self):
        self.mainloop()
    def close(self):
        self.quit()


class Splash(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl

    def draw(self):
        label = tk.Label(self, text = 'Splash !')
        label.grid(row=0, column=0)

class Game(tk.Frame):
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl
        self.draw()

    def draw(self):
        label = tk.Label(self, text = 'Game !')
        label.grid(row=0, column=0)

class Char(tk.Frame):
    imgPath = "poo/chars/"
    chars = ["char1.png", "char2.png", "char3.png"]
    img_s = {}
    def __init__(self, parent, ctrl):
        tk.Frame.__init__(self, parent)
        self.ctrl = ctrl
        self.draw()

    def draw(self):
        #Choix du pseudo
        label = tk.Label(self, text = 'Nickname :')
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 20),
            sticky=tk.E)
        input_nick = tk.Entry(self, bg="white", fg="black", justify=tk.CENTER,
            relief="flat")
        input_nick.focus_set()
        input_nick.grid(row=0, column=2, columnspan=2, padx=5, pady=(15, 20),
         sticky=tk.W, ipadx=3, ipady=3)

    #Choix du personnage
        size = 200, 250
        image = Image.open(self.imgPath + self.chars[0])
        image.thumbnail(size, Image.ANTIALIAS)
        size = image.size
        image = ImageTk.PhotoImage(image)
        self.img_s[self.chars[0]] = image
        img = tk.Canvas(self, width=size[0], height=size[1])
        img.create_image(0, 0, anchor=tk.NW, image=image)
        img.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, pady=5)
        tk.Button(self, text='Previous', command=self.previousImg) \
        .grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self, text='Next', command=self.nextImg) \
        .grid(row=5, column=1, padx=5, pady=5)


    #Choix des caracs
        self.frame = tk.LabelFrame(self, borderwidth=1, relief=tk.SUNKEN,
            text="Caracteristics")
        self.frame.grid(row=1, column=2, columnspan=2, rowspan=4, sticky=tk.N,
            pady=0)
        label = tk.Label(self.frame, text = 'Age :')
        label.grid(row=0, column=0, padx=5, pady=5)
        input_age = tk.Entry(self.frame, bg="white", fg="black", justify=tk.CENTER,
            relief="flat")
        input_age.grid(row=0, column=1, padx=5, pady=5)

        label = tk.Label(self.frame, text = 'Class :')
        label.grid(row=1, column=0, padx=5, pady=5)

        opt_list = ["Mage", "Warrior", "Rogue"]
        self.class_var = tk.StringVar(self.frame)
        self.class_var.set(opt_list[0]) # default value

        w = tk.OptionMenu(self.frame, self.class_var, *opt_list)
        w["menu"].config(borderwidth=1)
        w.config(borderwidth=1)
        w.config(highlightthickness=0)
        w.grid(row=1, column=1, padx=5, pady=5)

    #Boutons du bas
        tk.Button(self, text='Clear', command=self.clearData)\
        .grid(row=6, column=0, columnspan=2, padx=5, pady=(25, 10))
        tk.Button(self, text ='Play', font=self.ctrl.fonts["default"]["18"],
            command=lambda:self.ctrl.showFrame("Game"), width=5, height=2)\
        .grid(row=6, column=2, columnspan=2, padx=5, pady=(15, 5))

    def clearData(self):
        pass
    def nextImg(self):
        pass
    def previousImg(self):
        pass

if __name__ == '__main__':
    sys.exit(0)