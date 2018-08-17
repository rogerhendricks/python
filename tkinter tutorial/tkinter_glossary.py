from tkinter import *

# main:
window = Tk()
window.title("My Coding Glossary")

# create label
Label(window, text="Enter the word you want defining:").grid(row=0, column=0, sticky=W)

# create test entry box
entry = Entry(window, width=20, bg="light green")
entry.grid(row=0, column=1, sticky=W)


# key press function
def click():
    entered_text = entry.get() # collect text from text entry box
    output.delete(0.0, END)# clear text box
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "Ther is no entry for this word."
    output.insert(END, definition)

# add a submit button:
Button(window, text="SUBMIT", width=5, command=click).grid(row=0, column=3, sticky=W)

# create another label
Label(window, text="\nDefinition:").grid(row=3, column=0, sticky=W)

# create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# The dictionary:

my_glossary = {
    'algorithm':'Step by step instructions to perform a task that a compter could understand.', 'bug':'A peice of code thsat is causing a program to fail to run properly or at all.', 'binary number':'A number represented in base 2.'
}

# Run mainloop
window.mainloop()
