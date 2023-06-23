'''
Graphic version of Scissor Paper Rock
'''

from tkinter import *
from tkmacosx import *
from PIL import ImageTk, Image
import random

def get_winner(usero, syso):
    pass
    # 0 for draw, 1 for system, 2 for user
    # syso is system option, usero is user option
    if syso == 1 and usero == 2 or syso == 2 and usero == 3 or syso == 3 and usero == 1:
        return 1
    elif syso == 1 and usero == 3 or syso == 2 and usero == 1 or syso == 3 and usero == 2:
        return 2
    else:
        return 0

def gameplay():
    global userchoice, user_score
    global systemchoice, system_score
    global draw_score
    #print(f"User Option: {userchoice}")
    #print(f"system Option: {systemchoice}")
    win = get_winner(userchoice, systemchoice)
    if win == 0:
        pass
        draw_score += 1
        #print("It's a draw...")
        draw_score_disp.configure(text = str(draw_score))
        other_win_display.configure(text = "It is a DRAW")
    elif win == 1:
        pass
        system_score += 1
        #print("System wins! Better luck next time...")
        sys_score_disp.configure(text = str(system_score))
        other_win_display.configure(text = "System Wins!!! Better luck next time")
    elif win == 2:
        pass
        user_score += 1
        #print("Awesome!! YOU WIN!!! Keep Going...")
        user_score_disp.configure(text = str(user_score))
        user_win_display.configure(text = "Rooockking!! You win!!")
    #print(f"Your Score: {user_score} System Score: {system_score} Draw: {draw_score}")
    pass

def system_play():
    global systemchoice
    systemchoice = random.randint(1, 3)
    sys_but_list[systemchoice-1].configure(state = NORMAL,background = "BLUE")
    #print(systemchoice)
    comp_select.configure(image = sys_img_list[systemchoice-1], width = 80, height = 80)
    gameplay()
    pass

def disable_sys_choice():
    pass
    comp_sci_but.configure(state = DISABLED)
    comp_pap_but.configure(state = DISABLED)
    comp_roc_but.configure(state = DISABLED)

def selected(choice):
    global userchoice
    userchoice = choice
    #print(userchoice)
    user_select.configure(image = usr_img_list[userchoice-1], height = 80, width = 80)
    user_win_display.configure(text = "")
    other_win_display.configure(text = "")
    disable_sys_choice()
    system_play()
#
    

#driver code
global myPath 
global game_info_file
global game_img
global userchoice
global systemchoice
global user_score
global system_score
global draw_score

user_score = system_score = draw_score = 0

#path variable & file names
myPath = "/Users/nijosyula/Personal/IGNOU/PGDCA/pyprac/python_practice/tkinter/"
game_info_file = "sci_pa_ro_info.txt"
game_img = "spr_main.ico"
sci_img = "sci.jpg"
roc_img = "rock.jpg"
pap_img = "pap1.jpg"
comp_sci = "comp_sci.jpg"
comp_pap = "comp_paper.jpg"
comp_roc = "comp_rock.jpg"

#main tkinter components
myMain = Tk()
myMain.title("Scissor Paper Rock")
myMain.iconbitmap(myPath+game_img)
exit_game = Button(myMain, text = "Quit", command = myMain.quit)

my_sci = ImageTk.PhotoImage(Image.open(myPath + sci_img))
sci_holder = Label(image = my_sci)
#sci_holder.pack()

my_pap = ImageTk.PhotoImage(Image.open(myPath + pap_img))
pap_holder = Label(image = my_pap)
#pap_holder.pack()

my_roc = ImageTk.PhotoImage(Image.open(myPath + roc_img))
roc_holder = Label(image = my_roc)
#roc_holder.pack()

com_sci = ImageTk.PhotoImage(Image.open(myPath + comp_sci))
com_paper = ImageTk.PhotoImage(Image.open(myPath + comp_pap))
com_rock = ImageTk.PhotoImage(Image.open(myPath + comp_roc))

#user choices
sci_but = Button(myMain, image = my_sci, height = 80, width = 80, command = lambda:selected(1))
sci_but.grid(row = 2, column = 0)

pap_but = Button(myMain, image = my_pap, height = 80, width = 80, command = lambda:selected(2))
pap_but.grid(row = 2, column = 1)

roc_but = Button(myMain, image = my_roc, height = 80, width = 80, command = lambda:selected(3))
roc_but.grid(row = 2, column = 2)

usr_img_list = [my_sci, my_pap, my_roc]

#computer choices
comp_sci_but = Button(myMain, image = com_sci, height = 80, width = 80, state = DISABLED)
comp_sci_but.grid(row = 5, column = 0)
''''''
comp_pap_but = Button(myMain, image = com_paper, height = 80, width = 80, state = DISABLED)
comp_pap_but.grid(row = 5, column = 1)

comp_roc_but = Button(myMain, image = com_rock, height = 80, width = 80, state = DISABLED)
comp_roc_but.grid(row = 5, column = 2)

sys_but_list = [comp_sci_but, comp_pap_but, comp_roc_but]
sys_img_list = [com_sci, com_paper, com_rock]

#choice holders
user_select = Label(myMain, text = "User Choice", height = 5, width = 10)
comp_select = Label(myMain, text = "System Choice", height = 5, width = 10)

user_select.grid(row = 3, column = 1)
comp_select.grid(row = 4, column = 1)
''''''
#score holders
user_score_label = Label(myMain, text = "Your Score", width = 10, pady = 10, padx = 5, relief = RAISED)
user_score_disp = Label(myMain, text = "0", width = 10, pady = 10, relief = SUNKEN)

sys_score_label = Label(myMain, text = "System Score", width = 10, pady = 10, relief = RAISED)
sys_score_disp = Label(myMain, text = "0", width = 10, pady = 10, relief = SUNKEN)

draw_score_label = Label(myMain, text = "Draw", width = 10, pady = 10, padx = 10, relief = RAISED)
draw_score_disp = Label(myMain, text = "0", width = 10, pady = 10, relief = SUNKEN)

#display

user_win_display = Label(myMain, text = "", width = 10, height = 10, relief = SUNKEN, anchor = "w", justify = CENTER, wraplength = 100)
other_win_display = Label(myMain, text = "", width = 10, height = 10, relief = SUNKEN, anchor = "w", justify = CENTER, wraplength = 100)

user_score_label.grid(row = 0, column = 0)
user_score_disp.grid(row = 1, column = 0)

sys_score_label.grid(row = 0, column = 1)
sys_score_disp.grid(row = 1, column = 1)

draw_score_label.grid(row = 0, column = 2)
draw_score_disp.grid(row = 1, column = 2)

user_win_display.grid(row = 3, column = 0, rowspan = 2)
other_win_display.grid(row = 3, column = 2, rowspan = 2)

exit_game.grid(row = 6, columnspan = 3, pady = 10)
myMain.mainloop()