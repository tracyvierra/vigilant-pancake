# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *


root = Tk()		

label1 = Label(root, text="First Name", bg="Red", fg="White")			# Create a label widget
label1.pack(fill=X)								# Pack the label widget

label2 = Label(root, text="Last Name", bg="Blue", fg="Green")			# Create another label widget
label2.pack(side=LEFT,fill=Y)							# Pack the label widget

root.mainloop()								# Start the main loop

