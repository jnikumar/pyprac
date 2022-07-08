'''
Simple number guessing game
Random number will picked within a range
Player/User will be asked to guess and given
hints if guess is lower or higer than the random
number generated
# of turns will be saved to see the minimum
turns taken the player/user
'''
from tkinter import *
import random

def get_min_turns(min_turns, attempts):
    if min_turns == 0:
        return attempts
    else:
        return attempts if attempts < min_turns else min_turns
#
def set_game_limit(game_limit):
    while game_limit != 1 or game_limit != 2 or game_limit != 3 :
        if(game_limit == 1):
            return(random.randint(1,10), 10)
        elif(game_limit == 2):
            return(random.randint(1,100), 100)
        elif(game_limit == 3):
            return(random.randint(1,1000), 1000)
        print("Invalid input....")
        game_limit = int(input("Enter 1 or 2 or 3: "))
#

player_name = input("Please enter your name to start playing: ")
print("Enter Y/Yes or N/No")
choice = input("Do you want to play a number guessing game: ")
min_turns = 0
a = 1
b = 2
'''
Continue to play the game as long as 
the player is interested - choice is yes or y
'''
while choice.lower() == "y" or choice.lower() == "yes":
    print("1. Guess number between 1 to 10")
    print("2. Guess number between 1 to 100")
    print("3. Guess number between 1 to 1000")
    game_limit = int(input("Enter 1 or 2 or 3: "))
    '''
    Get the boundaries of guessing game from user
    initiate the reference number using random
    number generator
    Welcome the player and start the game
    '''
    ref_number, upper_limit = set_game_limit(game_limit)
    print(f"Welcome {player_name} to guess a number between 1 & {upper_limit}")
    print(f"Start guessing, wish you good luck....")
    guess = 0
    attempts = 0
    #Continue accepting the guess till it matches 
    #the reference number
    while(guess != ref_number):
        guess = int(input("Enter your guess: "))
        if guess < ref_number:
            print(f"{guess} is way too low, jump higher")
        elif guess > ref_number:
            print(f"{guess} is way too high, jump lower")
        attempts += 1
    min_turns = get_min_turns(min_turns, attempts)
    print(f"Awesome, you have guessed it correct - {ref_number} in {attempts} attempts")
    print(f"Minimum turns taken so far is {min_turns}")
    game_limit = 0
    min_turns = attempts
    print("Enter Y/Yes or N/No")
    choice = input("Do you want to play again : \n")
#