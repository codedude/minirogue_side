#!/usr/bin/env/ python3.5
#-*- coding: utf-8 -*-
#

try:
    import sys
    from tkinter import *
    from PIL import Image, ImageTk
    import GuiChar as gui

except ImportError as e:
    print("Failed to load modules : {0}".format(e))
    sys.exit(2)




if __name__ == '__main__':
    print("App is launching...\n")

    #Create and Init main screen
    screen = gui.App("Character creator")

#Infinite loop -> event handling
    screen.loop()


#Window is closed, end app
    screen.close()

    print("\nApp is now closing...")
    sys.exit(0)