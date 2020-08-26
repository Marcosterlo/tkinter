#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Drop Down Menu")
root.geometry("500x500")

Options = []

for i in range(20):
    Options.insert(i, "Option #" + str(i+1))

clicked = StringVar()
clicked.set(Options[0])

def show():
    Label(root, text=clicked.get()).pack()

drop = OptionMenu(root, clicked, *Options).pack() #in this case clicked is the variable assigned to the Option Menu

Button(root, text="Show Variable", command=show).pack()

root.mainloop()