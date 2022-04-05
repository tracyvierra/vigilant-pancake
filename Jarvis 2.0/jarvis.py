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

def date():
	date = datetime.datetime.now().strftime("%d-%m-%Y")
	speak("The current date is " + date)

def greeting():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good Morning!")
	elif hour >= 12 and hour < 18:
		speak("Good Afternoon!")
	elif hour >= 18 and hour < 24:
		speak("Good Evening!")

def takeCommandCMD():
	query = input("Please tell me how I can help? : ")
	return query

def sendEmail(to, subject, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('tracyv', 'Tr1cky1!')
	server.sendmail(from_addr='tracyv@gmail.com', to_addrs=to, msg=content)


def wishme():
	greeting()
	time()
	date()
	speak("Jarvis at your service, please tell me how I can help?")

voice = int(input('Enter number to select voice for Jarvis: \n1. Male \n2. Female \n'))
getvoices(voice)




if __name__ == '__main__':
	wishme()
	while True:
		query = takeCommandCMD().lower()
		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'wikipedia' in query:
			speak("Searching Wikipedia...")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)
		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
		elif 'open google' in query:
			webbrowser.open("google.com")
		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")
		elif 'play music' in query:
			music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))
		elif 'open code' in query:
			codePath = 'D:\\Users\\tracy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
			os.startfile(codePath)
		elif 'email to nicole' in query:
			try:
				speak("What should I say?")
				content = takeCommandCMD()
				to = "buggirl_2057@yahoo.com"
				subject = "My Swee!"
				sendEmail(to, subject, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry my friend Nicole is not responding")
		elif 'roll a six sided' in query:
			speak("Rolling the six sided die...")
			roll = random.randint(1, 6)
			speak("The result is " + str(roll))
		elif 'roll a eight sided' in query:
			speak("Rolling the eight sided die...")
			roll = random.randint(1, 8)
			speak("The result is " + str(roll))
		elif 'roll a ten sided' in query:
			speak("Rolling the ten sided die...")
			roll = random.randint(1, 10)
			speak("The result is " + str(roll))
		elif 'roll a twelve sided' in query:
			speak("Rolling the twelve sided die...")
			roll = random.randint(1, 12)
			speak("The result is " + str(roll))
		elif 'roll a twenty sided' in query:
			speak("Rolling the twenty sided die...")
			roll = random.randint(1, 20)
			speak("The result is " + str(roll))
		elif 'roll a hundred sided' in query:
			speak("Rolling the one hundred sided die...")
			roll = random.randint(1, 100)
			speak("The result is " + str(roll))
		elif 'roll a percentile' in query:
			speak("Rolling the percentile die...")
			roll = random.randint(1, 100)
			speak("The result is " + str(roll) + "%")
		
		
			