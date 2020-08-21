from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message boxes")

#Different types of mesage boxes:
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel
#showinfo --> ok="ok"
#showwarning --> ok="ok"
#showerror --> ok="ok"
#askyesno --> yes=1, no=0,
#askokcancel --> ok=1, cancel=0
#askquestion --> yes="yes", no="no"
#askyesnocancel --> yes=1, no=0, cancel=

def popup():
    response = messagebox.showerror("This is my popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    elif response == 0:
        Label(root, text="You clicked no!"). pack()
    elif response == " ":
        Label(root, text="You cancelled!").pack()

Button(root, text="Popup", comman=popup).pack()


root.mainloop()