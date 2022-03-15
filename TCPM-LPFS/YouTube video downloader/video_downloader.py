# Author: Tracy Vierra
# Date Created: 3/15/2022
# Date Modified: 3/15/2022

# Description: GUI app to download YouTube videos by link.

# Usage:

# from sysconfig import get_path
import moviepy
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *
import shutil




def download_video():
	video_path = url_entry.get()
	download_path = path_label.cget("text")
	mp4 = YouTube(video_path).streams.get_highest_resolution().download(download_path)
	video_clip = VideoFileClip(mp4)
	# code for mp3 conversion
	audio_file = video_clip.audio
	audio_file.write_audiofile("audio.mp3")
	audio_file.close()
	shutil.move("audio.mp3", download_path)
	# code for mp3 conversion
	video_clip.close()
	messagebox.showinfo("Download Complete", "Video downloaded to " + download_path)

    

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x350")

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

# path to download videos
path_label = tk.Label(root, text = "Select path to download videos:" ) 
path_button = tk.Button(root, text="Browse", command=get_path)
canvas.create_window(150, 150, window=path_label)
canvas.create_window(150, 180, window=path_button)


# download button
download_button = tk.Button(root, text="Download", command=lambda: download_video())
canvas.create_window(150, 250, window=download_button)



root.mainloop()