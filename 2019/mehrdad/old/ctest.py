contacts = []


def display_menu():
    menu_items = [
        "Add Contact",
        "Edit Contact",
        "Delete Contact",
        "Find Contact",
        "Display Contact",
        "Exit",
    ]

    for index, item in enumerate(menu_items):
        print(f"[{index+1}] {item}")


def write_back(lines):
    with open('contacts.txt', 'w') as f:
	    f.write(''.join(lines))

def append_contact(contact_id, name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{contact_id}:{name}:{phone}\n")


def get_max_id():
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 0:
                max_id = 0
            else:
                lastline = lines[-1]
                max_id = lastline.split(':')[0]
        return int(max_id)
    except FileNotFoundError as e:
        print("Contact.txt file not found we created it.", e)
        max_id = 0
    
    return max_id


def add_contact():
    """ Get name and phone and store it as a contact """

    max_id = get_max_id() + 1
    name = input("Name: ")
    phone = input("Phone: ")
    append_contact(max_id, name, phone)


def edit_contact():
    correctname = input("Plese Enter the name you want to change: ")
    with open("contacts.txt", "r") as f1:
        lines = f1.readlines()
        for line in lines:
            idx, name, phone = line.split(':')
            if name == correctname:
                index = lines.index(line)
                new_name = input('New Name?')
                r = ':'.join([idx, new_name, phone])
                lines[index] = r
                print('Updated!')
                break
        else:
            print('contact not found!')
    # write back
    write_back(lines)


def delete_contact():
    correctname = input("Plese Enter the name you want to delet: ")
    with open("contacts.txt", "r") as f1:
        lines = f1.readlines()
        
        for line in lines:
            _, name, _ = line.split(':')
            if name == correctname:
                index = lines.index(line)
                del lines[index]
                print('deleted!')
                break
        else:
            print('contact not found!')
            
    # write back
    write_back(lines)

def find_contact():
    correctname = input("Plese Enter contact name: ")
    with open("contacts.txt", "r") as f1:
        lines = f1.readlines()
        for line in lines:
            if correctname in line:
                object = line.split(":")[-1]
                print("The phone number of '{}' is '{}' ".format(correctname, object))
        else:
            print("Contact Not Found!")



def display_contact():
    with open("contacts.txt", "r") as f:
        print(f.read())


'''
if correctname in line:

                    newline = line.replace(line, "")

                    f2.write(newline)

                    print("Contact is successfuly deleted.")

                    break

            

            else:

                print("{} is not a valid contact".format(correctname))
                '''
                
                
'''
newcontent = []

        is_contact_found = False

        

        for line in lines:

            if correctname in line:

                empty = line.replace(line, '')

                newcontent.append(empty)

                print('Contact deleted!')

                is_contact_found = True

            else:

                newcontent.append(line)

                

        if not is_contact_found:

            print('Contact Not Found')
            '''
