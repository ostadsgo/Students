import os
import logging

logging.basicConfig(filename="example.log")

# project shopping list:
print("*******SHOPPING_LIST*******")

# exit:
EXIT_COMMANDS = ["q", "quit", "ex", "exit"]
shopping_list = []


f = open("fruit.txt", "w")
f.write(
    "apple:55\n orange:70\n banana:100\n grape:60\n watermelon:80\n peach:30\n cucumber:25"
)
f.close()

# open and read the file after the appending:
f = open("fruit.txt", "r")
item = f.readline()

while item:
    item = f.readline()
f.close()


f = open("market.txt", "w")
f.write("jam:60\n chess:45\n milk:30\n butter:15\n pasta:40\n sauce:15\n chocolate:50")
f.close()

# open and read the file after the appending:
f = open("market.txt", "r")
print(f.read())

f = open("vegetables.txt", "w")
f.write(
    "cabbage:15\n lettuce:20\n broccoli:75\n peas:35\n green beans:65\n parsley:25\n mint:10"
)
while item:
    item = f.readline()
f.close()

# open and read the file after the appending:
f = open("vegetables.txt", "r")
print(f.read())
# add function in list:
def add_item(list, item):
    """


    Parameters
    ----------
    list :add list in shopping_list

    item :add item in shopping_list


    Returns item get in list
    -------

    """
    list.append(item)
    return list
    show_help(list)


# show function in list:
def show_help(list):
    """
    Parameters
    ----------
    list : show in list


    Returns show list will return
    -------

    """
    for item in list:
        print(item)


# remove function in list:
def remove_item(list, item):
    """

    Parameters
    ----------
    list : remove in list

    item : remove in item


    Returns remove item will return list
    -------

    """
    if item not in list:
        print("item that you are trying to remove is not in the list")
    else:
        list.remove(item)


# search function in list:
def search_item(list, item):
    """

    Parameters
    ----------
    list : search in list

    item : search in item


    Returns search item in list will return
    -------

    """
    if item in list:
        print("yes, " + str(item) + " is in list.")
    else:
        print("no, " + str(item) + " is not in list")
    return list


# beautify function in list:
def beautify_list(list):
    """

    Parameters
    ----------
    list : beautify item in list


    Returns beautify will return in list
    -------

    """
    for item in list:
        print(f">{item}")


# show function in list:
def show_help():
    """ """
    print("enter,`QUIT` to exit the app and see your list")
    print("enter `HELP` to see help")


# sort function in list asc:
def sort_list_ascending(list):
    """

    Parameters
    ----------
    list : sort in list asc


    Returns sort in list will return
    -------

    """
    print(sorted(list))


# sort function in list des:
def sort_list_descending(list):
    """

    Parameters
    ----------
    list : sort in list desc


    Returns  sort in list will return
    -------

    """
    print(sorted(list, reverse=True))


# clear screen function in list:
def clear_screen():
    """ """
    return os.system("CLS")

    # multi function:
    """

    Parameters
    ----------
    list : 3 list whit multiply
        

    Returns 3 list whit multiply will return
    -------

    """


# sum function:
def sum_list(list):
    """

    Parameters
    ----------
    list :3 list whit sum


    Returns 3 list with sum will return
    -------

    """


# infinite loop:
while True:
    # get input:
    item = input("please enter item that you want to add:")
    if item in EXIT_COMMANDS:
        beautify_list(shopping_list)
        break
    elif item == "show":
        beautify_list(shopping_list)
    elif item == "help":
        show_help()
    elif item == "remove":
        item_to_remove = input("please enter the item that you want to remove:")
        remove_item(shopping_list, item_to_remove)
    elif item == "search":
        item_to_search = input("please enter the item that you want to search:")
        search_item(shopping_list, item_to_search)
    elif item == "clear":
        clear_screen()
    elif item == "sort asc":
        sort_list_ascending(shopping_list)
    elif item == "sort desc":
        sort_list_descending(shopping_list)
    elif item == "add":
        if item in shopping_list:
            print(input("item is already in your list"))
        else:
            add_item(shopping_list, item)
            print(
                f"{item} add to your list and there are {len(shopping_list)} items in your list"
            )
    else:
        print("wrong option\n options are ['show', 'add', 'clear']")
        logging.error("User choosed wrong option", item)
