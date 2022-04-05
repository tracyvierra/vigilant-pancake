# Author: Tracy Vierra
# Date Created: 4/5/2022
# Date Modified: 4/5/2022

# Description: Jarvis 2.0 personal assistant in python.

# Usage:

import speech_recognition as sr # speech recognition
import pyttsx3 			# text to speech
import datetime 		# date and time	
import wikipedia 		# wikipedia search 
import webbrowser 		# open browser
import os 			# operating system
import smtplib 			# send email
import random			# random number
import requests			# request
import json 			# json
import time 			# time
import sys 			# system
import subprocess 		# subprocess
import re 			# regular expression
import urllib.request		# url request
import urllib.parse 		# url parse
import urllib.error 		# url error
import urllib.request 		# url request

engine = pyttsx3.init()


# print("Hello, I am Jarvis. How can I help you?")
# engine.say("Hello, I am Jarvis. How can I help you?")
# engine.runAndWait()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def getvoices(voice):
	voices = engine.getProperty('voices')
	# print(voices[1].id)
	if voice == 1:
		engine.setProperty('voice', voices[0].id)
	if voice == 2:
		engine.setProperty('voice', voices[1].id)

def time():
	time = datetime.datetime.now().strftime("%I:%M:%S")
	speak("The current time is " + time)

voice = int(input("Select voice: 1. male 2. female: "))
getvoices(voice)

time()

	
# while True:
# 	voice = int(input("Select voice: 1. male 2. female: "))
# 	getvoices(voice)
# 	audio = "Hello, I am Jarvis. How can I help you?"
# 	speak(audio)





