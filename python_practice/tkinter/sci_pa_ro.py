'''
Sciscor Paper Rock Game
Simple simulation
'''
import random


def get_winner(syso, usero):
    # 0 for draw, 1 for system, 2 for user
    # syso is system option, usero is user option
    if syso == 1 and usero == 2 or syso == 2 and usero == 3 or syso == 3 and usero == 1:
        return 1
    elif syso == 1 and usero == 3 or syso == 2 and usero == 1 or syso == 3 and usero == 2:
        return 2
    else:
        return 0
#

def get_sys_option(syso):
    pass
    if syso == 1:
        print("System choice: Sciscor")
    elif syso == 2:
        print("System choice: Paper")
    elif syso == 3:
        print("System choice: Rock")


def welcome():
    pass
    global myPath
    global game_info_file
    global pl_name

    print(f"Welcome to the game {pl_name}...\n")
    with open(myPath+game_info_file, 'r') as f:
        pass
        for line in f:
            print(line)
# end welcome


def get_input():
    pass
    global pl_name
    print("Welcome, let's play Scissor Paper Rock.... ")
    pl_name = input("Enter your name: ")
    welcome()
# end get input

# driver code

# variables
global pl_score, sys_score, draw_score
global pl_name
global game_info_file
global myPath
global user_option, sys_option
pl_score = sys_score = draw_score = 0

myPath = "/Users/nijosyula/Personal/IGNOU/PGDCA/python_practice/tkinter/"
game_info_file = "sci_pa_ro_info.txt"

get_input()
while 1 < 2:
    print("Current Score is...")
    print(f"System: {sys_score} You: {pl_score} DRAW: {draw_score}")
    print("1. Sciscor - Enter 1 to chose Sciscor")
    print("2. Paper - Enter 2 to chose Paper")
    print("3. Rock - Enter 3 to chose Rock")
    print("4. Exit - Enter 0 (ZERO) to Exit")
    user_option = input("Enter 1, 2 or 3...: ")
    if user_option == "1":
        print("Your choice: Sciscor...")
    elif user_option == "2":
        print("Your choice: Paper...")
    elif user_option == "3":
        print("Your choice: Rock...")
    elif user_option == "0":
        print(f"Thank you {pl_name}, hope you liked it")
        print("Good bye....")
        print(f"Final Score:")
    
        break
    else:
        print("Invalid option! Try again...")
        continue

    sys_option = random.randint(1, 3)
    get_sys_option(sys_option)
    win = get_winner(sys_option, int(user_option))
    if win == 0:
        pass
        draw_score += 1
        print("It's a draw...")
    elif win == 1:
        pass
        sys_score += 1
        print("System wins! Better luck next time...")
    elif win == 2:
        pass
        pl_score += 1
        print("Awesome!! YOU WIN!!! Keep Going...")
#print("this is to test multi line strings and see if they are printed properly or not on the output")
