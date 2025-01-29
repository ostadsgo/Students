

import pickle
import os


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phonebook:
    def __init__(self, database='contacts.pickle'):
        self.database = database
        self.persons = {}

        if os.path.exists(self.database):
            with open(self.database, 'rb') as f:
                self.persons = pickle.load(f)
        else:
            f = open(self.database, 'wb')
            pickle.dump({}, f)
            f.close()
    




    def edit(self):
        name = input('Name to update: ')
        if name in self.persons:
            new_phone = input('New Phone')
            self.persons[name].phone = new_phone
        else:
            print('Contact not found')

    def display(self):
        for item in self.persons:
            print(item, self.persons[item].phone)

    def delete(self):
        name = input('name to delete: ')
        if name in self.persons:
            del self.persons[name]
        else:
            print('contact not found')

    
    def find(self):
        name = input('Name to find: ')

        if name in self.persons:
            print(self.persons[name].phone)
        else:
            print('contact not found')


    def exit(self):
        with open(self.database, 'wb') as f:
            pickle.dump(self.persons, f)
        exit()
