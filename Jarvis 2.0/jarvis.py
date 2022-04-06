# Author: Tracy Vierra
# Date Created: 4/5/2022
# Date Modified: 4/6/2022

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
import pyautogui
from time import sleep
from email.message import EmailMessage
from secrets import senderemail, gmail_user, gmail_pwd


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

def sendWhatsApp_msg(phone_num, msg):
	url = "https://api.whatsapp.com/send?phone={}&text={}".format(phone_num, msg)
	webbrowser.open(url)
	sleep(8)
	pyautogui.press('enter')

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
			try:
				speak("Searching Wikipedia...")
				query = query.replace("wikipedia", "")
				results = wikipedia.summary(query, sentences=2)
				speak("According to Wikipedia")
				print(results)
				speak(results)
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not find any results")
		elif 'open youtube' in query:
			try:
				webbrowser.open("youtube.com")
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not open youtube")
		elif 'open google' in query:
			try:
				webbrowser.open("google.com")
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not open google")
		elif 'open stackoverflow' in query:
			try:
				webbrowser.open("stackoverflow.com")
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not open stackoverflow")
		elif 'play music' in query:
			try:
				music_dir = 'D:\\music\\Tracy Vierra\\420'
				songs = os.listdir(music_dir)
				print(songs)
				os.startfile(os.path.join(music_dir, songs[0]))
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not play music")
		elif 'open code' in query:
			try:
				codePath = 'D:\\Users\\tracy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
				os.startfile(codePath)
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not open code")
		elif 'percentile' in query:
			try:
				speak("Rolling the percentile die...")
				roll = random.randint(1, 100)
				speak("The result is " + str(roll) + "%")
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not roll the percentile die")
		elif 'search' in query:
			try:
				query = query.replace("search", "")
				query = query.replace("for", "")
				query = query.replace("on", "")
				query = query.replace("google", "")
				query = query.replace("youtube", "")
				query = query.replace("stackoverflow", "")
				query = query.replace(" ", "+")
				webbrowser.open("https://www.google.com/search?q=" + query)
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not search for " + query)
		elif 'who are you' in query:
			speak("I am Jarvis, your personal assistant. I am here to make your life easier!")
		elif 'who made you' in query:
			speak("I have been created by Tracy")
		elif 'tell me a joke' in query:
			try:
				speak(pyjokes.get_joke())
			except Exception as e:
				print(e)
				speak("Sorry sir, I could not tell you a joke")
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
		elif 'weather' in query:
			try:
				speak("What is the city?")
				city = takeCommandMIC()
				speak("What is the country?")
				country = takeCommandMIC()
				url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&appid=271d1234d3f497eed5b1d80a07b3fcd1"
				json_data = requests.get(url).json()
				temp = json_data['main']['temp']
				temp = temp - 273.15
				temp = (temp * (9/5)) + 32
				temp = round(temp, 2)
				speak("The temperature in " + city + " is " + str(temp) + " degrees farenheit")
			except Exception as e:
				print(e)
				speak("Sorry my friend weather API is not responding")
		elif 'create list' in query:
			try:
				speak("What is the name of the list?")
				name = takeCommandMIC()
				speak("What should I put in the list?")
				content = takeCommandMIC()
				list_name = name + ".txt"
				with open(list_name, 'w') as f:
					f.write(content)
				speak("List has been created")
			except Exception as e:
				print(e)
				speak("Sorry my friend list is not responding")
		elif 'read list' in query:
			try:
				speak("What is the name of the list?")
				name = takeCommandMIC()
				list_name = name + ".txt"
				with open(list_name, 'r') as f:
					content = f.read()
					print(content)
					speak(content)
			except Exception as e:
				print(e)
				speak("Sorry my friend list is not responding")
		elif 'delete list' in query:
			try:
				speak("What is the name of the list?")
				name = takeCommandMIC()
				list_name = name + ".txt"
				os.remove(list_name)
				speak("List has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry my friend list is not responding")
		elif 'create text file' in query:
			try:
				speak("What is the name of the file?")
				name = takeCommandMIC()
				speak("What should I put in the file?")
				content = takeCommandMIC()
				file_name = name + ".txt"
				with open(file_name, 'w') as f:
					f.write(content)
				speak("File has been created")
			except Exception as e:
				print(e)
				speak("Sorry my friend file is not responding")
		elif 'read text file' in query:
			try:
				speak("What is the name of the file?")
				name = takeCommandMIC()
				file_name = name + ".txt"
				with open(file_name, 'r') as f:
					content = f.read()
					print(content)
					speak(content)
			except Exception as e:
				print(e)
				speak("Sorry my friend file is not responding")
		elif 'delete text file' in query:
			try:
				speak("What is the name of the file?")
				name = takeCommandMIC()
				file_name = name + ".txt"
				os.remove(file_name)
				speak("File has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry my friend file is not responding")
		elif 'create folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.mkdir(name)
				speak("Folder has been created")
			except Exception as e:
				print(e)
				speak("Sorry my friend folder is not responding")
		elif 'delete folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.rmdir(name)
				speak("Folder has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry my friend folder is not responding")
		elif 'open folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.chdir(name)
				speak("Folder has been opened")
			except Exception as e:
				print(e)
				speak("Sorry my friend folder is not responding")
		elif 'whatsapp message' in query:
			user_name = {'Tracy': '+15093934105', 'Nicole': '+15094211558'}
			try:
				speak("Who should I send the message to?")
				name = takeCommandMIC()
				phone_num = user_name[name]
				speak("What should I say?")
				content = takeCommandMIC()
				sendWhatsApp_msg(phone_num, content)
				speak("Message has been sent")
			except Exception as e:
				print(e)
				speak("Sorry my friend whatsapp is not responding")
		

		
		
		
		

		
		
		
		
			