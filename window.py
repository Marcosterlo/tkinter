from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("New Window")


def open():
    global img #I need to put the image variable global in order to let python not put it in the trash (?)
    top = Toplevel() #tkinter wants not to call another Tk() function, we use instead TopLevel
    top.title("Second Window")
    img = ImageTk.PhotoImage(Image.open("images/num4.jpg"))
    lbl = Label(top, image=img).pack()
    Button(top, text="Close window", command=top.destroy).pack() #destroy eliminates the widget

btn = Button(root, text="Open second windows", command=open).pack()

root.mainloop()