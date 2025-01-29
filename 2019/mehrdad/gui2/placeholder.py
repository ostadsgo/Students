# Kown Bug:
# with multipe widgets that's show last message.

# Question:

from tkinter import *
from tkinter import ttk


# the keys didn't remove placeholder when it exisit
# _no_keys = ("Tab", "Shift_L", "Control_L", "Control_L", "Return")
_traked_keys = (
	'1', '2', '3', '4', '5', '6', '7', '7', '8', '9', '0', 
	'minus', 'equal', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 
	'o', 'p', 'bracketleft', 'bracketright', 'backslash', 'a', 'grave',
	's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon', 'apostrophe', 
	'z', 'x', 'c', 'v', 'b', 'n', 'm', 'comma', 'period', 'slash', 'space', 
	'asciitilde', 'exclam', 'at', 'at', 'numbersign', 'dollar', 'percent', 
	'asciicircum', 'ampersand', 'asterisk', 'parenleft', 'parenright', 
	'underscore', 'plus', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 
	'P', 'braceleft', 'braceright', 'bar', 'A', 'S', 'D', 'F', 'G', 'H',
	'J', 'K', 'L', 'colon', 'quotedbl', 'Z', 'X', 'C', 'V', 'B', 'N', 
	'M', 'less', 'greater', 'question',  
)


# if somthing typed this function will be called.
def key_press(event):

	keysym = event.keysym
	keycode = event.keycode

	# if user type somthing when placeholder exist 
	# and user typed char in _traked_keys list:
	if event.widget.placeholder_exist and keysym in _traked_keys:
		event.widget.delete(0, END)  # delete placeholder
		event.widget.configure(foreground='black')  # text should be black
		# that's mean there isn't placeholder anymore.
		event.widget.placeholder_exist = False  

	elif event.widget.placeholder_exist and keysym in ["Delete", "BackSpace"]:
		return 'break'


# if there is a placeholder cursor should be move postion 0
def on_click(event):
	if event.widget.placeholder_exist:
		event.widget.icursor(0)  # cursor move to postion 0


# double click event handler
# if there is a placeholder double click should move cursor to pos 0
def on_double_click(event):

	if event.widget.placeholder_exist:
		event.widget.icursor(0)
		return 'break'


# clear highlighted color if there is a placeholder
def on_select(event):
	if event.widget.placeholder_exist:
		event.widget.icursor(0)
		event.widget.select_clear()


def on_remove(event):
	content_len = len(event.widget.get())

	# if there is a placeholder
	if event.widget.placeholder_exist:
		event.widget.icursor(0)  # move the cursor to position 0
		return 'break'  # don't run default event handler.

	# display placeholder message if nothing is inside of widget.
	elif content_len < 1:
		event.widget.delete(0, END)  # delete text of the widget
		# insert placeholder message
		event.widget.insert(0, event.widget.placeholder_message)  
		event.widget.icursor(0)  # move cursor to position 0
		event.widget.configure(foreground= "gray")
		event.widget.placeholder_exist = True


# Add placeholder to the widget.
def placeholder(widget=None, placeholder=''):

	placeholder = placeholder.strip()
	placeholder = ' ' + placeholder + ' '
	widget.insert(0, placeholder)  # insert the message to the widget
	widget.icursor(0)  # move the cursor to the first index
	widget.configure(foreground = "gray")  # make the text Gray
	
	widget.placeholder_message = placeholder  # save every widget message in itslef
	widget.placeholder_exist = True
	
	# creating custom event order
	# PostRemove and PostClick will be evaluvate after default event("TEntry")
	widget.bindtags(( str(widget), "TEntry", "PostEvent", ".", "all"))
	widget.bind_class("PostEvent", "<1>", on_click)
	widget.bind_class("PostEvent", "<BackSpace>", on_remove)
	widget.bind_class("PostEvent", "<Delete>", on_remove)
	widget.bind_class("PostEvent", "<ButtonPress-1><Motion>", on_select)
	widget.bind("<Double-Button-1>", on_double_click)
	widget.bind("<Key>", key_press)


ttk.Entry.placeholder = placeholder