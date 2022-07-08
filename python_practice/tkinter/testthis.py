
from tkinter import *
from tkmacosx import *
from time import *
import random

myMain = Tk()
myMain.configure(background="white")
myMain.title("Welcome to the Number Guessing Game....")

print(type(random))

def doThis():
    print("Entry event")

def start_guessing():
    #print(guess)
    user_input = 0
    attempts = 0
    label_info = Label(myMain, text = "Enter your guess")
    user_guess_inp = Entry(myMain, width = 20, border = 5)
    user_guess_inp.insert(0, user_input)
    label_res = Label(myMain, text = "Text")
    label_gap1 = Label(myMain, text = "                     ")
    label_gap1.configure(background="white")
    
    label_info.grid(row = 15, column = 0, columnspan = 2)
    user_guess_inp.grid(row = 15, column = 1, columnspan = 2)
    label_gap.grid(row = 16, column = 0, pady = 10, columnspan = 4)
    '''
    '''
    while user_input != guess:
        while user_guess_inp != '':
            user_guess_inp.focus_set()
        user_input = int(user_guess_inp.get())
        if user_input < guess:
            print(f"{user_input} is way too low, jump higher")
        elif user_input > guess:
            print(f"{user_input} is way too high, jump lower")
        attempts += 1
        user_guess_inp.delete(0,END)
        user_guess_inp.focus()
    '''
    '''
    #
    #label_res.grid(row = 15, column = 0, padx = 25)
    #label_res.config(text = "Test")
    #
#

def set_limit(upper):
    global guess, min_turns
    min_turns = 0
    guess = random.randint(1,upper)
    
    label_rnd = Label(myMain, text = "Random Number: ")
    rnd_inp = Entry(myMain, width = 10, border = 5)
    #rnd_inp.configure(foreground = "white")
    label_min_turns = Label(myMain, text = " Min Turns: ")
    min_turns_inp = Entry(myMain, width = 10, border = 5)
    
    label_rnd.grid(row = 13, column = 0)
    rnd_inp.grid(row = 13, column = 1)
    rnd_inp.insert(0, str(guess))
    label_min_turns.grid(row = 13, column =2)
    min_turns_inp.grid(row = 13, column = 3)
    rnd_inp.delete(0,END)
    rnd_inp.insert(0, str(guess))
    min_turns_inp.insert(0,"NA")
    label_gap.grid(row = 14, column = 0)
    
    start_guessing()
    #
#

def number_guessing():
    #
    label_play = Label(myMain, text = "Let's play the game....")
    label_play.configure(background = "white")
    label_gap.grid(row = 9, column = 0)
    label_play.grid(row = 10, column = 0, columnspan = 4)
    #
    label_limit = Label(myMain, text = "Select Range")
    button_10 = Button(myMain, text = "1 - 10", padx=10, command = lambda: set_limit(10))
    button_100 = Button(myMain, text = "1 - 100", padx=10, command = lambda: set_limit(100))
    button_1000 = Button(myMain, text = "1 - 1000", padx=10, command = lambda: set_limit(1000))
    #
    label_limit.grid(row = 11, column = 0)
    button_10.grid(row = 11, column = 1)
    button_100.grid(row = 11, column = 2)
    button_1000.grid(row = 11, column = 3)
    label_gap.grid(row = 12, column = 0)
    #
#

#Chooses to play the game
def play_game():
    global guess
    label_welcome = Label(myMain, text = "Welcome " + namebox.get() + "!!!, Let's play!!!", padx = 60)
    label_welcome.configure(background = "white", foreground = "black")
    
    label_quit = Label(myMain, text = "Click Quit to leave any time....")
    label_quit.configure(background = "white", foreground = "black")
    
    label_gap.grid(row = 5, column = 0)
    label_welcome.grid(row = 6, column = 0, columnspan = 4)
    label_gap.grid(row = 7, column = 0)
    label_quit.grid(row = 8, column = 0, columnspan = 4)
    
    number_guessing()
    #
#

#Chooses NOT to play the game
def good_bye():
    label_bye = Label(myMain, text = "Thank you " + namebox.get()) 
    label_gap.grid(row = 5, column = 0)
    label_bye.grid(row = 6, column = 0, columnspan = 4)
    sleep(5)
    myMain.quit()
    #
#

label1 = Label(myMain, text = "Enter your Name")
namebox = Entry(myMain, width=40,border=5)
namebox.focus_set()

label1.grid(row=0, column=0)
namebox.grid(row=0, column=1, columnspan=3)

label_gap = Label(myMain, text = "                     ")
label_gap.configure(background="white")
label_gap.grid(row = 1, column = 0, columnspan = 4)


label2 = Label(myMain, text = "Play number guessing game?")
button_y = Button(myMain, text = "Yes", padx=30, command = play_game)
button_n = Button(myMain, text = "Quit", padx=29, command = good_bye)

label2.grid(row = 4, column=0)
button_y.grid(row = 4, column=1)
button_n.grid(row = 4, column=2)
label_gap.grid(row = 5, column = 0, columnspan = 4)

myMain.mainloop()
