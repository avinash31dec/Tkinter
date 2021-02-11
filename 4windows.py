# Topic - Label
from tkinter import *

root = Tk()
root.geometry("400x400") # Window can be resize in any direction.
root.resizable(0,0) # It will fix the window pannel.
#root.maxsize(300,300) # Max size is defined.
un = Label(root, text="Hello Avinash",font=("Arial",15))
un.pack()
root.mainloop()
