# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description: Text to speech example

# Usage:

from turtle import bgcolor
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

def open_file_input():
    input_file = fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("text files","*.txt")))
    input_entry.insert(0, input_file)

def open_file_output():
    output_file = fd.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("text files","*.txt")))
    output_entry.insert(0, output_file)

def clear_fields():
    input_entry.delete(0,tk.END)
    output_entry.delete(0,tk.END)

def convert(input_file, output_file):
    text = open(input_file, 'r').read()
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)



window = tk.Tk()
window.title("Text 2 Speech")
window.geometry("300x150")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window, text="Input file:")
output_label = tk.Label(window, text="Output file:")

input_label.grid(row = 0, column = 0)
output_label.grid(row = 0, column = 1)

input_entry.grid(row=2, column=0)
output_entry.grid(row=2, column=1)

button_clear = tk.Button(window, text="Clear", command=lambda: clear_fields())
button_clear.grid(row=2, column=4)

button_file_input = tk.Button(window, text="Input file", command=lambda: open_file_input())
button_file_input.grid(row=3, column=0)

button_file_output = tk.Button(window, text="Output file", command=lambda: open_file_output())
button_file_output.grid(row=3, column=1)

button_convert = tk.Button(window, text="Convert", command=lambda: convert(input_entry.get(), output_entry.get()))
button_convert.configure(background='green', foreground='white')
button_convert.grid(row=6, column=0)

button_exit = tk.Button(window, text="Exit", command=lambda: window.destroy())
button_exit.grid(row=6, column=1)

window.mainloop()



# text = open('demo.txt', 'r').read()

# gTTS(text=text, lang='en').save("hello.mp3")
# os.system("start hello.mp3")