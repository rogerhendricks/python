from tkinter import *
import sys

def doNothing():
    print("Do nothing!")

def quitecommand():
    sys.exit()

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
fileMenu.add_command(label="Exit", command=quitecommand)

# creates the next menu 
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


#***** Toolbar *****
toolbar = Frame(mainWindow, bg="blue")

insert = Button(toolbar, text="Insert Text", command=doNothing)
insert.pack(side=LEFT, padx=2, pady=2)

undo = Button(toolbar, text="Undo", command=doNothing)
undo.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#***** Status bar *****

status =Label(mainWindow, text="Perparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mainWindow.mainloop()
