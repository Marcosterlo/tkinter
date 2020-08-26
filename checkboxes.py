#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Checkboxes")
root.geometry("500x500")

var = StringVar() #value to assign to checkbox

def show():
    Label(root, text=var.get()).pack()

#Checkbox
c = Checkbutton(root, text="Check", variable=var, onvalue="Suchegno", offvalue="SUCONE")
c.deselect()
c.pack()

Button(root, text="Show val", command=show).pack()

root.mainloop()