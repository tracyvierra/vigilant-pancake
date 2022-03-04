# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *

def function1():
	print("You created a new project.")

def function2():
	print("You have saved the project.")

def function3():
	print("Last command has been undone.")

root = Tk()

myMenu = Menu(root)	
root.config(menu=myMenu)

subMenu = Menu(myMenu)

myMenu.add_cascade(label="File", menu=subMenu)			

subMenu.add_command(label="New Project...", command=function1)		
subMenu.add_command(label="Save", command=function2)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=function3)


root.mainloop()

