from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames, radio buttons")

frame = LabelFrame(root, text="This is my frame", padx=5, pady=5) #The pad in the frame definitionpds the inside
frame.pack(padx=10, pady=10) #The pad on the pack call pads the outside of the frame

#tkinter variables, are different from python variables
r = IntVar()
r.set(2)

def clicked(value):
    mylab = Label(root, text=value).pack()


#Radiobutton(frame, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack() #We can even create Radio Buttons via iteration
#Radiobutton(frame, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#b = Button(frame, text="Click me", command=lambda: clicked(r.get())).pack()

mylab = Label(root, text=r.get()).pack()

#b = Button(frame, text="Click me")
#b2 = Button(frame, text="Click me")
#b.grid(row=0, column=0) #You can either pack a frame and then grid object inside the frame
#b2.grid(row=1, column=1)


root.mainloop()