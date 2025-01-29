import pickle

import os

import sqlite3





class Phonebook:
    def __init__(self, database='contacts.db'):
        try:
            with sqlite3.connect('contacts.db') as db:
                self.conn = sqlite3.connect(database)
                self.cursor = self.conn.cursor()
                self.cursor.execute("""CREATE TABLE contact (
                	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                	"first_name"	TEXT NOT NULL,
                	"last_name"	TEXT NOT NULL,
                	"phone"	NUMERIC NOT NULL
                )""")
        except Exception as e:
            print(e)



    def add(self, first, last, phone):
        contact = {'x': first, 'y': last, 'z': phone}
        sql_cmd = "INSERT INTO contact(first_name, last_name, phone) VALUES (:x, :y, :z)"
        try:
            with self.conn:
                self.cursor.execute(sql_cmd, contact)
        except Exception as e:
            return e

        return True
    
    def _search(self, first, last):
        with self.conn:
            find_obj = {'x':first, 'y':last}
            sql_cmd = "SELECT * FROM contact WHERE first_name = :x AND last_name= :y"
            self.cursor.execute(sql_cmd, find_obj)
            data = self.cursor.fetchall()
            if len(data) > 0:
                return data

            return False

    def find(self):
        first = input('First Name: ').lower()
        last = input('Last Name: ').lower()
        data = self._search(first, last)
        if data:
            print('\nContact info is: \nname: {} {} \nphone: {}'.format(data[0][1], data[0][2], data[0][3]))
        else:
            print("The given contact does not exist use 5 to display the contacts")

    def edit(self):
        first = input('First Name: ').lower()
        last = input('Last Name: ').lower()

        with self.conn:
            if self._search(first, last):
                new_phone = input('New Phone: ')
                sql_cmd = "UPDATE contact SET phone = :x WHERE first_name = :y AND last_name= :z"
                edit_obj = {'x':new_phone, 'y':first, 'z':last}
                self.cursor.execute(sql_cmd, edit_obj)
                print('Contact is updated successfuly.')
            else:
                print('Contact not found press 5 to see all contacts.')

    def delete(self):
        first = input('First Name: ').lower()
        last = input('Last Name: ').lower()
        with self.conn:
            if self._search(first, last):
                sql_cmd = "DELETE from contact WHERE first_name = :x AND last_name = :y"
                del_obj = {'x': first, 'y': last}
                self.cursor.execute(sql_cmd, del_obj)
                print('Contact is successfuly deleted!!')
            else:
                print("The contact does not exist use 5 to display the contacts")

    def _get_contacts(self):
        sql_cmd = "SELECT first_name, last_name, phone FROM contact;"

        with self.conn:
            data = self.cursor.execute(sql_cmd).fetchall()
        return data




myphonebook = Phonebook()


   

