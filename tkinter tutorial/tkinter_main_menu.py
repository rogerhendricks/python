from tkinter import *

def doNothing():
    print("Do nothing!")

mainWindow = Tk()
# Create top menu bar
menu = Menu(mainWindow)
mainWindow.config(menu=menu)

# create the file menu dropdown
fileMenu = Menu(menu)
# create the menu type
menu.add_cascade(label="File", menu=fileMenu)
# the menu items and labels that call a function that does something
fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New", command=doNothing)
# creates a seperator
fileMenu.add_separator()
#the Exit button on the buttom
fileMenu.add_command(label="Exit", command=doNothing)

# creates the next menu 
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

mainWindow.mainloop()