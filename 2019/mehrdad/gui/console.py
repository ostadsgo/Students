import phonebook

def add_contact_console(self):
    first = input('First Name: ').lower()
    last = input('Last Name: ').lower()
    phone = input('Phone: ')

def display(self):
    data = self.myphonebook._get_contacts()
    for fn, ln, ph in data:

        print(fn + ' ' + ln, ':', ph)
        
def update():
        first = input('First Name: ').lower()
        last = input('Last Name: ').lower()
