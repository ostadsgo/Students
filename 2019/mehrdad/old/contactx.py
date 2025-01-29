contacts = []


def display_menu():
    menu_items = [
    'Add Contact',
    'Edit Contact',
    'Delete Contact',
    'Find Contact',
    'Display Contact',
    'Exit',
    ]

    for index, item in enumerate(menu_items):
        print(f'[{index+1}] {item}')

def append_contact(contact_id, name, phone):
    with open('contacts.txt', 'a') as f:
        f.write(f'{contact_id}:{name}:{phone}\n')

def get_max_id():
    try:
        with open('contacts.txt', 'r') as f:
            last_contact = f.readlines()[-1]
            max_id = last_contact.split(':')[0]
            
        return int(max_id)
    except FileNotFoundError as e:
        print('Contact.txt file not found we created it.', e)
        return 0


def add_contact():
    ''' Get name and phone and store it as a contact '''

    max_id = get_max_id() + 1
    name = input('Name: ')
    phone = input('Phone: ')
    append_contact(max_id, name, phone) 
 
    

def edit_contact():
    name = input('Name')
    for item in contacts:
        if item['name'] == name:
            new_phone = input('New Phone')
            item['phone'] = new_phone
            print('Contact updated successfuly.')
            break
    else:
        print('Contact Not Found!')


def delete_contact():
    name = input('Name')
    for index, item in enumerate(contacts):
        if item['name'] == name:
            del contacts[index]
            print('Contact Removed Successfuly.')
            break
    else:  # No break
        print('Not Found!')


def find_contact():
    name = input('Name')
    for item in contacts:
        if item['name'] == name:
            print(item['phone'])
            break
    else:
        print('Not Found')


def display_contact():
    with open('contacts.txt', 'r') as f:
        print(f.read())
