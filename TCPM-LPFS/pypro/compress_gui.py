# Author: Tracy Vierra
# Date Created: 3/10/2022
# Date Modified: 3/10/2022

# Description:

# Usage:

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

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file to compress',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


window = tk.Tk()
window.title("Compression engine")
window.geometry("400x400")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text="Input file:")
output_label = tk.Label(window, text="Output file:")

input_label.grid(row = 0, column = 0)
output_label.grid(row = 0, column = 1)

input_entry.grid(row=2, column=0)
output_entry.grid(row=2, column=1)

button_compress = tk.Button(window, text="Compress", command=lambda: compress(input_entry.get(), output_entry.get()))
button_decompress = tk.Button(window, text="Decompress", command=lambda: decompress(input_entry.get(), output_entry.get()))

button_compress.grid(row=3, column=0)
button_decompress.grid(row=3, column=1)



# open_button = ttk.Button(
#     window,
#     text='Open a File',
#     command=select_file
# )

# open_button.grid(row=5, column=0)




window.mainloop()





