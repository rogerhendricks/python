from tkinter import *

mainWindow = Tk()
#function to print with an event argument
def printName(event):
    print("Hello Roger!")

# create the button
button_1 = Button(mainWindow, text="Print my name")

# binding left button to printName function
button_1.bind("<Button-1>", printName)

# display the button
button_1.pack()

mainWindow.mainloop()