import sys
import api

from PyQt5.QtWidgets import *


class Register(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout(self)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password_conf = QLineEdit()
        self.register = QPushButton('Register')
        self.error_message = QLabel()
        

        self.init_ui()

    def init_ui(self):
        self.layout.addRow(QLabel('Username'), self.username)
        self.layout.addRow(QLabel('Password'), self.password)
        self.layout.addRow(QLabel('Password Confirm'), self.password_conf)
        self.layout.addRow(self.register)

        self.register.clicked.connect(self.register_handler)
        
        self.show()

    def register_handler(self):
        username = self.username.text()
        password = self.password.text()

        r = api.add_user(username, password)
        print(r, r.content)

        if api.check_status('POST', r):
            print('registerd successfuly.')
            QMessageBox.about(self, 'Add User', 'User added successfuly.')
        else:   # some problem occured in user adding
            self.error_message.setText(str(r))


    def check_password(password):
        # applying opertions.
        pass


class User(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.table_widget = QTableWidget()
        self.error_message = QLabel()
        self.update = QPushButton('Update')
        self.delete = QPushButton('Delete')
        self.update_form = QWidget()

        self.init_ui()

    def init_ui(self):
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.update)
        self.layout.addWidget(self.delete)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Username', 'Password'])
        self.fill_table()

        self.update.clicked.connect(self.update_handler)
        self.show()

    def fill_table(self):
        row = 0

        r = api.get_users()
        if api.check_status('GET', r):
            users = r.json()
            self.table_widget.setRowCount(len(users))
            for user in users:
                self.table_widget.setItem(row, 0, QTableWidgetItem(f'{user.get("username")}'))
                self.table_widget.setItem(row, 1, QTableWidgetItem(f'{user.get("password")}'))
                row += 1
        else:
            self.error_message.setText(f'{r.status_code} Error')
            self.layout.addWidget(self.error_message)

    def update_handler(self):
        pass_column = 1
        self.curr_username = self.table_widget.currentItem() .text()
        pass_row = self.table_widget.currentRow()
        self.curr_pass = self.table_widget.item(pass_row, pass_column).text()

        lay = QFormLayout(self.update_form)
        self.update_username = QLineEdit()
        self.update_pass = QLineEdit()
        update_button = QPushButton('Update')   
        lay.addRow(QLabel('Username: '), self.update_username)
        lay.addRow(QLabel('Password'), self.update_pass)
        lay.addRow(update_button)

        self.update_username.setText(self.curr_username)
        self.update_pass.setText(self.curr_pass)
        update_button.clicked.connect(self.update_on_server_handler)
        self.update_form.show()
        self.setEnabled(False)

    def update_on_server_handler(self):
        user = self.update_username.text()
        password = self.update_pass.text()
        r = api.udpate_user2(self.curr_username, self.curr_pass, user, password)
        
        if api.check_status('PUT', r):
            QMessageBox.about(self.update_form, 'Update', 'User updated successfuly.')
            self.setEnabled(True)
            self.fill_table()
            self.update_form.destroy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = User()
    app.exec_()