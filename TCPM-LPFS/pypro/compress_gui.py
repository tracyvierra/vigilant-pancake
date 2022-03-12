# Author: Tracy Vierra
# Date Created: 3/10/2022
# Date Modified: 3/10/2022

# Description:

# Usage:

from fileinput import filename
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import zlib, base64

def compress(input_file, output_file):
	data = open(input_file, 'r').read()
	b_data = bytes(data, 'utf-8')
	compressed_data = base64.b64encode(zlib.compress(b_data,9))		
	compressed_file = open(output_file, 'w').write(compressed_data.decode('utf-8'))	
	return compressed_file

def decompress(input_file, output_file):
	compressed_data = open(input_file, 'r').read()
	decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
	decompressed_file = open(output_file, 'w').write(decompressed_data.decode('utf-8'))
	return decompressed_file

def compression(i,o):
	compress(i,o)

def decompression(i,o):
	decompress(i,o)

def open_file_input():
    input_file = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("text files","*.txt")))
    input_entry.insert(0, input_file)

def open_file_output():
    output_file = fd.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("text files","*.txt")))
    output_entry.insert(0, output_file)

def clear_fields():
    input_entry.delete(0,tk.END)
    output_entry.delete(0,tk.END)


window = tk.Tk()
window.title("Compression engine")
window.geometry("300x150")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text="Input file:")
output_label = tk.Label(window, text="Output file:")

input_label.grid(row = 0, column = 0)
output_label.grid(row = 0, column = 1)

input_entry.grid(row=2, column=0)
output_entry.grid(row=2, column=1)

button_compress = tk.Button(window, text="Compress", command=lambda: compress(input_entry.get(), output_entry.get()))
button_compress.configure(background="green", foreground="white")
button_decompress = tk.Button(window, text="Decompress", command=lambda: decompress(input_entry.get(), output_entry.get()))
button_decompress.configure(background="green", foreground="white")

button_compress.grid(row=6, column=0)
button_decompress.grid(row=6, column=1)

button_clear = tk.Button(window, text="Clear", command=lambda: clear_fields())
button_clear.grid(row=2, column=4)

button_file_input = tk.Button(window, text="Input file", command=lambda: open_file_input())
button_file_input.configure(background="cyan", foreground="black")
button_file_input.grid(row=3, column=0)

button_file_output = tk.Button(window, text="Output file", command=lambda: open_file_output())
button_file_output.configure(background="cyan", foreground="black")
button_file_output.grid(row=3, column=1)

button_exit = tk.Button(window, text="Exit", command=window.destroy)
button_exit.configure(background="red", foreground="black")
button_exit.grid(row=7, column=4)


window.mainloop()



# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file to compress',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )

# open_button = ttk.Button(
#     window,
#     text='Open a File',
#     command=select_file
# )

# open_button.grid(row=5, column=0)