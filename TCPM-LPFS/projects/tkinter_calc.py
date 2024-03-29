# Author: Tracy Vierra
# Date Created: 3/4/2022
# Date Modified: 3/4/2022

# Description: A GUI calculator in Python and tkinter.

# Usage:


from tkinter import *
import math


root = Tk()
root.title("Calculator")

# get the user input and place it in the input box
i = 0
def get_variables(num):
	global i
	display.insert(i, num)
	i += 1

def clear_all():	
	display.delete(0, END)	

def del_char():
	length = len(display.get())	
	display.delete(length - 1)	

def get_operation(operator):
	global i
	length = len(display.get())
	display.insert(i, operator)
	i += length

def factorial():
	#calculate the factorial and return the result.
	num = display.get()
	# math.factorial(num)
	display.insert(i, math.factorial(int(num)))

def calculate():
	# calculate the result
	equation = display.get()
	# check if the equation has a solution
	try:
		answer = eval(equation)
		clear_all()
		display.insert(0, answer)
	except:
		clear_all()
		display.insert(0, "Error")
	
	


# adding the iput field
display = Entry(root)					# Create an Entry widget
display.grid(row=1, column=0, columnspan=6, sticky=W+E)	# Add it to the window

# adding the first row buttons


Button(root, text="1", command=lambda :get_variables(1), padx=5, pady=5).grid(row=2, column=0)
Button(root, text="2", command=lambda :get_variables(2), padx=5, pady=5).grid(row=2, column=1)
Button(root, text="3", command=lambda :get_variables(3), padx=5, pady=5).grid(row=2, column=2)


# adding the second row buttons


Button(root, text="4", command=lambda :get_variables(4), padx=5, pady=5).grid(row=3, column=0)
Button(root, text="5", command=lambda :get_variables(5), padx=5, pady=5).grid(row=3, column=1)
Button(root, text="6", command=lambda :get_variables(6), padx=5, pady=5).grid(row=3, column=2)


# adding the third row buttons


Button(root, text="7", command=lambda :get_variables(7), padx=5, pady=5).grid(row=4, column=0)
Button(root, text="8", command=lambda :get_variables(8), padx=5, pady=5).grid(row=4, column=1)
Button(root, text="9", command=lambda :get_variables(9), padx=5, pady=5).grid(row=4, column=2)

# adding other buttons 0, +, _, *, /, =, and clear

Button(root, text="AC", command=lambda :clear_all(), padx=4, pady=5).grid(row=5, column=0)
Button(root, text="0", command=lambda :get_variables(0), padx=5, pady=5).grid(row=5, column=1)
Button(root, text="=", command=lambda :calculate(), padx=5, pady=5).grid(row=5, column=2)

Button(root, text="+", command=lambda :get_operation("+"), padx=4, pady=5).grid(row=2, column=3)
Button(root, text="-", command=lambda :get_operation("-"),padx=5, pady=5).grid(row=3, column=3)
Button(root, text="*", command=lambda :get_operation("*"), padx=5, pady=5).grid(row=4, column=3)
Button(root, text="/", command=lambda :get_operation("/"), padx=5, pady=5).grid(row=5, column=3)

# adding other operators

Button(root, text="Pi", command=lambda :get_operation("* 3.14"), padx=5, pady=5).grid(row=2, column=4)
Button(root, text="%", command=lambda :get_operation("%"), padx=5, pady=5).grid(row=3, column=4)
Button(root, text="(", command=lambda :get_variables("("), padx=6, pady=5).grid(row=4, column=4)
Button(root, text="EXP", command=lambda :get_operation("**"), padx=3, pady=5).grid(row=5, column=4)


Button(root, text="<-", command=lambda :del_char(), padx=5, pady=5).grid(row=2, column=5)
Button(root, text="x!", command=lambda :factorial(), padx=5, pady=5).grid(row=3, column=5)
Button(root, text=")", command=lambda :get_variables(")"), padx=6, pady=5).grid(row=4, column=5)
Button(root, text="^2", command=lambda :get_operation("**2"), padx=3, pady=5).grid(row=5, column=5)




root.mainloop()