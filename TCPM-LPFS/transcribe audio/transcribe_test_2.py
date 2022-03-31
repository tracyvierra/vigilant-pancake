# Author: Tracy Vierra
# Date Created: 3/30/2022
# Date Modified: 3/30/2022

# Description: a Python program that will transcribe given mp3 files to text

# Usage:

from turtle import clear
import speech_recognition as sr
from os import path
from pydub import AudioSegment

sound = AudioSegment.from_mp3("hello.mp3")
sound.export('hello.wav', format='wav')

AUDIO_FILE = 'hello.wav'
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    print("Transcription:", r.recognize_google(audio))
    