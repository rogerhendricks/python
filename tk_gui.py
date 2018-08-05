import tkinter as tk 
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
# label
aLabel.grid(column=0, row=0)

#Button click event callback function
def clickMe():
    action.configure(text="Hello"+name.get)
# Position Button in second row, second column
action.grid(column=1, row=0)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)


win.mainloop()

