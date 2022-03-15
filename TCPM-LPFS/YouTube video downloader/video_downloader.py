# Author: Tracy Vierra
# Date Created: 3/15/2022
# Date Modified: 3/15/2022

# Description: GUI app to download YouTube videos by link.

# Usage:

import moviepy as mp
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox



root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x500")

canvas = tk.Canvas(root, height=400, width=300)
canvas.pack()

# app label
app_label = tk.Label(root, text="YouTube Video Downloader", fg='blue' ,font=("Helvetica", 20))
canvas.create_window(150, 25, window=app_label)

# entry to accept video link
url_label = tk.Label(root, text = "Enter video URL:")
url_entry = tk.Entry(root, width=50)
canvas.create_window(150, 80, window=url_label)
canvas.create_window(150, 100, window=url_entry)








root.mainloop()