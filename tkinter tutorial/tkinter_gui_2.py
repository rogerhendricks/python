from tkinter import *

mainWindow = Tk()

one = Label(mainWindow, text="One", bg = "red", fg="white")
one.pack()
two = Label(mainWindow, text="Two", bg = "black", fg="green")
two.pack(fill=X)

three = Label(mainWindow, text="Three", bg = "blue", fg="white")
three.pack(side=LEFT, fill=Y)
mainWindow.mainloop()