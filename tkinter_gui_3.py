from tkinter import *

mainWindow = Tk()
# create the widgets
label_1 = Label(mainWindow, text="Name")
label_2 = Label(mainWindow, text="Password")
entry_1 = Entry(mainWindow)
entry_2 = Entry(mainWindow)
checkBox_1 = Checkbutton(mainWindow, text="Keep me logged in.")

# Place the widget
label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
checkBox_1.grid(columnspan=2)


mainWindow.mainloop()
