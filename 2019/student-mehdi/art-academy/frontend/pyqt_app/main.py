import os
import sys
import api

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Login(QDialog):
	def __init__(self):
		super().__init__()
		self.title = 'Login'
		self.width = 720
		self.height = 480
		self.top = 200
		self.left = 400
		self.layout = QVBoxLayout(self)
		
		self.init_ui()


	def init_ui(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		# definitions
		self.message = QLabel()
		self.header = QLabel(f'<h4>Login to Art Academy</h4>')
		self.username = QLineEdit()
		self.password = QLineEdit()
		self.login_button = QPushButton('Login')
		
		# confings
		self.message.setObjectName('message')
		self.header.setObjectName('header')
		self.login_button.clicked.connect(self.login_handler)

		# add to layout
		self.layout.addWidget(self.header)
		self.layout.addWidget(QLabel('Username'))
		self.layout.addWidget(self.username)
		self.layout.addWidget(QLabel('Password'))
		self.layout.addWidget(self.password)
		self.layout.addWidget(self.login_button)
		self.layout.addWidget(self.message)
		self.show()

	def login_handler(self):
		username = self.username.text()
		password = self.password.text()

		response = api.admin_auth(username=username, password=password)
		if response.get('result') == 'ok':
			api.admin_username = username
			api.admin_password = password
			print('you logged in')
		else:
			self.message.setText('Error {}'.format(response))

if __name__ == '__main__':
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')

	app = QApplication(sys.argv)
	login = Login()
	login.setObjectName('login_form')

	with open(os.path.join(STATIC_ROOT, 'main.css'), 'r') as f:
		app.setStyleSheet(f.read())
	
	sys.exit(app.exec_())
