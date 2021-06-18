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
sys.setrecursionlimit(5000)

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

    
    """Basic programmer information Labels"""
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
def opentop():
    archive = open('Top7.txt', "r")
    data = [line.rstrip('\n').split(':') for line in archive]
    print(data)
    messagebox.showinfo(message = '1. ' + str((data[1][0], data[10][0])) + '\n' + '2. ' + str((data[2][0], data[11][0])) + '\n' + '3. ' + str((data[3][0], data[12][0])) + '\n' + '4. ' + str((data[4][0], data[13][0])) + '\n' + '5. ' + str((data[5][0], data[14][0])) + '\n' + '6. ' + str((data[6][0], data[15][0])) + '\n' + '7. ' + str((data[7][0], data[16][0])), title = 'Top 7 Players') #opens the message box with the top 7 players

"""Game1 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""

def game1():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light 2") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    game.resizable(False, False)
    
    """Canvas widget_______________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650) #create the canvas widget where the animation is going to occu
    spacebg = gamecanvas.create_image(230, 350, image = space)
    user = gamecanvas.create_image(240, 500, image = userimg) #user's spaceship

    """User's life functions____________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them

    """Top 7 Set_____________________________________________________________________________________________________________________"""
    def top7set():
        top7 = top7txt()
        with open('Top7.txt', 'w') as update:
            for i in top7: #cycle that writes down the information in the .txt
                update.write(str(i))
                update.write("\n")
    
    def top7txt():
        alltext = []
        with open('Top7.txt', 'r') as top7:
            for line in top7.readlines():
                alltext.append(line)

        allminusn = []
        for line in alltext:
            minusn = line.replace("\n", "")
            allminusn.append(minusn)

        scoreonly = allminusn
        n = 10
        while n != 0:
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 8):
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 7
        while i != scores:
            intscores.append(int(scoreonly[i]))
            i += 1


        '''Quick Sort Algorithm'''
        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
          
            for j in range(low, high):
          
                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
          
                    # increment index of smaller element
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
          
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
          
        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index
          
        # Function to do Quick sort
          
          
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
          
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)
          
                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)


        def check(score, sclist):
                if sclist == []:
                        return False
                elif score > sclist[0]:
                        return True
                else:
                        return check(score, sclist[1:])


        top7 = (nameonly, intscores) #tuple with names and scores
        names = top7[0] #names list
        scores = top7[1] #scores list
        user_name = str(name.get())
        user_score = score
        check = check(user_score, scores)
        if check == True:
                scores.append(user_score) #append the user's score
                n = len(scores) - 1 #variable for quick sort method
                sort = quickSort(scores, 0, n) #sorts the new list
                scores.reverse() #inverts the order of the array
                i = scores.index(user_score) #takes the new score's index
                names.insert(i, user_name) #adds the username in the index of the user score
                names = names[: -1] #finally, deletes the least score and name
                scores = scores[: -1]
        fortxt = ["Top 7 Players by score"] + names + [""] + ["Respective score"] + scores
        return fortxt
    
    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second
        global score
        global userlife
        userlife = 3
        score = 0
        second = 0
        game.destroy() #destroy the game window by the 'main menu' button

    """Obstacles movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        obstacle1 = Thread(target = create_obs1, args = ()) #thread that calls the function that produces the movement
        obstacle1.start() #starts the movement thread
        obstacle2 = Thread(target = create_obs2, args = ()) #thread that calls the function that produces the movement
        obstacle2.start() #starts the movement thread
        obstacle3 = Thread(target = create_obs3, args = ()) #thread that calls the function that produces the movement
        obstacle3.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        global second
        global score
        global userlife
        global score2
        
        while True:
            if second == 60:
                score2 = score
                nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                nextth.start() #start the thread
                messagebox.showinfo(message = 'YOU WON!  Your score is: ' + str(score2) + '. Keep going')
                level2th = Thread(target = game2, args = ()) #thread that calls the destroygame function
                level2th.start() #start the thread
            else:
                time.sleep(1)
                second += 1
                score += 1
                countdown.config(text = "Timer: " + str(second)) #set the actual time to the tag that shows it
                scoreindicator.config(text = "Score: " + str(score)) #set the actual score to the tag that shows it
            
    """Obstacle movement_______________________________________________________________________________________________________"""
    def create_obs1():
        ufo1 = gamecanvas.create_image(18, 50, image = ufoimg)
        move_obstacle(ufo1)
        
    def create_obs2():
        ufo2 = gamecanvas.create_image(200, 50, image = ufoimg)
        move_obstacle(ufo2)
        
    def create_obs3():
        ufo3 = gamecanvas.create_image(400, 50, image = ufoimg)
        move_obstacle(ufo3)
        
    def move_obstacle(ufo):
        global userlife
        global score
        global score2
        
        x = random.randint(10, 20)
        y = random.randint(10, 20)
        
        while True:
            ufopos = gamecanvas.coords(ufo) #canvas function that receives the coordinates of the obstacles
            userpos = gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship
            randact = random.randint(0, 10)
            
            if ufopos[0] + 18 >= 450: #if the obstacle reaches the right edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = - random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
    
            elif ufopos[0] - 18 <= 0: #if the obstacle reaches the left edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
            
            elif ufopos[1] + 18 >= 650: #if the obstacle reaches the lower edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = - random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                
            elif ufopos[1] - 18 <= 0: #if the obstacle reaches the upper edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                    
            elif (int(ufopos[0]) in range(int(userpos[0] - 30), int(userpos[0] + 30))) and (int(ufopos[1]) in range(int(userpos[1] - 36), int(userpos[1] + 36))):
                time.sleep(0.1)
                userlife -= 1 #subtracts 1 life point from the userlife variable
                ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
                ulifeth.start() #starts the user's life modification thread
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('hitmarker.mp3') #loads the hitmarker sound
                mixer.music.play() #plays the sound
                if userlife <= 0:
                    top7th = Thread(target = top7set, args = ()) #thread that calls the function of the top7 modification
                    top7th.start() #starts the top7 modification thread
                    score2 = score
                    time.sleep(0.5)
                    pygame.mixer.init() #initialize the mixer
                    mixer.music.load('explosionsound.wav') #loads the explosion sound
                    mixer.music.play() #plays the sound
                    gamecanvas.delete(user) #deletes the user
                    time.sleep(1)
                    loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    loseth.start() #start the thread
                else:
                    gamecanvas.delete(ufo) #deletes the ufo
                    break
            else:
                time.sleep(0.1)
                gamecanvas.move(ufo, x, y)


    """Keys functions________________________________________________________________________________________________________________________"""
    #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()

"""Game 2 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def game2():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light 2") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    game.resizable(False, False)
    
    """Canvas widget_______________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650) #create the canvas widget where the animation is going to occu
    spacebg = gamecanvas.create_image(230, 350, image = space)
    user = gamecanvas.create_image(240, 500, image = userimg) #user's spaceship

    """User's life functions____________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them
    
    """Top 7 Set_____________________________________________________________________________________________________________________"""
    def top7set():
        top7 = top7txt()
        with open('Top7.txt', 'w') as update:
            for i in top7: #cycle that writes down the information in the .txt
                update.write(str(i))
                update.write("\n")
    
    def top7txt():
        alltext = []
        with open('Top7.txt', 'r') as top7:
            for line in top7.readlines():
                alltext.append(line)

        allminusn = []
        for line in alltext:
            minusn = line.replace("\n", "")
            allminusn.append(minusn)

        scoreonly = allminusn
        n = 10
        while n != 0:
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 8):
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 7
        while i != scores:
            intscores.append(int(scoreonly[i]))
            i += 1


        '''Quick Sort Algorithm'''
        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
          
            for j in range(low, high):
          
                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
          
                    # increment index of smaller element
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
          
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
          
        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index
          
        # Function to do Quick sort
          
          
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
          
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)
          
                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)


        def check(score, sclist):
                if sclist == []:
                        return False
                elif score > sclist[0]:
                        return True
                else:
                        return check(score, sclist[1:])


        top7 = (nameonly, intscores) #tuple with names and scores
        names = top7[0] #names list
        scores = top7[1] #scores list
        user_name = str(name.get())
        user_score = score2
        check = check(user_score, scores)
        if check == True:
                scores.append(user_score) #append the user's score
                n = len(scores) - 1 #variable for quick sort method
                sort = quickSort(scores, 0, n) #sorts the new list
                scores.reverse() #inverts the order of the array
                i = scores.index(user_score) #takes the new score's index
                names.insert(i, user_name) #adds the username in the index of the user score
                names = names[: -1] #finally, deletes the least score and name
                scores = scores[: -1]
        fortxt = ["Top 7 Players by score"] + names + [""] + ["Respective score"] + scores
        return fortxt
    
    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second
        global score2
        global userlife
        userlife = 3
        score2 = 0
        second = 0
        game.destroy() #destroy the game window by the 'main menu' button

    """Obstacles movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        obstacle1 = Thread(target = create_obs1, args = ()) #thread that calls the function that produces the movement
        obstacle1.start() #starts the movement thread
        obstacle2 = Thread(target = create_obs2, args = ()) #thread that calls the function that produces the movement
        obstacle2.start() #starts the movement thread
        obstacle3 = Thread(target = create_obs3, args = ()) #thread that calls the function that produces the movement
        obstacle3.start() #starts the movement thread
        obstacle4 = Thread(target = create_obs4, args = ()) #thread that calls the function that produces the movement
        obstacle4.start() #starts the movement thread
        obstacle5 = Thread(target = create_obs5, args = ()) #thread that calls the function that produces the movement
        obstacle5.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        global second
        global score2
        global userlife
        global score3
        
        while True:
            if second == 61:
                score3 = score2
                nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                nextth.start() #start the thread
                messagebox.showinfo(message = 'YOU WON!  Your score is: ' + str(score3) + '. Keep going')
                level3th = Thread(target = game3, args = ()) #thread that calls the destroygame function
                level3th.start() #start the thread
            else:
                time.sleep(1)
                second += 1
                score2 += 3
                countdown.config(text = "Timer: " + str(second)) #set the actual time to the tag that shows it
                scoreindicator.config(text = "Score: " + str(score2)) #set the actual score to the tag that shows it
            
    """Obstacle movement_______________________________________________________________________________________________________"""
    def create_obs1():
        ufo1 = gamecanvas.create_image(18, 50, image = ufoimg)
        move_obstacle(ufo1)
        
    def create_obs2():
        ufo2 = gamecanvas.create_image(118, 50, image = ufoimg)
        move_obstacle(ufo2)
        
    def create_obs3():
        ufo3 = gamecanvas.create_image(218, 50, image = ufoimg)
        move_obstacle(ufo3)

    def create_obs4():
        ufo4 = gamecanvas.create_image(318, 50, image = ufoimg)
        move_obstacle(ufo4)

    def create_obs5():
        ufo5 = gamecanvas.create_image(418, 50, image = ufoimg)
        move_obstacle(ufo5)
        
    def move_obstacle(ufo):
        global userlife
        global score2
        global score3
        
        x = random.randint(10, 20)
        y = random.randint(10, 20)
        
        while True:
            ufopos = gamecanvas.coords(ufo) #canvas function that receives the coordinates of the obstacles
            userpos = gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship
            randact = random.randint(0, 10)
            
            if ufopos[0] + 18 >= 450: #if the obstacle reaches the right edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = - random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
    
            elif ufopos[0] - 18 <= 0: #if the obstacle reaches the left edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
            
            elif ufopos[1] + 18 >= 650: #if the obstacle reaches the lower edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = - random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                
            elif ufopos[1] - 18 <= 0: #if the obstacle reaches the upper edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                    
            elif (int(ufopos[0]) in range(int(userpos[0] - 30), int(userpos[0] + 30))) and (int(ufopos[1]) in range(int(userpos[1] - 36), int(userpos[1] + 36))):
                time.sleep(0.1)
                userlife -= 1 #subtracts 1 life point from the userlife variable
                ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
                ulifeth.start() #starts the user's life modification thread
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('hitmarker.mp3') #loads the hitmarker sound
                mixer.music.play() #plays the sound
                if userlife <= 0:
                    top7th = Thread(target = top7set, args = ()) #thread that calls the function of the top7 modification
                    top7th.start() #starts the top7 modification thread
                    score3 = score2
                    time.sleep(0.5)
                    pygame.mixer.init() #initialize the mixer
                    mixer.music.load('explosionsound.wav') #loads the explosion sound
                    mixer.music.play() #plays the sound
                    gamecanvas.delete(user) #deletes the user
                    time.sleep(1)
                    loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    loseth.start() #start the thread
                else:
                    gamecanvas.delete(ufo) #deletes the ufo
                    break
            else:
                time.sleep(0.1)
                gamecanvas.move(ufo, x, y)


    """Keys functions________________________________________________________________________________________________________________________"""
    #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score2), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()
    
    
"""Game 3 Window______________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________
___________________________________________________________________________________________________________________________________________"""
def game3():
    game = Toplevel() #creates the game window
    game.title("Operation Moon Light 2") #gives the game window a title
    game.geometry("630x750") #gives the game window its dimensions
    game.configure(background = "midnightblue") #configure the window background color
    game.resizable(False, False)
    
    """Canvas widget_________________________________________________________________________________________________________________"""
    gamecanvas = Canvas(game, width = 450, height = 650) #create the canvas widget where the animation is going to occu
    spacebg = gamecanvas.create_image(230, 350, image = space)
    user = gamecanvas.create_image(240, 500, image = userimg) #user's spaceship

    """User's life functions____________________________________________________________________________________________________________"""
    def ulifeassignation():
        ulifeindicator.config(text = "Life: " + str(userlife)) #set the actual user life points to the tag that show them

    """Top 7 Set_____________________________________________________________________________________________________________________"""
    def top7set():
        top7 = top7txt()
        with open('Top7.txt', 'w') as update:
            for i in top7: #cycle that writes down the information in the .txt
                update.write(str(i))
                update.write("\n")
    
    def top7txt():
        alltext = []
        with open('Top7.txt', 'r') as top7:
            for line in top7.readlines():
                alltext.append(line)

        allminusn = []
        for line in alltext:
            minusn = line.replace("\n", "")
            allminusn.append(minusn)

        scoreonly = allminusn
        n = 10
        while n != 0:
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 8):
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 7
        while i != scores:
            intscores.append(int(scoreonly[i]))
            i += 1


        '''Quick Sort Algorithm'''
        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
          
            for j in range(low, high):
          
                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
          
                    # increment index of smaller element
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
          
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
          
        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index
          
        # Function to do Quick sort
          
          
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
          
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)
          
                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)


        def check(score, sclist):
                if sclist == []:
                        return False
                elif score > sclist[0]:
                        return True
                else:
                        return check(score, sclist[1:])


        top7 = (nameonly, intscores) #tuple with names and scores
        names = top7[0] #names list
        scores = top7[1] #scores list
        user_name = str(name.get())
        user_score = score3
        check = check(user_score, scores)
        if check == True:
                scores.append(user_score) #append the user's score
                n = len(scores) - 1 #variable for quick sort method
                sort = quickSort(scores, 0, n) #sorts the new list
                scores.reverse() #inverts the order of the array
                i = scores.index(user_score) #takes the new score's index
                names.insert(i, user_name) #adds the username in the index of the user score
                names = names[: -1] #finally, deletes the least score and name
                scores = scores[: -1]
        fortxt = ["Top 7 Players by score"] + names + [""] + ["Respective score"] + scores
        return fortxt
    
    """Destruction of the game window_______________________________________________________________________________________________________________"""
    def destroygame():
        #reset all the values for future uses if the window isn't closed
        global second
        global score3
        global userlife
        userlife = 3
        score3 = 0
        second = 0
        game.destroy() #destroy the game window by the 'main menu' button

    """Obstacles movement function and timer function thread_________________________________________________________________________"""
    def startthread():
        obstacle1 = Thread(target = create_obs1, args = ()) #thread that calls the function that produces the movement
        obstacle1.start() #starts the movement thread
        obstacle2 = Thread(target = create_obs2, args = ()) #thread that calls the function that produces the movement
        obstacle2.start() #starts the movement thread
        obstacle3 = Thread(target = create_obs3, args = ()) #thread that calls the function that produces the movement
        obstacle3.start() #starts the movement thread
        obstacle4 = Thread(target = create_obs4, args = ()) #thread that calls the function that produces the movement
        obstacle4.start() #starts the movement thread
        obstacle5 = Thread(target = create_obs5, args = ()) #thread that calls the function that produces the movement
        obstacle5.start() #starts the movement thread
        obstacle6 = Thread(target = create_obs6, args = ()) #thread that calls the function that produces the movement
        obstacle6.start() #starts the movement thread
        obstacle7 = Thread(target = create_obs7, args = ()) #thread that calls the function that produces the movement
        obstacle7.start() #starts the movement thread
        timer = Thread(target = starttimer, args = ()) #thread that calls the function of the timer
        timer.start() #starts the timer thread
    
    """Timer Functions_______________________________________________________________________________________________________________"""
    def starttimer():
        global second
        global userlife
        global score3
        global score4
        
        while True:
            if second == 61:
                top7th = Thread(target = top7set, args = ()) #thread that calls the function of the top7 modification
                top7th.start() #starts the top7 modification thread
                time.sleep(1.5)
                score4 = score3
                nextth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                nextth.start() #start the thread
                messagebox.showinfo(message = 'YOU WON!  Your score is: ' + str(score4) + '. Keep going')
                score4 = 0
            else:
                time.sleep(1)
                second += 1
                score3 += 5
                countdown.config(text = "Timer: " + str(second)) #set the actual time to the tag that shows it
                scoreindicator.config(text = "Score: " + str(score3)) #set the actual score to the tag that shows it
            
    """Obstacle movement_______________________________________________________________________________________________________"""
    def create_obs1():
        ufo1 = gamecanvas.create_image(18, 50, image = ufoimg)
        move_obstacle(ufo1)
        
    def create_obs2():
        ufo2 = gamecanvas.create_image(168, 50, image = ufoimg)
        move_obstacle(ufo2)
        
    def create_obs3():
        ufo3 = gamecanvas.create_image(318, 50, image = ufoimg)
        move_obstacle(ufo3)

    def create_obs4():
        ufo4 = gamecanvas.create_image(418, 50, image = ufoimg)
        move_obstacle(ufo4)

    def create_obs5():
        ufo5 = gamecanvas.create_image(93, 80, image = ufoimg)
        move_obstacle(ufo5)

    def create_obs6():
        ufo6 = gamecanvas.create_image(243, 80, image = ufoimg)
        move_obstacle(ufo6)

    def create_obs7():
        ufo7 = gamecanvas.create_image(393, 80, image = ufoimg)
        move_obstacle(ufo7)
        
    def move_obstacle(ufo):
        global userlife
        global score3
        global score4

        x = random.randint(10, 20)
        y = random.randint(10, 20)
        
        while True:
            ufopos = gamecanvas.coords(ufo) #canvas function that receives the coordinates of the obstacles
            userpos = gamecanvas.coords(user) #canvas function that receives the coordinates of the user's spaceship
            randact = random.randint(0, 10)
            
            if ufopos[0] + 18 >= 450: #if the obstacle reaches the right edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = - random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
    
            elif ufopos[0] - 18 <= 0: #if the obstacle reaches the left edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                x = random.randint(10, 20)
                if randact % 3 == 0:
                    y = -y
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
            
            elif ufopos[1] + 18 >= 650: #if the obstacle reaches the lower edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = - random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                
            elif ufopos[1] - 18 <= 0: #if the obstacle reaches the upper edge, it moves randomly
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('metalhit.mp3') #loads the metalhit sound
                mixer.music.play() #plays the sound
                time.sleep(0.1)
                y = random.randint(10, 20)
                if randact % 3 == 0:
                    x = -x
                    gamecanvas.move(ufo, x, y)
                else:
                    gamecanvas.move(ufo, x, y)
                    
            elif (int(ufopos[0]) in range(int(userpos[0] - 30), int(userpos[0] + 30))) and (int(ufopos[1]) in range(int(userpos[1] - 36), int(userpos[1] + 36))):
                time.sleep(0.1)
                userlife -= 1 #subtracts 1 life point from the userlife variable
                ulifeth = Thread(target = ulifeassignation, args = ()) #thread that calls the function of the user's life modification
                ulifeth.start() #starts the user's life modification thread
                pygame.mixer.init() #initialize the mixer
                mixer.music.load('hitmarker.mp3') #loads the hitmarker sound
                mixer.music.play() #plays the sound
                if userlife <= 0:
                    top7th = Thread(target = top7set, args = ()) #thread that calls the function of the top7 modification
                    top7th.start() #starts the top7 modification thread
                    time.sleep(0.5)
                    pygame.mixer.init() #initialize the mixer
                    mixer.music.load('explosionsound.wav') #loads the explosion sound
                    mixer.music.play() #plays the sound
                    gamecanvas.delete(user) #deletes the user
                    time.sleep(1)
                    loseth = Thread(target = destroygame, args = ()) #thread that calls the destroygame function
                    loseth.start() #start the thread
                else:
                    gamecanvas.delete(ufo) #deletes the ufo
                    break
            else:
                time.sleep(0.1)
                gamecanvas.move(ufo, x, y)


    """Keys functions________________________________________________________________________________________________________________________"""
    #x and y are the number of positions the user's spaceship is going to move from its original position
    def left(event):
        x = -20 
        y = 0
        gamecanvas.move(user, x, y) #moves the ship -20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def right(event):
        x = 20
        y = 0
        gamecanvas.move(user, x, y) #moves the ship 20 spaces in the x direction and 0 spaces in the y direction, from its original position

    def up(event):
        x = 0
        y = -20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and -20 spaces in the y direction, from its original position

    def down(event):
        x = 0
        y = 20
        gamecanvas.move(user, x, y) #moves the ship 0 spaces in the x direction and 20 spaces in the y direction, from its original position
                        
    """Keys Binding______________________________________________________________________________________________________________________"""

    game.bind("<Left>", left) #binds the left key to the left movement function
    game.bind("<Right>", right) #binds the right key to the left movement function
    game.bind("<Up>", up) #binds the up key to the left movement function
    game.bind("<Down>", down) #binds the down key to the left movement function
    
    """Buttons of the game window___________________________________________________________________________________________________________"""
    startgame = tk.Button(game, text = "Start", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = startthread)
    startgame.place(x = 50, y = 10) #start the game
    
    game_mainnmenu = tk.Button(game, text = "Main Menu", font = ("Comic Sans MS", 10), bg = "white", fg = "midnightblue", command = destroygame)
    game_mainnmenu.place(x = 110, y = 10) #return to the main menu, losing the user's record
    
    """Labels of the game window___________________________________________________________________________________________________________"""    
    n = name.get() #Gets the user's name
    username = tk.Label(game, text = "User: " + n, font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue")
    username.place(x = 510, y = 100) #Label where the user's name is written

    countdown = tk.Label(game, text = "Timer: " + str(second), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the time is written
    countdown.place(x = 510, y = 140) #place the timer label

    scoreindicator = tk.Label(game, text = "Score: " + str(score3), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the score is written
    scoreindicator.place(x = 510, y = 180) #place the score label
    
    ulifeindicator = tk.Label(game, text = "Life: " + str(userlife), font = ("Comic Sans MS", 10), fg = "ghostwhite", bg = "midnightblue") #Label where the user's life is written
    ulifeindicator.place(x = 510, y = 220) #place the user's life label
    
    """Canvas configuration_________________________________________________________________________________________________________________"""
    gamecanvas.place(x = 50, y = 50) #place the canvas widget  
    game.mainloop()
    
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
