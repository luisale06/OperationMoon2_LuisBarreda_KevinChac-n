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

"""Instruction Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""

def openinst():
    info = Toplevel() #Creates the about window
    info.title("Instructions") #Gives the window a name
    info.geometry("675x450") #Dimensions of the window

    """Images___________________________________________________________________________________________________________________________"""
    bg_label= tk.Label(info, image= bg_instructions)#background image
    bg_label.place(x=0,y=0)
    
    userimage= tk.Label(info, image= userimg, bg = "black")#ship image
    userimage.place(x=60,y=105)
    arrowsimage= tk.Label(info, image= arrows, bg = "black")#ship image
    arrowsimage.place(x=60,y=195)
    enemyimage= tk.Label(info, image= ufoimg1, bg = "black")#ship image
    enemyimage.place(x=60,y=305)

    
    """Basic instructions information Labels"""
    user_inf = tk.Label(info, font = ("Comic Sans MS", 13), text = "User image, you have 3 lives \n There are 3 levels \n  Each level lasts 60 seconds ", fg = "white", bg = "black"). place(x = 150, y = 85) #User instructions Label
    move_inf = tk.Label(info, font = ("Comic Sans MS", 13), text = "You move with the arrow keys \n ", fg = "white", bg = "black"). place(x = 200, y = 195) #Move instructions Label
    enemy_inf = tk.Label(info, font = ("Comic Sans MS", 13), text = "This is the enemy you have to avoid \n Each level has 2 more enemies than the other.", fg = "white", bg = "black"). place(x = 150, y = 335) #Enemy instructions Label
    

    """Buttons______________________________________________________________________________________________________________________________"""
    def destroyabout():
        info.destroy() #finally destroys the window
        
    
    destruir = tk.Button(info, image= back, command = destroyabout, bg= "black"). place(x = 3, y = 5) #button with the "about" window destruction command
    
    
    info.mainloop()

"""Top Players Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
