# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *


root = Tk()

label1 = Label(root, text="First Name")			# Create a label widget
label2 = Label(root, text="Last Name")			# Create another label widget

entry1 = Entry(root)					# Create an entry widget
entry2 = Entry(root)					# Create another entry widget

label1.grid(row=0, column=0)				# Grid it into the window
label2.grid(row=1, column=0)				# Grid it into the window

entry1.grid(row=0, column=1)				# Grid it into the window
entry2.grid(row=1, column=1)				# Grid it into the window



root.mainloop()

