# Author: Tracy Vierra
# Date Created: 3/30/2022
# Date Modified: 3/30/2022

# Description: a Python program that will transcribe given mp3 files to text

# Usage:

import sys
from os import path
from textwrap import TextWrapper

import pyaudio
import pydub

p = pyaudio.PyAudio()

# Open the audio device
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=48000,
                input=True,
                frames_per_buffer=1024)

# Loop until we are done.
while not stream.stop_stream():
    data = stream.read(1024)
    try:
        # Transcribe, if you want to use this as an input to a natural language
        # recognizer, use pydub.AudioSegment.duration_ms()
        duration = int(round(data.duration_ms))
        text = TextWrapper(
            data,
            width=duration,
            newline=True,
            indent=4)
        print(text.as_string())
    except:
        print("Error")

print("Bye")
stream.close()
p.terminate()
sys.exit()
