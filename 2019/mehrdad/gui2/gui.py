import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import placeholder as plc
from phonebook import myphonebook


class Contact:
    
    def _delete_tree_item(self, tree, item=None):
        # delete all contacts
        if item is None:
            for row in tree.get_children():
                print(row)
                tree.delete(row)
        # delete an indevidual item of tree
        else:
            pass

    def fill_table(self, tree):
        data = myphonebook._get_contacts()
        # delete all contacts before refill it
        self._delete_tree_item(tree)

        for item in enumerate(data):
            tree.insert('', 'end', iid=item[0], values=item[1])
        
    def add_contact(self, fn, ln, ph, tree=None):
        result = myphonebook.add(fn.get(), ln.get(), ph.get())
        if result:
            messagebox.showinfo('Add Contact', 'Contact added successfuly')
            fn.delete(0, 'end')
            ln.delete(0, 'end')
            ph.delete(0, 'end')
            self.fill_table(tree)
        else:
            messagebox.showwarning('Error', f'This problem happend: {result}')
    
    def update_contact(self, event=None, **kw):
        print(kw)
        data = kw.get('data')
        entries = kw.get('entries')
        entries.get('first').insert(0, data.get('first_name'))
        entries.get('last').insert(0, data.get('last_name'))
        entries.get('phone').insert(0, data.get('phone'))


class ContactApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.action = Contact()
        self.style = ttk.Style(self)
        self.style.configure('mainframe.TFrame', background='#D9D9D9')
        self.title('Contact App')
        # self.geometry(f'600x500+500+150')

        self.mainframe = ttk.Frame(self, style='mainframe.TFrame')
        self.mainframe.pack(fill='both', expand=True)

        # Frames
        self.search_frame = ttk.Frame(self.mainframe, relief='solid', padding=(10, 5))
        self.center_frame = ttk.Frame(self.mainframe, relief='solid', padding=10)
        self.action_frame = ttk.Frame(self.mainframe, relief='solid', padding=10)
        self.search_frame.pack(expand=1)
        self.center_frame.pack(fill='both')
        self.action_frame.pack(fill='x')

        self.search_box = ttk.Entry(self.search_frame, width=50)
        plc.placeholder(self.search_box, 'Search ... ')
        self.search_button = ttk.Button(self.search_frame, text='Search')
        self.search_box.pack(side='left')
        self.search_button.pack(side='left', padx=10)

        # Center Frame (contact_table)

        self.contact_table = ttk.Treeview(self.center_frame)
        self.contact_table.pack()
        self.contact_table['columns'] = ('first_name', 'last_name', 'phone_number')
        self.contact_table.heading('first_name', text='First Name')
        self.contact_table.heading('last_name', text='Last Name')
        self.contact_table.heading('phone_number', text='Phoen Number')
        self.contact_table['show'] = 'headings'

        # action frame
        add_button = ttk.Button(self.action_frame, text='Add', command=self.add_contact_form)
        edit_button = ttk.Button(self.action_frame, text='Edit', command=self.update_contact_form)
        delete_button = ttk.Button(self.action_frame, text='Delete')
        close = ttk.Button(self.action_frame, text='Close', command=self.quit)
        add_button.pack(side='left')
        edit_button.pack(side='left')
        delete_button.pack(side='left')
        close.pack(side='left')

        for child in self.action_frame.winfo_children():
            child.pack_configure(padx=5)

        # display all contacts in contact_table
        self.action.fill_table(self.contact_table)


    def add_contact_form(self):
        add_form = tk.Toplevel(self)
        add_form.title('Add New Contat')
        first_name = ttk.Entry(add_form)
        last_name = ttk.Entry(add_form)
        phone_number = ttk.Entry(add_form)
        add_button = ttk.Button(add_form, 
                                text='Add New Contact', 
                                command=lambda: self.action.add_contact(first_name,
                                                                    last_name,
                                                                    phone_number, 
                                                                    self.contact_table))
        close_button = ttk.Button(add_form, text='close', command=add_form.destroy)
        first_name.pack()
        last_name.pack()
        phone_number.pack()
        add_button.pack()
        close_button.pack()

    def update_contact_form(self):
        update_form = tk.Toplevel(self)
        first_name = ttk.Entry(update_form)
        last_name = ttk.Entry(update_form)
        phone_number = ttk.Entry(update_form)
        update_button = ttk.Button(update_form, text='Edit')
        close_button = ttk.Button(update_form, text='close', command=update_form.destroy)

        first_name.pack()
        last_name.pack()
        phone_number.pack()
        update_button.pack()
        close_button.pack()

        # record which user clicked on 
        item_id = self.contact_table.selection()
        values = self.contact_table.item(item_id).get('values')
        data = {'first_name': values[0], 'last_name': values[1], 'phone': values[2]}
        entries = {'first': first_name, 'last': last_name, 'phone': phone_number}

        update_button.bind('<1>', lambda e: self.action.update_contact(data=data, entries=entries))




mycontact_app = ContactApp()
mycontact_app.mainloop()
