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

insert = Button(toolbar, text="Insert Iext", command=doNothing)
insert.grid(row=0, column=0, padx=2, pady=2)

undo = Button(toolbar, text="Undo", command=doNothing)
undo.grid(row=0, column=1, padx=2, pady=2)

toolbar.grid(side=TOP, fill=X)

# create the widgets
label_1 = Label(mainWindow, text="Name")
label_2 = Label(mainWindow, text="Password")
entry_1 = Entry(mainWindow)
entry_2 = Entry(mainWindow)
checkBox_1 = Checkbutton(mainWindow, text="Keep me logged in.")

# Place the widget
label_1.grid(row=1, column=0, sticky=E)
label_2.grid(row=2, column=0, sticky=E)
entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
checkBox_1.grid(columnspan=2)

mainWindow.mainloop()