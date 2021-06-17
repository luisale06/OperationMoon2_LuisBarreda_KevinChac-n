import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from threading import Thread
import threading
import random
import sys
import pygame
from pygame import mixer
sys.setrecursionlimit(3000)

"""About Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def openaboutw():
    info = Toplevel() #Creates the about window
    info.title("Programmer information") #Gives the window a name
    info.geometry("675x450") #Dimensions of the window

    bg_label= tk.Label(info, image= bg_about)
    bg_label.place(x=0,y=0)
    
    
    """Basic programmer information Labels"""
    country_of_prod = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Country of Production  -->  Costa Rica", fg = "white", bg = "black"). place(x = 60, y = 95) #Country Label
    university_career = tk.Label(info, font = ("Comic Sans MS", 13), text = "- University --> Tecnológico de Costa Rica \n Career --> Computer Engineering", fg = "white", bg = "black"). place(x = 60, y = 135) #College and career label
    subject_year_group = tk.Label(info, font = ("Comic Sans MS", 12), text = "- Subject/Year/Group  -->  Taller de Programación, 2nd Year, Group 3", fg = "white", bg = "black"). place(x = 60, y = 195) #Subject label
    professor = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Professor  -->  Leonardo Araya Martinez", fg = "white", bg = "black"). place(x = 60, y = 235) #Professor label
    version = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Version  -->  1.0", fg = "white", bg = "black"). place(x = 60, y = 265) #Version label
    author_name = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Author's name's  -->  Luis Alejandro Barreda Acevedo \n Kevin Andrés Chacón Chaves", fg = "white", bg = "black"). place(x = 60, y = 295) #Author label
    module_authors = tk.Label(info, font = ("Comic Sans MS", 13), text = "- Modules' authors  -->  ______", fg = "white", bg = "black"). place(x = 60, y = 365) #Modules' authors label

    """Buttons______________________________________________________________________________________________________________________________"""
    def destroyabout():
        info.destroy() #finally destroys the window
        
    
    destruir = tk.Button(info, image= back, command = destroyabout, bg= "black"). place(x = 3, y = 5) #button with the "about" window destruction command
    
    
    info.mainloop()

