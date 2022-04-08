# Author: Tracy Vierra
# Date Created: 4/5/2022
# Date Modified: 4/8/2022

# Description: Jarvis 2.0 personal assistant in python.

# Usage: jarvis.py


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
	try:

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
	except Exception as e:
		print(e)
		print("Failed to send mail")

def sendWhatsApp_msg(phone_num, msg):
	try:
		url = "https://api.whatsapp.com/send?phone={}&text={}".format(phone_num, msg)
		webbrowser.open(url)
		sleep(8)
		pyautogui.press('enter')
	except Exception as e:
		print(e)
		print("Failed to send message")

def get_random_advice():
	try:
		res = requests.get("https://api.adviceslip.com/advice").json()
		return res['slip']['advice']
	except Exception as e:
		print(e)
		print("Failed to get advice")

def get_trending_movies():
	try:
		trending_movies = []
		res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key=a300e27e1b4a17e70eee7745e3e1da69").json()
		results = res["results"]
		for r in results:
 		       	trending_movies.append(r["original_title"])
		return trending_movies[:10]
	except Exception as e:
		print(e)
		print("Failed to get trending movies")

def get_trending_tv_shows():
	try:
		trending_tv_shows = []
		res = requests.get(f"https://api.themoviedb.org/3/trending/tv/day?api_key=a300e27e1b4a17e70eee7745e3e1da69").json()
		results = res["results"]
		for r in results:
 		       	trending_tv_shows.append(r["original_title"])
		return trending_tv_shows[:10]
	except Exception as e:
		print(e)
		print("Failed to get trending tv shows")

def play_on_youtube(video):
	try:
		speak("Opening youtube")
		kit.playonyt(video)
	except Exception as e:
		print(e)
		print("Failed to play on youtube")

def open_notepad():
	try:
		speak("Opening notepad")
		os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++")
	except Exception as e:
		print(e)
		print("Failed to open notepad")

def open_discord():
	try:
		speak("Opening Discord")
		sp.run('C:\\Users\\tracy\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open Discord")

def open_camera():
	try:
		speak("Opening camera")
		sp.run('start microsoft.windows.camera:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open camera")

def open_wordpad():
	try:
		speak("Opening Wordpad")
		sp.Popen('C:\\Windows\\System32\\write.exe')
	except Exception as e:
		print(e)
		print("Failed to open Wordpad")

def open_calculator():
	try:
		speak("Opening calculator")
		sp.run('start calc', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open calculator")

def open_steam():
	try:
		speak("Opening Steam")
		os.startfile("C:\\Users\\tracy\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk")
	except Exception as e:
		print(e)
		print("Failed to open Steam")

def open_edge():
	try:
		speak("Opening Edge")
		sp.run('start microsoft-edge:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open Edge")

def open_chrome():
	try:
		speak("Opening Chrome")
		sp.run('start chrome', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open Chrome")

def open_firefox():
	try:
		speak("Opening FireFox")
		sp.run('start firefox', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open FireFox")

def open_cmd():
	try:
		speak("Opening Command Prompt")
		sp.run('start cmd', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open Command Prompt")

def open_office():
	try:
		speak("Opening Libre Office")
		sp.Popen('C:\\Program Files\\LibreOffice\\program\\soffice.exe')
	except Exception as e:
		print(e)
		print("Failed to open Libre Office")

def open_reason():
	try:
		sp.Popen('C:\\Program Files\\Propellerhead\\Reason 10\\Reason.exe')
		sleep(4)
		pyautogui.press('enter')
	except Exception as e:
		print(e)
		print("Failed to open Reason")

def append_list(list_name, item):
	try:
		with open(list_name, 'a') as f:
			f.write('\n' + item + '\n')
	except Exception as e:
		print(e)
		print("Failed to append to list")

def open_calendar():
	try:
		sp.run('start outlookcal:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open calendar")

def open_maps():
	try:
		sp.run('start explorer shell:appsfolder\\Microsoft.WindowsMaps_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open maps")

def open_voice_recorder():
	try:
		sp.run('start shell:appsfolder\\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open voice recorder")

def open_snip_sketch():
	try:
		sp.run('start shell:appsfolder\\Microsoft.ScreenSketch_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open snip sketch")

def open_microsoft_store():
	try:
		sp.run('start shell:appsfolder\\Microsoft.WindowsStore_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open microsoft store")

def open_snipping_tool():
	try:
		sp.Popen('C:\\windows\\system32\\SnippingTool.exe')
		# sp.run('start shell:appsfolder\\Microsoft.SnippingTool_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open snipping tool")

def open_check_for_updates():
	try:
		sp.run('start shell:appsfolder\\Microsoft.WindowsUpdate_8wekyb3d8bbwe!App:', shell=True)
	except Exception as e:
		print(e)
		print("Failed to open check for updates")

def open_vnc_viewer():
	try:
		sp.Popen('"C:\\Program Files\\RealVNC\\VNC Viewer\\vncviewer.exe"')
	except Exception as e:
		print(e)
		print("Failed to open vnc viewer")

def open_windscribe():
	try:
		sp.Popen('C:\\Program Files (x86)\\Windscribe\\WindscribeLauncher.exe')
	except Exception as e:
		print(e)
		print("Failed to open windscribe")

def open_screenshot():
	try:
		image = pyautogui.screenshot()
		image.save('screenshot.png')
		speak('Screenshot taken.')
	except Exception as e:
		print(e)
		print("Failed to open screenshot")

def open_take_a_note():	
	try:
		speak("Taking a note")
		note_text = takeCommandMIC()
		if(note_text!=None):
			f = open('notes.txt','a')
			timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			f.write(timestamp + '\n')
			note = note_text + '\n\n'
			f.write(note)
			f.close()
			speak("Note taken")
			print("Note taken.")
	except Exception as e:
		print(e)
		print("Failed to take a note")

def wishme():
	try:
		speak("Welcome back sir!")
		greeting()
		time()
		date()
		speak("Jarvis at your service, please tell me how I can help?")
	except Exception as e:
		print(e)
		print("Failed to wish me")

voice = int(input('Enter number to select voice for Jarvis: \n1. Male \n2. Female \n'))
getvoices(voice)


if __name__ == '__main__':
	wishme()
	while True:
		query = takeCommandMIC().lower()
		if 'current time' in query:
			time()
		elif 'current date' in query:
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
		elif 'append list' in query:
			try:
				speak("Which list do you want to append?")
				name = takeCommandMIC().lower()
				list_name = name + ".txt"
				speak("What do you want to append?")
				append = takeCommandMIC().lower()
				append_list(list_name, append)				
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
		elif 'back one folder' in query:
			try:
				os.chdir('..')
				print(os.getcwd())
				speak("Folder has been opened")
			except Exception as e:
				print(e)
				speak("Sorry the folder is not responding")
		elif 'what folder' in query:
			try:
				print(os.getcwd())
				speak(os.getcwd())
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
		elif 'top 20' in query:
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
				speak("For your convenience, I am printing it on the screen.")
				print(*get_trending_movies(), sep='\n')
			except Exception as e:
				print(e)
				speak("Sorry the trending movies API is not responding")
		elif "trending tv shows" in query:
			try:
				speak(f"Some of the trending tv shows are: {get_trending_tv_shows()}")
				speak("For your convenience, I am printing it on the screen.")
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
				speak("Sorry youtube is not responding")
		elif 'discord' in query:
			try:
				open_discord()
			except Exception as e:
				print(e)
				speak("Sorry discord is not responding")
		elif 'notepad' in query:
			try:
				open_notepad()
			except Exception as e:
				print(e)
				speak("Sorry notepad is not responding")
		elif 'calculator' in query:
			try:
				open_calculator()
			except Exception as e:
				print(e)
				speak("Sorry calculator is not responding")
		elif 'wordpad' in query:
			try:
				open_wordpad()
			except Exception as e:
				print(e)
				speak("Sorry wordpad is not responding")
		elif 'chrome' in query:
			try:
				open_chrome()
			except Exception as e:
				print(e)
				speak("Sorry chrome is not responding")
		elif 'firefox' in query:
			try:
				open_firefox()
			except Exception as e:
				print(e)
				speak("Sorry firefox is not responding")
		elif 'steam' in query:
			try:
				open_steam()
			except Exception as e:
				print(e)
				speak("Sorry Steam is not responding")
		elif 'edge' in query:
			try:
				open_edge()
			except Exception as e:
				print(e)
				speak("Sorry Microsoft Edge is not responding")
		elif 'prompt' in query:
			try:
				open_cmd()
			except Exception as e:
				print(e)
				speak("Sorry command prompt is not responding")
		elif 'office' in query:
			try:
				open_office()
			except Exception as e:
				print(e)
				speak("Sorry office is not responding")
		elif 'reason' in query:
			try:
				speak("Opening Reason")
				open_reason()
			except Exception as e:
				print(e)
				speak("Sorry Reason is not responding")
		elif 'calendar' in query:
			try:
				speak("Opening Calendar")
				open_calendar()
			except Exception as e:
				print(e)
				speak("Sorry Calendar is not responding")
		elif 'maps' in query:
			try:
				speak("Opening Maps")
				open_maps()
			except Exception as e:
				print(e)
				speak("Sorry Maps is not responding")
		elif 'voice recorder' in query:
			try:
				speak("Opening Voice Recorder")
				open_voice_recorder()
			except Exception as e:
				print(e)
				speak("Sorry Voice Recorder is not responding")
		elif 'snip and sketch' in query:
			try:
				speak("Opening Snip and Sketch")
				open_snip_sketch()
			except Exception as e:
				print(e)
				speak("Sorry Snip and Sketch is not responding")
		elif 'microsoft store' in query:
			try:
				speak("Opening Microsoft Store")
				open_microsoft_store()
			except Exception as e:
				print(e)
				speak("Sorry Microsoft Store is not responding")
		
		elif 'snipping tool' in query:
			try:
				speak("Opening Snipping Tool")
				open_snipping_tool()
			except Exception as e:
				print(e)
				speak("Sorry Snipping Tool is not responding")
		elif 'check for updates' in query:
			try:
				speak("Checking for updates")
				open_check_for_updates()
			except Exception as e:
				print(e)
				speak("Sorry Check for updates is not responding")
		elif 'vnc viewer' in query:
			try:
				speak("Opening VNC Viewer")
				open_vnc_viewer()
			except Exception as e:
				print(e)
				speak("Sorry VNC Viewer is not responding")
		elif 'windscribe' in query:
			try:
				speak("Opening Windscribe")
				open_windscribe()
			except Exception as e:
				print(e)
				speak("Sorry Windscribe is not responding")
		elif 'screenshot' in query:
			try:
				speak("Opening Screenshot")
				open_screenshot()
			except Exception as e:
				print(e)
				speak("Sorry Screenshot is not responding")
		elif 'take a note' in query:
			try:
				speak("Opening Take a Note")
				open_take_a_note()
			except Exception as e:
				print(e)
				speak("Sorry Take a Note is not responding")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

		
		
		
		
			