from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

pizza = IntVar()
pizza.set(1)

MENU = [("Margherita", 1), ("Romana", 2), ("Diavola", 3), ("Pollo", 4)]

frame = LabelFrame(root, text="Pizza Menu", padx=10, pady=10).pack(padx=10, pady=10)

for text, id in MENU:
    Radiobutton(frame, text=text, variable=pizza, value=id).pack(anchor=W)

b = Button(frame, text="Submit", command=lambda: Label(root, text=pizza.get()).pack()).pack()

root.mainloop()