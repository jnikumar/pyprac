from tkinter import *

#root widgeet or window to hold all the other elements
root = Tk()
root.configure(bg="#FFFFFF")

#crate a label widget
myLabel1 = Label(root, text = "Hello Tkinter")
myLabel2 = Label(root, text = "Practicing GUI Development")
#put it on to the root screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

x = 1
print(type(x))

#create a loop for the root widget to be showing
root.mainloop()