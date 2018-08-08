from tkinter import *

mainWindow = Tk()

canvas = Canvas(mainWindow, width=200, height=100)
canvas.pack()

#create lines
blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")

# create a rectangle
greenbox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# delete the redline
canvas.delete(redline)

# deletes everything on the canvas
canvas.delete(ALL)

mainWindow.mainloop()