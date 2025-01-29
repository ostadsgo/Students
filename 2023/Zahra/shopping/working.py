from enum import Enum
from dataclasses import dataclass


class Menu(Enum):
    show = "show"
    help = "help"
    remove = "remove"
    search = "search"
    clear = "clear"


class Operation:
    def show_items(self):
        pass


# item = input("please enter item that you want to add:")

# if item == Menu.show:
#     show_item()


@dataclass
class ShoppingList:
    name: str
    price: int

    def write(self) -> float:
        print("Write to file....")


items = [("jam", 60), ("chess", 45), ("milk", 30)]

for item in items:
    name, price = item  # unpacking.


with open("file_working.py", "r") as f:
    c = f.read()
    print(c)
