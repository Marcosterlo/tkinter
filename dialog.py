
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("File Dialog")
root.geometry("400x400")

second = Toplevel()
second.title("Second Window")

def resize(i):
    second.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

def resize_self():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=400, to=1000, command=resize)
vertical.pack()
horizontal = Scale(root, from_=400, to=1000, orient=HORIZONTAL, command=resize)
horizontal.pack()

def get_slider():
    Label(root, text="Vertical = " + str(vertical.get()) + "\nHorizontal = " + str(horizontal.get())).pack()

def open():
    global img
    suca = filedialog.askopenfilename(initialdir="/home/marco/operative/tkinter/images", title="Select a file", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    lbl = Label(root, text=suca).pack() #root.filename return the directory of the file
    img = ImageTk.PhotoImage(Image.open(suca))
    Label(root, image=img).pack()

btn = Button(root, text="Get slider values", command=get_slider).pack()
btn2 = Button(root, text="Resize", command=resize_self).pack()
#btn3 = Button(root, text="Open file", command=open).pack()


root.mainloop()