# FIX: 
# after loginning main window displayed but then after closing it programmed didn't end. 

import sys
import api
import os

from PyQt5.uic import loadUiType
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from ui import res_rc 


BASE_DIR = os.path.dirname(__file__)
UI_PATH = os.path.join(BASE_DIR, 'ui')

class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(UI_PATH, 'login.ui'), self)
        self.login_button.clicked.connect(self.login_handler)
        self.show() 

    def login_handler(self):
        self.error_message.setText('')
        r = api.admin_auth(self.username.text(), self.password.text())
        if r.get('result') == 'ok':
            print('correct creditionals')
            self.main = MainWindow()
            self.destroy()

        else:  # Error
            message = f'{r.get("result").title()} {r.get("status_code")}: {r.get("message")}'
            self.error_message.setText(message)



class UsersManagment(QDialog):
    def __init__(self):
        super().__init__()
        
    def load_users(self, table_widget):
        header = table_widget.horizontalHeader()       
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        row = 0
        r = api.get_users()
        if api.check_status('GET', r):
            users = r.json()
            table_widget.setRowCount(len(users))
            
            for user in users:
                btn = QPushButton('Edit')
                table_widget.setItem(row, 0, QTableWidgetItem(f'{user.get("username")}'))
                table_widget.setItem(row, 1, QTableWidgetItem(f'{user.get("password")}'))
                table_widget.setCellWidget(row, 2, btn)
                row += 1
        else:
            # self.error_message.setText(f'{r.status_code} Error')
            # self.layout.addWidget(self.error_message)
            print(r.status_code)

    def new_user_form(self):
        self.new_user_ui = loadUi(os.path.join(UI_PATH, 'register.ui'), self)
        self.new_user_ui.show()

        self.new_user_ui.register_button.clicked.connect(self.add_user)

    def add_user(self):
        username = self.new_user_ui.username.text()
        password = self.new_user_ui.password.text()
        pass_conf = self.new_user_ui.password_confirm.text()
        if password == pass_conf:
            r = api.add_user(username, password)
            if api.check_status('POST', r):
                self.error_message.setStyleSheet('color: #00ff00')
                self.error_message.setText(f'{r.status_code} User Successfuly Added.')
                self.new_user_ui.username.setText('')
                self.new_user_ui.password.setText('')
                self.new_user_ui.password_confirm.setText('')
            else:
                self.error_message.setText(str(r))
        else:
            self.error_message.setText('Wrong password!')


class MainWindow(QMainWindow):
    
    def __init__(self):
        print('in main')
        super().__init__()
        self.pages_number = {'users': 0, 'profiles': 1, 'payments': 2, 'send_email': 3, 'help': 4 }
        self.main_ui = loadUi(os.path.join(UI_PATH, 'main.ui'), self)
        # self.load_users()
        
        self.main_ui.users.clicked.connect(self.display_users_page)
        self.main_ui.profiles.clicked.connect(self.display_profiles_page)
        self.main_ui.payments.clicked.connect(self.display_payments_page)
        self.main_ui.send_email.clicked.connect(self.display_send_email_page)
        self.main_ui.help.clicked.connect(self.display_help_page)
        self.main_ui.new_user.clicked.connect(self.display_add_user_form)
        self.main_ui.show()

    def display_users_page(self):
        self.pages.setCurrentIndex(self.pages_number.get('users'))
        users = UsersManagment()
        users.load_users(self.main_ui.table_widget)
        print('after load users')

    def display_profiles_page(self):
        self.pages.setCurrentIndex(self.pages_number.get('profiles'))

    def display_payments_page(self):
        self.pages.setCurrentIndex(self.pages_number.get('payments'))

    def display_send_email_page(self):
        self.pages.setCurrentIndex(self.pages_number.get('send_email'))

    def display_help_page(self):
        self.pages.setCurrentIndex(self.pages_number.get('help'))

    def display_add_user_form(self):
        um = UsersManagment()
        um.new_user_form()  # load a register.ui 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # login = LoginForm()
    main = MainWindow()
    #u = AddUser()
    sys.exit(app.exec_())
