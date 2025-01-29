import os
from random import choice
import tkinter as tk
from tkinter import ttk

from card import Card


class CardFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.points = 0
        self.cards = []

    def generate_cards(self, number=6):
        # card images
        for i in range(number):
            card = Card(self)
            card.pack(side=tk.LEFT, padx=20, pady=10)
            self.cards.append(card)

    def set_points(self, points):
        self.points = points
        print(self.points, points)


class BottomFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.points = tk.IntVar()
        self.points.set(0)
        opt = {"side": tk.LEFT, "padx": (5, 20)}
        ttk.Button(self, text="Hands out", command=self.hands_out).pack(**opt)
        ttk.Label(self, text="Total Points: ").pack(**opt)
        ttk.Label(self, textvariable=self.points).pack(**opt)

    def hands_out(self):
        print("hands out")


class MainFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self["borderwidth"] = 2
        self["relief"] = "sunken"
        self["padding"] = 5

        # Bottom area for information and hands outing
        bottom_frame = BottomFrame(self)
        bottom_frame.grid(row=1, column=0, sticky="snwe")

        # Frame for holding all
        cards_frame = CardFrame(self)
        cards_frame.grid(row=0, column=0, sticky="snwe")
        cards_frame.points = bottom_frame.points
        cards_frame.generate_cards()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Card Game")
        mainframe = MainFrame()
        mainframe.grid(row=0, column=0, sticky="snwe")
        mainframe.rowconfigure(0, weight=9)  # the row contains cards
        mainframe.rowconfigure(1, weight=1)  # the row contains buttons


app = MainWindow()  # runs from here
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
app.mainloop()
