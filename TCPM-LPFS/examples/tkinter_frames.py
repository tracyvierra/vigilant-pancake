# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *


root = Tk()

newframe = Frame(root)			# Create a frame widget
newframe.pack()				# Pack it into the window

otherframe = Frame(root)			# Create another frame widget
otherframe.pack(side=BOTTOM)			# Pack it into the window

button1 = Button(newframe, text="Click Here!", fg="Red")		# Create a button widget
button2 = Button(otherframe, text="Or Here!", fg="Blue")		# Create another button widget

button1.pack()					# Pack it into the window
button2.pack(side=RIGHT)			# Pack it into the window


root.mainloop()

