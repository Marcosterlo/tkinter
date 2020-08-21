from tkinter import *
from PIL import ImageTk, Image

global index
index=0

root = Tk()
root.title("Icons and Images on Tkinter")
#root.iconbitmap('@/home/marco/operative/tkinter/icon.xbm') #.xbm in Ubunutu and .ico on Windows

img1 = ImageTk.PhotoImage(Image.open("images/num4.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/num5.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/num1.png"))
img4 = ImageTk.PhotoImage(Image.open("images/num2.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/num3.jpg"))

image_list = [img1, img2, img3, img4, img5]

#Images can be added to almost every widget

def back():
    global index
    global lab
    if index>0:
        index-=1
        lab.grid_forget()
        lab = Label(image=image_list[index])
        lab.grid(row=0, column=0, columnspan=3)
        if index == 0:
            butt_back = Button(root, text="<<", command=back, state=DISABLED)
            butt_forw = Button(root, text=">>", command=forward, state=ACTIVE)
        else:
            butt_back = Button(root, text="<<", command=back, state=ACTIVE)
            butt_forw = Button(root, text=">>", command=forward, state=ACTIVE)
        butt_back.grid(row=1, column=0)
        butt_forw.grid(row=1, column=2)
        status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    return

def forward():
    global index
    global lab
    if index<4:
        index+=1
        lab.grid_forget()
        lab = Label(image=image_list[index])
        lab.grid(row=0, column=0, columnspan=3)
    if index == 4:
        butt_back = Button(root, text="<<", command=back, state=ACTIVE)
        butt_forw = Button(root, text=">>", command=forward, state=DISABLED)
    else:
        butt_back = Button(root, text="<<", command=back, state=ACTIVE)
        butt_forw = Button(root, text=">>", command=forward, state=ACTIVE)
    butt_back.grid(row=1, column=0)
    butt_forw.grid(row=1, column=2)
    status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    return

lab = Label(image=image_list[index])
butt_back = Button(root, text="<<", command=back, state=DISABLED)
butt_forw = Button(root, text=">>", command=forward, state=ACTIVE)
status = Label(root, text="Image " + str(index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

lab.grid(row=0, column=0, columnspan=3)
butt_back.grid(row=1, column=0)
butt_forw.grid(row=1, column=2)

butt_quit = Button(root, text="Exit", command=root.quit)
butt_quit.grid(row=1, column=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#Root window loop
root.mainloop()