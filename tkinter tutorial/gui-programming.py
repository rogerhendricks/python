import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        
        def clickMe():
            action.configure(text="hello" + name.get())
            
        


if name == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()