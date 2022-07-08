from tkinter import *
#from tkmacosx import *

#root widgeet or window to hold all the other elements
root = Tk()

def myClick():
    myLabel = Button(root, text="Button Clicked!!!",highlightbackground="blue")
    myLabel.pack()

root.configure(background='blue')

#crate a button widget
myButton = Button(root, text="My Button", command=myClick)
myButton.pack()

#create a loop for the root widget to be showing
root.mainloop()