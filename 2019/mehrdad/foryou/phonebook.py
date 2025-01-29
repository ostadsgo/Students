import pickle
import os
import sqlite3


class Phonebook:
    def __init__(self, database='contacts.db'):
        try:
            with sqlite3.connect('contacts.db') as db:
                self.conn = sqlite3.connect(database)
                self.cursor = self.conn.cursor()

        except Exception as e:
            print(e)
        
    def add(self):
        first_name, last_name = input('Name: ').split(' ')
        phone = input('Phone: ')
        contact = {'x': first_name, 'y': last_name, 'z': phone}
        sql_cmd = "INSERT INTO contact(first_name, last_name, phone) VALUES (:x, :y, :z)"
        with self.conn:
            self.cursor.execute(sql_cmd, contact)
        print('Contact added successfuly.')


    def edit(self):pass
    def delete(self):pass
    def display(self):
        sql_cmd = "SELECT first_name, last_name, phone FROM contact;"
        with self.conn:
            data = self.cursor.execute(sql_cmd).fetchall()
            
        for fn, ln, ph in data:
            print(fn + ' ' + ln, ':', ph)

    def find(self):pass