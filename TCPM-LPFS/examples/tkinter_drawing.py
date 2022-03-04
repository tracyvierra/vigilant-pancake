# Author: Tracy Vierra
# Date Created: 3/3/2022
# Date Modified: 3/3/2022

# Description:

# Usage:

from tkinter import *


root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 200, 100, fill="blue")
newline2 = canvas.create_line(0, 100, 200, 0, fill="blue")
newrect = canvas.create_rectangle(50, 25, 150, 75, fill="red")
# newpolygon = canvas.create_polygon(10, 10, 10, 40, 30, 20, fill="green")


root.mainloop()

