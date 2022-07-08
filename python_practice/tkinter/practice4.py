from tkinter import *
from tkmacosx import *

#root widgeet or window to hold all the other elements
root = Tk()
root.configure(background='white')

def myClick():
    row = 2
    myLabel = Label(root, text="Hello " + inp.get())
    myLabel.grid(row = row+1,column=2)

inp_label = Label(root, text = "Enter Your Name")
inp = Entry(root, bg='white')
#inp.insert(0, "Enter your name: ")
#inp.pack()
inp_label.grid(row=1, column=1)
inp.grid(row=1, column=2)


#crate a button widget
myButton = Button(root, text="My Button", command=myClick)
#myButton.pack()
myButton.grid(row=2,column=2)

#create a loop for the root widget to be showing
root.mainloop()