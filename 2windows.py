# Topic - Label
from tkinter import *

root = Tk()
root.minsize(300,300) # Min size is defined.
un = Label(root, text="Hello Avinash",font=("Arial",15))
un.pack()
root.mainloop() # Here window will be running in the loop so any statement will only run once window is closed.

