from tkinter import *

#root widgeet or window to hold all the other elements
root = Tk()

#crate a label widget
myLabel = Label(root, text = "Hello Tkinter")
#put it on to the root screen
myLabel.pack()

#create a loop for the root widget to be showing
root.mainloop()