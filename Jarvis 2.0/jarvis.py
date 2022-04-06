# Author: Tracy Vierra
# Date Created: 4/5/2022
# Date Modified: 4/5/2022

# Description: Jarvis 2.0 personal assistant in python.

# Usage:


from unicodedata import name
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
import pyjokes
from email.message import EmailMessage
from secrets import senderemail, epwd, to, gmail_user, gmail_pwd


engine = pyttsx3.init()



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
	date = datetime.datetime.now().strftime("%m-%d-%Y")
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

def takeCommandMIC():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-US')
		print(f"User said: {query}\n")
	except Exception as e:
		print(e)
		print("Say that again please...")
		return "None"
	return query



def sendEmail(receiver, subject, content):
	# SMTP_SSL Example
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(gmail_user, gmail_pwd)  
	# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
	email = EmailMessage()
	email['From'] = senderemail
	email['To'] = receiver
	email['Subject'] = subject
	email.set_content(content)
	server_ssl.send_message(email)
	server_ssl.close()
	print('successfully sent the mail')

def wishme():
	speak("Welcome back sir!")
	greeting()
	time()
	date()
	speak("Jarvis at your service, please tell me how I can help?")

voice = int(input('Enter number to select voice for Jarvis: \n1. Male \n2. Female \n'))
getvoices(voice)


if __name__ == '__main__':
	wishme()
	while True:
		query = takeCommandMIC().lower()
		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'wiki' in query:
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
			music_dir = 'D:\\music\\Tracy Vierra\\420'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))
		elif 'open code' in query:
			codePath = 'D:\\Users\\tracy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
			os.startfile(codePath)
		elif 'percentile' in query:
			speak("Rolling the percentile die...")
			roll = random.randint(1, 100)
			speak("The result is " + str(roll) + "%")
		elif 'search' in query:
			query = query.replace("search", "")
			query = query.replace("for", "")
			query = query.replace("on", "")
			query = query.replace("google", "")
			query = query.replace("youtube", "")
			query = query.replace("stackoverflow", "")
			query = query.replace(" ", "+")
			webbrowser.open("https://www.google.com/search?q=" + query)
		elif 'who are you' in query:
			speak("I am Jarvis, your personal assistant. I am here to make your life easier!")
		elif 'who made you' in query:
			speak("I have been created by Tracy")
		elif 'tell me a joke' in query:
			speak(pyjokes.get_joke())
		elif 'offline' in query:
			speak("Jarvis is going offline")
			exit()
		elif 'email' in query:
			email_list = {'Tracy': 'tracyvierra@yahoo.com', 'Nicole': 'buggirl_2057@yahoo.com'}
			try:
				speak("Who should I send the email to?")
				name = takeCommandMIC()
				receiver = email_list[name]
				speak("what is the subject?")
				subject = takeCommandMIC()
				speak("What should I say?")
				content = takeCommandMIC()
				sendEmail(receiver, subject, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry my friend email is not responding")
		
		
		
		
		
		
			