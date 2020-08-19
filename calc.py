from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(i):
   e.delete(0, END)
   e.insert(0, i)
   return

butt_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
butt_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
butt_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
butt_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
butt_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
butt_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
butt_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
butt_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
butt_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
butt_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
butt_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_click())
butt_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click())
butt_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: e.delete(0, END))
sucone = Button(root, text="sucone", padx=120, pady=20, command=lambda: button_click("sucone"))
sucone.grid(row=6, column=0, columnspan=3)

butt_1.grid(row=3, column=0)
butt_2.grid(row=3, column=1)
butt_3.grid(row=3, column=2)

butt_4.grid(row=2, column=0)
butt_5.grid(row=2, column=1)
butt_6.grid(row=2, column=2)

butt_7.grid(row=1, column=0)
butt_8.grid(row=1, column=1)
butt_9.grid(row=1, column=2)

butt_0.grid(row=4, column=0)
butt_add.grid(row=5, column=0)
butt_equal.grid(row=5, column=1, columnspan=2)
butt_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()