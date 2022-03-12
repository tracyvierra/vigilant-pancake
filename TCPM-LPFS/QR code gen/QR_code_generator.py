# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description:

# Usage:


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pyqrcode
from PIL import Image, ImageTk

root = tk.Tk()

canvas = Canvas(root, width = 400, height = 600)
canvas.pack()

app_label = tk.Label(root, text = "QR Code Generator", fg='blue', font=('Helvetica', 16))
canvas.create_window(200, 50, window=app_label)



root.mainloop()