# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *

class MyButtons:
	def __init__(self, rootone):
		frame = Frame(rootone)
		frame.pack()

		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack()

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("Hello There!!")
	
root = Tk()

b = MyButtons(root)

root.mainloop()

