from tkinter import *
import tkinter.messagebox

mainWindow=Tk()

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 150years")

answer = tkinter.messagebox.askquestion("Question 1", "Do you like to eat?")

if answer== "yes":
    print("hotdogs it is then!")


mainWindow.mainloop()