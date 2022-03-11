# Author: Tracy Vierra
# Date Created: 3/11/2022
# Date Modified: 3/11/2022

# Description: Text to speech example

# Usage:

from gtts import gTTS
import os

text = open('demo.txt', 'r').read()

gTTS(text=text, lang='en').save("hello.mp3")
os.system("start hello.mp3")

