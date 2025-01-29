from random import choice
from os import listdir

import tkinter as tk
import tkinter.ttk as ttk

from game import Game


class Card(ttk.Checkbutton):
    IMAGE_DIR_NAME = "./images"
    selected_cards = []

    def __init__(self, parent):
        super().__init__(parent)
        # Instance variables
        self.cards = parent.cards
        self.points = parent.points
        self.status = tk.BooleanVar()
        self.name = tk.StringVar()
        # Card configs
        self["command"] = self.on_click
        self["variable"] = self.status

        # Choice random image for the card
        self.choice_random_image()
        self.game = Game()

    def on_click(self):
        selected_cards = self.selected_cards()

        if len(selected_cards) == 3:
            self.game.decide_score(selected_cards)
            total = self.points.get() + self.game.score
            self.points.set(total)

    def choice_random_image(self):
        # set a random image for the card
        image_name = choice(listdir(Card.IMAGE_DIR_NAME))
        photo = tk.PhotoImage(file=f"./images/{image_name}")
        self.image = photo
        self["image"] = self.image
        self.name.set(image_name)

    def selected_cards(self):
        return [card for card in self.cards if card.status.get()]
