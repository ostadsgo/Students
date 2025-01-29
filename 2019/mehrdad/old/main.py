import os
import contact



obj = contact.Contact()

operations = {
    '1': obj.add_contact,
    '2': obj.edit_contact,
    '3': obj.delete_contact,
    '4': obj.find_contact,
    '5': obj.display_contact,
    '6': exit,
}
while True:
    os.system('clear')
    obj.display_menu()


    response = input('Choice from menu...\n> ')
    
    if operations.get(response) is not None:
        operations[response]()
    else:
        print('Wrong Choice')
    
    input('Press any key to back to menu ...')




