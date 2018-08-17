from tkinter import *
from decimal import *

# key press function:
def click(key):
    #pressing equals key means calculate:
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, "--> Error!")
    #pressing C key means clear screen:
    elif key == "C":
        display.delete(0, END)
    elif key == const_list[0]:
        display.insert(END, "3.141592654")
    elif key == const_list[1]:
        display.insert(END, "299792458")
    elif key == const_list[2]:
        display.insert(END, "343")
    elif key == const_list[3]:
        display.insert(END, "150000000000")
    # add other key pressed values to end of current entry:
    else:
        display.insert(END, key)

#### main:
window = Tk()
window.title("My Calculator")

# Create top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry widget for an editable display
display = Entry(top_row, width=28, bg="light green")
display.grid()

# Create num_pad frame:
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

# Provide a list of keys for the number pad:
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=']

# create num_pad buttons with a loop
r = 0 # row counter
c = 0 # column counter

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1


# Create operator frame:
op = Frame(window)
op.grid(row=1, column=1, sticky=E)

# Provide a list of operator keys for operator pad:
op_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']

for b in op_list:
    def cmd(x=b):
        click(x)
    Button(op, text=b, width=5, command=cmd).grid(row=r, column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

# create constants_frame:
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)

const_list = [
    'pi',
    'speed of light (m/s)',
    'speed of sound (m/s)',
    'ave dist to sun (km)'
]

for btn_text in const_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text, width=16, command=cmd).grid(row=r, column=c)
    r = r+1
# create function buttons
functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)

functions_list = [
    'factorial (!)',
    '-> roman',
    '-> binary',
    'binary -> 10'
]

for b in functions_list:
    def cmd(x=b):
        click(x)
    Button(functions, text=b, width=11, command=cmd).grid(row=r, column=c)
    r = r+1

### Run mainloop
window.mainloop()

