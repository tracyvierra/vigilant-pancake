# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description: Text to speech example using user input to speech and saved as a file.

# Usage:

from turtle import right
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *


# text = open('demo.txt', 'r').read()

# gTTS(text=text, lang='en').save("hello.mp3")
# os.system("start hello.mp3")

def convert(entry, output_file):
    text = entry
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

output_file = "output.mp3"

root = Tk()
root.title("Text 2 Speech")
canvas1 = tk.Canvas(root, width = 300, height = 100)
canvas1.pack()

entry = tk.Entry(root)
canvas1.create_window(150, 20, window=entry)
canvas1.pack()

button_convert = tk.Button(text='Convert', command= lambda:convert(entry.get(), output_file))
button_convert.configure(background='green', foreground='white')
canvas1.create_window(150, 60, window=button_convert)
canvas1.pack()

button_exit = tk.Button(root, text="Exit", command=lambda: root.destroy())
button_exit.configure(background='red', foreground='black')
button_exit.pack(padx=5, pady=5)


root.mainloop()
