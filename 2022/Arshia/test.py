import tkinter as tk
from tkinter import ttk


def on_press():
    print(checkbutton)


root = tk.Tk()
photo = tk.PhotoImage(file="./images/1 symbol1 of blue  filled.png")
checkbutton = tk.Checkbutton(root, image=photo, indicatoron=False, command=on_press)
checkbutton.pack()
root.mainloop()
