from enum import Enum
from dataclasses import dataclass
import logging

logging.basicConfig(filename="products_app.log")


class Menu(Enum):
    add = "add"
    show = "show"
    help = "help"
    remove = "remove"
    search = "search"
    clear = "clear"
    sort_asc = "sort asc"
    sort_desc = "sort desc"


@dataclass
class Product:
    name: str
    price: int

    def write(self):
        try:
            with open("products.txt", "a") as f:
                f.write(self.name + ":" + str(self.price))
        except FileNotFoundError:
            logging.error("products.txt not found!")


def add(name, price):
    product = Product(name, price)
    product.write()


while True:
    # get input:
    print("Options are:")
    items = ""
    for i in Menu:
        items += i.value + ", "
    print(items)
    print()
    item = input("Choose form options: ")
    if item in ["q", "quit"]:
        pass
    elif item == Menu.add.value:
        name = input("Enter product name: ")
        price = input("Enter price of the product: ")
        add(name, price)
    elif item == Menu.show.value:
        pass
    elif item == Menu.help.value:
        pass
    elif item == Menu.remove.value:
        pass
    elif item == Menu.search.value:
        pass
    elif item == Menu.clear.value:
        pass
    elif item == Menu.sort_asc.value:
        pass
    elif item == Menu.sort_desc.value:
        pass
    else:
        pass

    print(item)
