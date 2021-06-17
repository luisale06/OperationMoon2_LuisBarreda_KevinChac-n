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

"""Main Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
mw = tk.Tk() #Creates the main window
name = StringVar() #Takes the name of the user for the top 7 list

mw.title("Operation Moon Light 2") #Title of the principal window
mw.geometry("500x300") #Size of the principal window
mw.resizable(False, False)

"""Images___________________________________________________________________________________________________________"""

bg = PhotoImage(file = 'img/background1.gif')#create a image background 
bg_label= tk.Label(mw, image= bg)
bg_label.place(x=0,y=0)

bg_about = PhotoImage(file = 'img/bg_about.gif')#create a image background
bg_instructions = PhotoImage(file = 'img/bg_inst.gif')#create a image background

space = PhotoImage(file = 'img/background.gif')#create a image background
space = space.subsample(1)
space = space.zoom(2)

easy = PhotoImage(file = 'img/easy.png')#create a easy image 
medium = PhotoImage(file = 'img/medium.png')#create a medium image  
hard = PhotoImage(file = 'img/hard.png')#create a hard image

about = PhotoImage(file = 'img/about.png')#create a about image 
top = PhotoImage(file = 'img/top.png')#create a top image  
instructions = PhotoImage(file = 'img/instructions.png')#create a isntructions image
back = PhotoImage(file = 'img/back.png')#create a back image
arrows = PhotoImage(file = 'img/arrows.png')#create a arrows image 

ufoimg = PhotoImage(file = 'img/ufo.png')
ufoimg1 = PhotoImage(file = 'img/ufo1.png')
userimg = PhotoImage(file = 'img/player.png')

"""Entries___________________________________________________________________________________________________________"""

user_name = tk.Entry(mw, textvariable = name, font = ("Comic Sans MS", 14), width = 10) #Entry widget for the user to write his/her name
user_name.place(x=185, y=65)

"""Labels___________________________________________________________________________________________________________"""
usernameinstruction = tk.Label(mw, font = ("Comic Sans MS", 12), text = "Enter your name to save your results", fg = "ghostwhite", bg = "#07070a"). place(x = 115, y = 95) #Label with the title of the game

"""Buttons___________________________________________________________________________________________________________"""
level1 = tk.Button(mw, image= easy, bg = "black", command = game1) .place(x=135, y=130) #Opens the level 1 window
level2 = tk.Button(mw, image= medium, bg = "black", command = game2) .place(x=215, y=130) #Opens the level 2 window
level3 = tk.Button(mw, image= hard, bg = "black", command = game3) .place(x=295, y=130) #Opens the level 3 window

btn_about = tk.Button(mw, image= about, command = openaboutw,  bg = "black") .place(x=135, y=190) #Opens the about window
btn_top = tk.Button(mw, image= top, bg = "black", command = game2) .place(x=215, y=190) #Opens the top window
btn_instructions = tk.Button(mw, image= instructions, bg = "black",command = openinst) .place(x=295, y=190) #Opens the instructions window

second = 0
userlife = 3
score = 0
score2 = 0
score3 = 0
score4 = 0

mw.mainloop()
