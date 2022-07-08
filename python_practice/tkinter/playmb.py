'''
'''
from tkinter import *
from tkinter import messagebox
from turtle import clear
from tkmacosx import *
import random

def print_prime(n):
    
    for num in range (1, n+1):
        pass
        for div in range (2, num//2+1):
            pass
            if(num % div == 0):
                print(f"{num} is {div} * {num//div}")
                break
        else:
            print(f"{num} is a prime number")
    pass

def odd_even(n):
    for num in range(1, n):
        if(num % 2 == 0):
            print(f"Found even number: {num}")
            continue
        print(f"{num} is odd number")
    pass

#driver
#print_prime(25)
#odd_even(25)
my_chocies = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(random.choice(my_chocies))


'''
myMain = Tk()
mymsg = "Test Message"
messagebox.showinfo("Awesome", mymsg)
myMain.mainloop()
'''