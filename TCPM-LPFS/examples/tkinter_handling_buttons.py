# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *


root = Tk()

def dosomething():
	print("Hello!")

button1 = Button(root, text="Click Me!", command=dosomething)		# Create a button widget, command=function will call function when button is clicked
button1.pack()							# Pack the button widget

root.mainloop()

