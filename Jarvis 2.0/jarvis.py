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



print("Hello, I am Jarvis. How can I help you?")

engine = pyttsx3.init()
engine.say("Hello, I am Jarvis. How can I help you?")
engine.runAndWait()

