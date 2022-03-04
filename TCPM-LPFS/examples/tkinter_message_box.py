# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("Window Title", "This is a message box!")	# showinfo() displays a message box with a title and a message

response = tkinter.messagebox.askquestion("Question 1", "Do you like this program?")	# askquestion() displays a message box with a title and a message and returns a string
if response == "yes":
	print("Great!")
else:
	print("Too bad!")


root.mainloop()

