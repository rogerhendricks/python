from tkinter import *
# main window
mainWindow = Tk()

# create a top container
topFrame = Frame(mainWindow)
topFrame.pack()
# create a bottom container
bottomFrame = Frame(mainWindow)
bottomFrame.pack(side=BOTTOM)

# Create some buttons
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(bottomFrame, text="Button 3", fg="purple")

# Where to display the widgets
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)

# infinite loop to keep it open until closed button is pushed.

mainWindow.mainloop()


