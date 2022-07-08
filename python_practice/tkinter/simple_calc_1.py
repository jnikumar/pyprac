from tkinter import *
from webbrowser import get
from tkmacosx import *

# root widget or window to hold all the other elements
simple_calc = Tk()
simple_calc.configure(background='white')
simple_calc.title("Simple Calculator")

# input field to capture inputs of numbers

inp = Entry(simple_calc, width=40, borderwidth=5)
inp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_clear():
    inp.delete(0, END)
#


def button_num(num):
    global curr_num
    curr_num = 0
    if inp.get() == '':
        curr_num = 0
    else:
        curr_num = inp.get()
    #

    inp.delete(0, END)
    inp.insert(0, (float(curr_num))*10 + num)
#


def button_calculate(code):
    global f_num, calc_code    
    
    f_num = float(inp.get())
    calc_code = code
    inp.delete(0, END) #clear the input box
#

def button_equal():
    
    s_num = inp.get()
    inp.delete(0,END)
    try:
        if calc_code == 1:
            inp.insert(0,f_num + float(s_num))
        elif calc_code == 2:
            inp.insert(0,f_num - float(s_num))
    except NameError:
        print("here")
        inp.insert(0,s_num)

#


# define buttons for digits
button_1 = Button(simple_calc, text="1", padx=15,
                  pady=15, command=lambda: button_num(1))
button_2 = Button(simple_calc, text="2", padx=15,
                  pady=15, command=lambda: button_num(2))
button_3 = Button(simple_calc, text="3", padx=15,
                  pady=15, command=lambda: button_num(3))
button_4 = Button(simple_calc, text="4", padx=15,
                  pady=15, command=lambda: button_num(4))
button_5 = Button(simple_calc, text="5", padx=15,
                  pady=15, command=lambda: button_num(5))
button_6 = Button(simple_calc, text="6", padx=15,
                  pady=15, command=lambda: button_num(6))
button_7 = Button(simple_calc, text="7", padx=15,
                  pady=15, command=lambda: button_num(7))
button_8 = Button(simple_calc, text="8", padx=15,
                  pady=15, command=lambda: button_num(8))
button_9 = Button(simple_calc, text="9", padx=15,
                  pady=15, command=lambda: button_num(9))
button_0 = Button(simple_calc, text="0", padx=15,
                  pady=15, command=lambda: button_num(0))

# buttons for functions
button_clr = Button(simple_calc, text="Clear", padx=15,
                    pady=15, command=button_clear)
button_add = Button(simple_calc, text="+", padx=15, pady=15,
                    command=lambda: button_calculate(1))
button_sub = Button(simple_calc, text="-", padx=15, pady=15,
                    command=lambda: button_calculate(2))
button_eq = Button(simple_calc, text="=", padx=80,
                   pady=15, command=button_equal)

# place buttons on the window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)

button_clr.grid(row=5, column=0)
button_eq.grid(row=5, column=1, columnspan=2)

# create a loop for the root widget to be showing
simple_calc.mainloop()
