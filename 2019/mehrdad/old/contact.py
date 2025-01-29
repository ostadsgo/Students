import pickle


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Contact:
    def display_menu(self):
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

    def write_back(self, lines):
        with open('contacts.txt', 'w') as f:
            f.write(''.join(lines))

    def append_contact(self, obj):
        
        with open("contacts.pickle", "ab") as f:
            # f.write(f"{contact_id}:{p.name}:{p.phone}\n")
            pickle.dump(obj, f)
    
    def get_max_id(self):
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

    def add_contact(self):
        """ Get name and phone and store it as a contact """

        # max_id = self.get_max_id() + 1
        name = input("Name: ")
        phone = input("Phone: ")
        p = Person(name=name, phone=phone)
        self.append_contact(p)

    
    def edit_contact(self):
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
        self.write_back(lines)
    
    def delete_contact(self):
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
        self.write_back(lines)

    def find_contact(self):
        correctname = input("Plese Enter contact name: ")
        with open("contacts.txt", "r") as f1:
            lines = f1.readlines()
            for line in lines:
                if correctname in line:
                    object = line.split(":")[-1]
                    print("The phone number of '{}' is '{}' ".format(correctname, object))
            else:
                print("Contact Not Found!")

    def display_contact(self):
        with open("contacts.pickle", "rb") as f:
            while True:
                line = pickle.load(f)
                print(line)

            # print(data1.name, data1.phone)
            # print(data2.name, data2.phone)


personal = Contact('personal.pickle')
firends = Contact('firends.pickle')


