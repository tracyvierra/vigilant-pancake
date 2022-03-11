# Author: Tracy Vierra
# Date Created: 3/10/2022
# Date Modified: 3/10/2022

# Description:

# Usage:

import tkinter as tk
from tkinter import filedialog
from compression_module import compress, decompress

def compression(i,o):
	compress(i,o)

def decompression(i,o):
	decompress(i,o)



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

button_compress = tk.Button(window, text="Compress", command=lambda: compression(input_entry.get(), output_entry.get()))
button_decompress = tk.Button(window, text="Decompress", command=lambda: decompression(input_entry.get(), output_entry.get()))

button_compress.grid(row=3, column=0)
button_decompress.grid(row=3, column=1)

# input_file = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
# output_file = filedialog.asksaveasfilename(filetypes=(("All files", "*.*"), ("Text files", "*.txt")))

# input_file.grid(row=4, column=0)
# output_file.grid(row=4, column=1)



window.mainloop()




