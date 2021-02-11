# Topic - Entry/Input
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0) 
un=Entry(root,font=("Arial",20),fg="red",width="10") #Use to create Entry object, other attributes are same like fg, bg etc.
un.pack()
root.mainloop()
