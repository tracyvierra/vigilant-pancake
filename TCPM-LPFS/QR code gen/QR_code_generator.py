# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description:

# Usage:


import tkinter as tk
import pyqrcode
import sys
import png
from PIL import Image, ImageTk

def generate_qr():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=6)
    img = ImageTk.PhotoImage(Image.open(file_name))
    img_label = tk.Label(root, image=img)
    img_label.image = img
    canvas.create_window(200, 450, window=img_label)
    
def clear_all():
    name_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)
    

root = tk.Tk()
root.title("QR Code Generator")


canvas = tk.Canvas(root, width = 400, height = 600)
canvas.pack()

app_label = tk.Label(root, text = "QR Code Generator", fg='blue', font=('Helvetica', 16))
canvas.create_window(200, 50, window=app_label)

name_label = tk.Label(root, text = "Link name: ", fg='blue', font=('Helvetica', 12))
link_label = tk.Label(root, text = "Link: ", fg='blue', font=('Helvetica', 12))
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = tk.Entry(root, width = 30)
link_entry = tk.Entry(root, width = 30)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

button = tk.Button(root, text = "Generate QR Code", command = lambda: generate_qr())
canvas.create_window(200, 250, window=button)

button_clear = tk.Button(root, text = "Clear", command = lambda: clear_all())
canvas.create_window(200, 300, window=button_clear)

button_exit = tk.Button(root, text = "Exit", command = lambda: sys.exit())
button_exit.pack(padx=5, pady=5)


root.mainloop()