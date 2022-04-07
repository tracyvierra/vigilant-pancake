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
import subprocess as sp		# subprocess
import re 			# regular expression
import urllib.request		# url request
import urllib.parse 		# url parse
import urllib.error 		# url error
import urllib.request 		# url request
import pyjokes
import pyautogui
import pywhatkit as kit
from time import sleep
from email.message import EmailMessage
from secrets import senderemail, gmail_user, gmail_pwd

# from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
# from os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
# from pprint import pprint

OPENWEATHER_APP_ID = "cce9b0c81b54033cc50f4e071fc11360"

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

def get_random_advice():
	res = requests.get("https://api.adviceslip.com/advice").json()
	return res['slip']['advice']

def get_trending_movies():
	trending_movies = []
	res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key=a300e27e1b4a17e70eee7745e3e1da69").json()
	results = res["results"]
	for r in results:
        	trending_movies.append(r["original_title"])
	return trending_movies[:10]

def get_trending_tv_shows():
	trending_tv_shows = []
	res = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key=a300e27e1b4a17e70eee7745e3e1da69").json()
	results = res["results"]
	for r in results:
        	trending_tv_shows.append(r["original_title"])
	return trending_tv_shows[:10]

def play_on_youtube(video):
	speak("Opening youtube")
	kit.playonyt(video)

def open_notepad():
	speak("Opening notepad")
	os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++")

def open_discord():
	speak("Opening Discord")
	sp.run('C:\\Users\\tracy\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe', shell=True)

def open_camera():
	speak("Opening camera")
	sp.run('start microsoft.windows.camera:', shell=True)

def open_wordpad():
	speak("Opening Wordpad")
	sp.Popen('C:\\Windows\\System32\\write.exe')

def open_calculator():
	speak("Opening calculator")
	sp.run('start calc', shell=True)

def open_steam():
	speak("Opening Steam")
	sp.run('start steam', shell=True)



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
				speak("Sorry the email is not responding")
		elif 'temperature' in query:
			try:
				speak("What is the city?")
				city = takeCommandMIC()
				speak("What is the country?")
				country = takeCommandMIC()
				url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&appid=cce9b0c81b54033cc50f4e071fc11360"
				json_data = requests.get(url).json()
				temp = json_data['main']['temp']
				temp = temp - 273.15
				temp = (temp * (9/5)) + 32
				temp = round(temp, 2)
				speak("The temperature in " + city + " is " + str(temp) + " degrees farenheit")
			except Exception as e:
				print(e)
				speak("Sorry the weather API is not responding")
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
				speak("Sorry the list is not responding")
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
				speak("Sorry the list is not responding")
		elif 'delete list' in query:
			try:
				speak("What is the name of the list?")
				name = takeCommandMIC()
				list_name = name + ".txt"
				os.remove(list_name)
				speak("List has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry the list is not responding")
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
				speak("Sorry the file is not responding")
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
				speak("Sorry the file is not responding")
		elif 'delete text file' in query:
			try:
				speak("What is the name of the file?")
				name = takeCommandMIC()
				file_name = name + ".txt"
				os.remove(file_name)
				speak("File has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry the file is not responding")
		elif 'create folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.mkdir(name)
				speak("Folder has been created")
			except Exception as e:
				print(e)
				speak("Sorry the folder is not responding")
		elif 'delete folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.rmdir(name)
				speak("Folder has been deleted")
			except Exception as e:
				print(e)
				speak("Sorry the folder is not responding")
		elif 'open folder' in query:
			try:
				speak("What is the name of the folder?")
				name = takeCommandMIC()
				os.chdir(name)
				speak("Folder has been opened")
			except Exception as e:
				print(e)
				speak("Sorry the folder is not responding")
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
				speak("Sorry the whatsapp service is not responding")
		elif 'news' in query:
			try:
				url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=37ac9a803d7b4f509cae0d11b6c40365"
				json_data = requests.get(url).json()
				articles = json_data['articles']
				for article in articles:
					print(article['title'])
					speak(article['title'])
			except Exception as e:
				print(e)
				speak("Sorry the news API is not responding")
		elif 'top ten' in query:
			try:
				url = "https://api.themoviedb.org/3/movie/popular?api_key=a300e27e1b4a17e70eee7745e3e1da69&language=en-US&page=1"
				json_data = requests.get(url).json()
				movies = json_data['results']
				for movie in movies:
					print(movie['title'])
					speak(movie['title'])
			except Exception as e:
				print(e)
				speak("Sorry the movies API is not responding")
		elif 'forecast' in query:
			try:
				speak("What is the name of the city?")
				city = takeCommandMIC()
				speak("What is the name of the country?")
				country = takeCommandMIC()
				url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&appid=cce9b0c81b54033cc50f4e071fc11360"
				json_data = requests.get(url).json()
				weather = json_data['weather']
				for w in weather:
					print(w['description'])
					speak(w['description'])
			except Exception as e:
				print(e)
				speak("Sorry the weather API is not responding")
		elif "advice" in query:
			try:
				speak(f"Here's some advice for you, sir")
				advice = get_random_advice()
				speak(advice)
				speak("For your convenience, I am printing it on the screen sir.")
				print(advice)
			except Exception as e:
				print(e)
				speak("Sorry the advice API is not responding")
		elif "trending movies" in query:
			try:
				speak(f"Some of the trending movies are: {get_trending_movies()}")
				speak("For your convenience, I am printing it on the screen sir.")
				print(*get_trending_movies(), sep='\n')
			except Exception as e:
				print(e)
				speak("Sorry the trending movies API is not responding")
		elif "trending tv shows" in query:
			try:
				speak(f"Some of the trending tv shows are: {get_trending_tv_shows()}")
				speak("For your convenience, I am printing it on the screen sir.")
				print(*get_trending_tv_shows(), sep='\n')
			except Exception as e:
				print(e)
				speak("Sorry the trending tv shows API is not responding")
		elif 'youtube' in query:
			try:
				speak('What do you want to play on Youtube?')
				video = takeCommandMIC().lower()
				play_on_youtube(video)
			except Exception as e:
				print(e)
				speak("Sorry the youtube API is not responding")
		elif 'discord' in query:
			open_discord()
		elif 'notepad' in query:
			open_notepad()
		elif 'calculator' in query:
			open_calculator()
		
		
		

		
		
		
		
			