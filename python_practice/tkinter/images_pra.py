from tkinter import *
from tkmacosx import *
from PIL import ImageTk, Image

path = "/Users/nijosyula/Personal/IGNOU/PGDCA/python_practice/tkinter/"
myMain = Tk()
myMain.iconbitmap(path + "NKJ.ico")
myMain.title("Image Browser...")

my_img = ImageTk.PhotoImage(Image.open(path + "NKJ.png"))
image_holder = Label(image = my_img)
image_holder.pack()

#myMain.configure(background="white")

button_quit = Button(myMain, text = "Exit", command = myMain.quit)
button_quit.pack()
myMain.mainloop()