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
    global f_num, s_num
    global calc_code1, calc_code2
    #print("current calculation is {calc_code1}")
    try:
        print("Not the first operation")
        if calc_code1 == 1:
            if inp.get() == '':
                s_num = 0.0
            else:
                #s_num = float(inp.get())
                s_num = curr_num
            
            inp.delete(0, END)
            f_num = f_num + s_num
            s_num = 0.0
            
            inp.insert(0, f_num)
        elif calc_code1 == 2:
            if inp.get() == '':
                s_num = 0.0
            else:
                s_num = float(inp.get())
            
            f_num = f_num - s_num
            s_num = 0.0
            inp.delete(0, END)
        elif calc_code1 == 3:
            if inp.get() == '':
                s_num = 0.0
            else:
                s_num = float(inp.get())
            
            f_num = f_num * s_num
            s_num = 0.0
            inp.delete(0, END)
        elif calc_code1 == 4:
            if inp.get() == '':
                s_num = 0.0
            else:
                s_num = float(inp.get())
            
            f_num = f_num / s_num
            s_num = 0.0
            inp.delete(0, END)
        calc_code1 = code
        calc_code2 = calc_code1
    except NameError:#first operation
        print("First operation, curr_num: {curr_num}")
        
        calc_code1 = code
        if inp.get() == '': #assign current input to f_num
            f_num = 0.0
        else:
            f_num = float(inp.get())
        
        inp.delete(0, END) #clear the input box
#

def button_equal():
    global s_num
    global f_num
    
    if inp.get() == '' :
        s_num = 0.0
    else:
        #s_num = float(inp.get())
        s_num = curr_num

    print(f"f_num: {f_num}, s_num: {s_num}, code: {calc_code1}")
    inp.delete(0, END)
    if calc_code1 == 1:
        f_num = f_num + s_num
        inp.insert(0, f_num)
        s_num = 0.0
    elif calc_code1 == 2:
        f_num = f_num - s_num
        inp.insert(0, f_num)
        s_num = 0.0
    elif calc_code1 == 3:
        f_num = f_num * s_num
        inp.insert(0, f_num)
        s_num = 0.0
    elif calc_code1 == 4:
        f_num = f_num / s_num
        inp.insert(0, f_num)
        s_num = 0.0
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
