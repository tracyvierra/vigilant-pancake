# Author: Tracy Vierra
# Date Created: 4/5/2022
# Date Modified: 4/12/2022

# Description: Jarvis 2.0 personal assistant in python.

# Usage: jarvis.py


from unicodedata import name
import speech_recognition as sr  # speech recognition
import pyttsx3  # text to speech
import datetime  # date and time
import wikipedia  # wikipedia search
import webbrowser  # open browser
import os  # operating system
import smtplib  # send email
import random  # random number
import requests  # request
import json  # json
import time  # time
import sys  # system
import subprocess as sp  # subprocess
import re  # regular expression
import urllib.request  # url request
import urllib.parse  # url parse
import urllib.error  # url error
import urllib.request  # url request
import pyjokes
import pyautogui
import pywhatkit as kit
import clipboard
import string
import psutil
from newsapi import NewsApiClient
from time import sleep
from email.message import EmailMessage
from secrets import senderemail, gmail_user, gmail_pwd

# Some responses as constants:
TEXT_SENT_RESPONSE = "Text message sent"
LIST_NAME_QUESTION = "What is the name of the list?"
LIST_NOT_RESPONDING = "Sorry the list is not responding"
FILE_NAME_QUESTION = "What is the name of the file?"
FILE_NOT_RESPONDING = "Sorry the file is not responding"
FOLDER_NAME_QUESTION = "What is the name of the folder?"
FOLDER_NOT_RESPONDING = "Sorry the folder is not responding"


# SMTP mail gateway constant:
SMTP_GATEWAY = "smtp.gmail.com"

# OpenWeather API:
APPID = "&appid=cce9b0c81b54033cc50f4e071fc11360"
OW_API_LINK = "http://api.openweathermap.org/data/2.5/weather?q="

# newsapi.org
NEWS_API_KEY = "37ac9a803d7b4f509cae0d11b6c40365"
NEWS_API_LINK = "https://newsapi.org/v2/top-headlines?country=us&apiKey="

# My Documents user:
MY_DOCUMENTS = os.path.expanduser("~/Documents")
USERNAME = "tracy"


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty("voices")
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty("voice", voices[0].id)
    if voice == 2:
        engine.setProperty("voice", voices[1].id)


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
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(receiver, subject, content):
    try:

        # SMTP_SSL Example
        server_ssl = smtplib.SMTP_SSL(SMTP_GATEWAY, 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        email = EmailMessage()
        email["From"] = senderemail
        email["To"] = receiver
        email["Subject"] = subject
        email.set_content(content)
        server_ssl.send_message(email)
        server_ssl.close()
        print("successfully sent the mail")
    except Exception as e:
        print(e)
        print("Failed to send mail")


def sendWhatsApp_msg(phone_num, msg):
    try:
        url = "https://api.whatsapp.com/send?phone={}&text={}".format(phone_num, msg)
        webbrowser.open(url)
        sleep(8)
        pyautogui.press("enter")
    except Exception as e:
        print(e)
        print("Failed to send message")


def get_random_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res["slip"]["advice"]
    except Exception as e:
        print(e)
        print("Failed to get advice")


def get_trending_movies():
    try:
        trending_movies = []
        res = requests.get(
            f"https://api.themoviedb.org/3/trending/movie/day?api_key=a300e27e1b4a17e70eee7745e3e1da69"
        ).json()
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
        res = requests.get(
            f"https://api.themoviedb.org/3/trending/tv/day?api_key=a300e27e1b4a17e70eee7745e3e1da69"
        ).json()
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
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
        )
    except Exception as e:
        print(e)
        print("Failed to open notepad")


def open_discord():
    try:
        speak("Opening Discord")
        sp.run(
            "C:\\Users\\tracy\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",
            shell=True,
        )
    except Exception as e:
        print(e)
        print("Failed to open Discord")


def open_camera():
    try:
        speak("Opening camera")
        sp.run("start microsoft.windows.camera:", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open camera")


def open_wordpad():
    try:
        speak("Opening Wordpad")
        sp.Popen("C:\\Windows\\System32\\write.exe")
    except Exception as e:
        print(e)
        print("Failed to open Wordpad")


def open_calculator():
    try:
        speak("Opening calculator")
        sp.run("start calc", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open calculator")


def open_steam():
    try:
        speak("Opening Steam")
        os.startfile(
            "C:\\Users\\tracy\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk"
        )
    except Exception as e:
        print(e)
        print("Failed to open Steam")


def open_edge():
    try:
        speak("Opening Edge")
        sp.run("start microsoft-edge:", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open Edge")


def open_chrome():
    try:
        speak("Opening Chrome")
        sp.run("start chrome", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open Chrome")


def open_firefox():
    try:
        speak("Opening FireFox")
        sp.run("start firefox", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open FireFox")


def open_cmd():
    try:
        speak("Opening Command Prompt")
        sp.run("start cmd", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open Command Prompt")


def open_office():
    try:
        speak("Opening Libre Office")
        sp.Popen("C:\\Program Files\\LibreOffice\\program\\soffice.exe")
    except Exception as e:
        print(e)
        print("Failed to open Libre Office")


def open_reason():
    try:
        sp.Popen("C:\\Program Files\\Propellerhead\\Reason 10\\Reason.exe")
        sleep(4)
        pyautogui.press("enter")
    except Exception as e:
        print(e)
        print("Failed to open Reason")


def append_list(list_name, item):
    try:
        with open(list_name, "a") as f:
            f.write("\n" + item + "\n")
    except Exception as e:
        print(e)
        print("Failed to append to list")


def open_calendar():
    try:
        sp.run("start outlookcal:", shell=True)
    except Exception as e:
        print(e)
        print("Failed to open calendar")


def open_maps():
    try:
        sp.run(
            "start explorer shell:appsfolder\\Microsoft.WindowsMaps_8wekyb3d8bbwe!App:",
            shell=True,
        )
    except Exception as e:
        print(e)
        print("Failed to open maps")


def open_voice_recorder():
    try:
        sp.run(
            "start shell:appsfolder\\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App:",
            shell=True,
        )
    except Exception as e:
        print(e)
        print("Failed to open voice recorder")


def open_snip_sketch():
    try:
        sp.run(
            "start shell:appsfolder\\Microsoft.ScreenSketch_8wekyb3d8bbwe!App:",
            shell=True,
        )
    except Exception as e:
        print(e)
        print("Failed to open snip sketch")


def open_microsoft_store():
    try:
        sp.run(
            "start shell:appsfolder\\Microsoft.WindowsStore_8wekyb3d8bbwe!App:",
            shell=True,
        )
    except Exception as e:
        print(e)
        print("Failed to open microsoft store")


def open_snipping_tool():
    try:
        sp.Popen("C:\\windows\\system32\\SnippingTool.exe")
    except Exception as e:
        print(e)
        print("Failed to open snipping tool")


def open_check_for_updates():
    try:
        os.system("control update")
        sleep(3)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
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
        sp.Popen("C:\\Program Files (x86)\\Windscribe\\WindscribeLauncher.exe")
    except Exception as e:
        print(e)
        print("Failed to open windscribe")


def open_screenshot():
    try:
        image = pyautogui.screenshot()
        timestamp = datetime.datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
        image.save('screenshot-{}.png'.format(timestamp))
        speak("Screenshot taken.")
    except Exception as e:
        print(e)
        print("Failed to take a screenshot")


def open_take_a_note():
    try:
        speak("Taking a note")
        note_text = takeCommandMIC()
        if note_text != None:
            f = open("notes.txt", "a")
            timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            f.write(timestamp + "\n")
            note = note_text + "\n\n"
            f.write(note)
            f.close()
            speak("Note taken")
            print("Note taken.")
    except Exception as e:
        print(e)
        print("Failed to take a note")


def open_send_sms_text():
    try:
        speak("What number please?")
        number = takeCommandMIC()
        number = number.replace(" ", "")
        if number != None:
            speak("What message would you like to send?")
            text = takeCommandMIC()
            if text != None:
                # sp.Popen('C:\\Program Files (x86)\\Windows Phone\\Windows Phone 10\\App\\10.0.17763.1\\Phone\\bin\\SMS.exe ' + number + ' ' + text)
                server_ssl = smtplib.SMTP_SSL(SMTP_GATEWAY, 465)
                server_ssl.ehlo()  # optional, called by login()
                server_ssl.login(gmail_user, gmail_pwd)
                server_ssl.sendmail(
                    "Jarvis", number + "@mms.att.net", text
                )  # using the address for AT&T Wireless, for Verizon, use 'vtext.com', for T-Mobile, use 'tmomail.net'.
                speak(TEXT_SENT_RESPONSE)
                print(TEXT_SENT_RESPONSE)
    except Exception as e:
        print(e)
        print("Failed to send a text message")


def open_send_text_to():
    try:
        text_list = {"Tracy": "5093934105", "Nicole": "5094211558"}
        speak("Who would you like to send to?")
        number = text_list[takeCommandMIC()]
        if number != None:
            speak("What message would you like to send?")
            text = takeCommandMIC()
            if text != None:
                server_ssl = smtplib.SMTP_SSL(SMTP_GATEWAY, 465)
                server_ssl.ehlo()  # optional, called by login()
                server_ssl.login(gmail_user, gmail_pwd)
                server_ssl.sendmail(
                    "Jarvis", number + "@mms.att.net", text
                )  # using the address for AT&T Wireless, for Verizon, use 'vtext.com', for T-Mobile, use 'tmomail.net'.
                speak(TEXT_SENT_RESPONSE)
                print(TEXT_SENT_RESPONSE)
    except Exception as e:
        print(e)
        print("Failed to send a text message")


def open_check_weather():
    try:
        speak("What is your zip code?")
        zip_code = takeCommandMIC()
        url = OW_API_LINK + zip_code + APPID + "&units=imperial"
        res = requests.get(url)
        data = res.json()
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        temp = round(temp, 2)
        description = data["weather"][0]["description"]
        print(temp)
        print(weather)
        speak("The temperature is" + str(temp) + " degrees")
        speak("The forcast is " + description)
    except Exception as e:
        print(e)
        print("Failed to check weather")

def open_read_selected_text():
    try:
        text = clipboard.paste()
        speak(text)
        print(text)
    except Exception as e:
        print(e)
        print("Failed to read selected text")


def open_check_news():
    try:
        speak("What is the topic?")
        topic = takeCommandMIC().lower()
        newsapi = NewsApiClient(api_key='37ac9a803d7b4f509cae0d11b6c40365')
        data = newsapi.get_everything(q=topic, language='en', page_size=7)
        for i in range(len(data["articles"])):
            speak(data["articles"][i]["title"])
            print(data["articles"][i]["title"])
    except Exception as e:
        print(e)
        print("Failed to get news")

def open_my_documents():
    try:
        sp.Popen("explorer C:\\Users\\" + USERNAME + "\\Documents")
    except Exception as e:
        print(e)
        print("Failed to open my documents")
        
def wishme():
    try:
        speak("Welcome back Tracy!")
        greeting()
        time()
        date()
        speak("Jarvis at your service, what can I do for you?")
    except Exception as e:
        print(e)
        print("Failed to wish me")

def open_remember():
    try:
        speak("What would you like to remember?")
        text = takeCommandMIC()
        if text != None:
            f = open("remember.txt", "a")
            timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            f.write(timestamp + "\n")
            note = text + "\n\n"
            f.write(note)
            f.close()
            speak("Note taken")
            print("Note taken.")
    except Exception as e:
        print(e)
        print("Failed to take a note")

def open_generate_password():
    try:
        speak("How many characters would you like your password to be?")
        length = int(takeCommandMIC())
        if length != None:
            password = ""
            for i in range(length):
                password += random.choice(string.ascii_letters + string.digits)
            speak("Your password is " + password)
            print("Your password is " + password)
    except Exception as e:
        print(e)
        print("Failed to generate password")

def open_flip_a_coin():
    try:
        speak("Flipping a coin")
        coin = random.choice(["heads", "tails"])
        speak("The coin landed on " + coin)
        print("The coin landed on " + coin)
    except Exception as e:
        print(e)
        print("Failed to flip a coin")

def open_roll_dice():
    try:
        speak("Rolling a dice")
        dice = random.choice(["1", "2", "3", "4", "5", "6"])
        speak("The dice landed on " + dice)
        print("The dice landed on " + dice)
    except Exception as e:
        print(e)
        print("Failed to roll a dice")

def open_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent()
        speak("The CPU usage is " + str(cpu_usage) + "%")
        print("The CPU usage is " + str(cpu_usage) + "%")
    except Exception as e:
        print(e)
        print("Failed to get CPU stats")

def open_ram_usage():
    try:
        ram_usage = psutil.virtual_memory()[2]
        speak("The RAM usage is " + str(ram_usage) + "%")
        print("The RAM usage is " + str(ram_usage) + "%")
    except Exception as e:
        print(e)
        print("Failed to get RAM usage")

def open_disk_usage():
    try:
        disk_usage_c = psutil.disk_usage("C:")[3]
        disk_usage_d = psutil.disk_usage("D:")[3]
        speak("The C disk usage is " + str(disk_usage_c) + "%")
        print("The C: disk usage is " + str(disk_usage_c) + "%")
        speak("The D disk usage is " + str(disk_usage_d) + "%")
        print("The D: disk usage is " + str(disk_usage_d) + "%")
    except Exception as e:
        print(e)
        print("Failed to get disk usage")

def open_battery_status():
    try:
        battery_status = psutil.sensors_battery()[0]
        speak("The battery status is " + str(battery_status))
        print("The battery status is " + str(battery_status))
    except Exception as e:
        print(e)
        print("Failed to get battery status")

def open_check_internet_connection():
    try:
        url = "http://google.com"
        res = requests.get(url)
        if res.status_code == 200:
            speak("Internet connection is working")
            print("Internet connection is working")
        else:
            speak("Internet connection is not working")
            print("Internet connection is not working")
    except Exception as e:
        print(e)
        print("Failed to check internet connection")




try:
    voice = int(input("Enter number to select voice for Jarvis: \n1. Male \n2. Female \n"))
    getvoices(voice)
except Exception as e:
    print(e)
    print("failed to set voice.")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandMIC().lower()
        if "current time" in query:
            time()
        elif "current date" in query:
            date()
        elif "wiki" in query:
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
        elif "open youtube" in query:
            try:
                webbrowser.open("youtube.com")
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not open youtube")
        elif "open google" in query:
            try:
                webbrowser.open("google.com")
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not open google")
        elif "open stackoverflow" in query:
            try:
                webbrowser.open("stackoverflow.com")
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not open stackoverflow")
        elif "play music" in query:
            try:
                music_dir = "D:\\music\\Tracy Vierra\\420"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not play music")

        elif "open code" in query:
            try:
                codePath = "D:\\Users\\tracy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not open code")

        elif "percentile" in query:
            try:
                speak("Rolling the percentile die...")
                roll = random.randint(1, 100)
                speak("The result is " + str(roll) + "%")
                print("The result is " + str(roll) + "%")
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not roll the percentile die")

        elif "search" in query:
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
        elif "who are you" in query:
            speak(
                "I am Jarvis, your personal assistant. I am here to make your life easier!"
            )
            print(
                "I am Jarvis, your personal assistant. I am here to make your life easier!"
            )
        elif "who made you" in query:
            speak("I have been created by Tracy")
            print("I have been created by Tracy")
        elif "tell me a joke" in query:
            try:
                speak(pyjokes.get_joke())
            except Exception as e:
                print(e)
                speak("Sorry sir, I could not tell you a joke")
        elif "offline" in query:
            speak("Jarvis is going offline")
            print("Jarvis is going offline")
            exit()
        elif "email" in query:
            email_list = {
                "Tracy": "tracyvierra@yahoo.com",
                "Nicole": "buggirl_2057@yahoo.com",
            }
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
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry the email is not responding")
        elif "temperature" in query:
            try:
                speak("What is the city?")
                city = takeCommandMIC()
                speak("What is the country?")
                country = takeCommandMIC()
                url = OW_API_LINK + city + "," + country + APPID + "&units=metric"
                json_data = requests.get(url).json()
                temp = json_data["main"]["temp"]
                temp = (temp * 9 / 5) + 32  # convert to fahrenheit
                temp = round(temp, 2)
                print("The temperature is " + str(temp) + " degrees")
                speak(
                    "The temperature in "
                    + city
                    + " is "
                    + str(temp)
                    + " degrees farenheit"
                )
            except Exception as e:
                print(e)
                speak("Sorry the weather API is not responding")
        elif "create list" in query:
            try:
                speak(LIST_NAME_QUESTION)
                name = takeCommandMIC()
                speak("What should I put in the list?")
                content = takeCommandMIC()
                list_name = name + ".txt"
                with open(list_name, "w") as f:
                    f.write(content)
                speak("List has been created")
            except Exception as e:
                print(e)
                speak(LIST_NOT_RESPONDING)
        elif "read list" in query:
            try:
                speak(LIST_NAME_QUESTION)
                name = takeCommandMIC()
                list_name = name + ".txt"
                with open(list_name, "r") as f:
                    content = f.read()
                    print(content)
                    speak(content)
            except Exception as e:
                print(e)
                speak(LIST_NOT_RESPONDING)
        elif "append list" in query:
            try:
                speak("Which list do you want to append?")
                name = takeCommandMIC().lower()
                list_name = name + ".txt"
                speak("What do you want to append?")
                append = takeCommandMIC().lower()
                append_list(list_name, append)
            except Exception as e:
                print(e)
                speak(LIST_NOT_RESPONDING)

        elif "delete list" in query:
            try:
                speak(LIST_NAME_QUESTION)
                name = takeCommandMIC()
                list_name = name + ".txt"
                os.remove(list_name)
                speak("List has been deleted")
            except Exception as e:
                print(e)
                speak(LIST_NOT_RESPONDING)
        elif "create text file" in query:
            try:
                speak(FILE_NAME_QUESTION)
                name = takeCommandMIC()
                speak("What should I put in the file?")
                content = takeCommandMIC()
                file_name = name + ".txt"
                with open(file_name, "w") as f:
                    f.write(content)
                speak("File has been created")
            except Exception as e:
                print(e)
                speak(FILE_NOT_RESPONDING)
        elif "read text file" in query:
            try:
                speak(FILE_NAME_QUESTION)
                name = takeCommandMIC()
                file_name = name + ".txt"
                with open(file_name, "r") as f:
                    content = f.read()
                    print(content)
                    speak(content)
            except Exception as e:
                print(e)
                speak(FILE_NOT_RESPONDING)
        elif "delete text file" in query:
            try:
                speak(FILE_NAME_QUESTION)
                name = takeCommandMIC()
                file_name = name + ".txt"
                os.remove(file_name)
                speak("File has been deleted")
            except Exception as e:
                print(e)
                speak(FILE_NOT_RESPONDING)
        elif "create folder" in query:
            try:
                speak(FOLDER_NAME_QUESTION)
                name = takeCommandMIC()
                os.mkdir(name)
                speak("Folder has been created")
            except Exception as e:
                print(e)
                speak(FOLDER_NOT_RESPONDING)
        elif "delete folder" in query:
            try:
                speak(FOLDER_NAME_QUESTION)
                name = takeCommandMIC()
                os.rmdir(name)
                speak("Folder has been deleted")
            except Exception as e:
                print(e)
                speak(FOLDER_NOT_RESPONDING)
        elif "open folder" in query:
            try:
                speak(FOLDER_NAME_QUESTION)
                name = takeCommandMIC()
                os.chdir(name)
                speak("Folder has been opened")
            except Exception as e:
                print(e)
                speak(FOLDER_NOT_RESPONDING)
        elif "back one folder" in query:
            try:
                os.chdir("..")
                print(os.getcwd())
                speak("Folder has been opened")
            except Exception as e:
                print(e)
                speak(FOLDER_NOT_RESPONDING)
        elif "what folder" in query:
            try:
                print(os.getcwd())
                speak(os.getcwd())
            except Exception as e:
                print(e)
                speak(FOLDER_NOT_RESPONDING)
        elif "whatsapp message" in query:
            user_name = {"Tracy": "+15093934105", "Nicole": "+15094211558"}
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
        elif "headlines" in query:
            try:
                url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=37ac9a803d7b4f509cae0d11b6c40365"
                json_data = requests.get(url).json()
                articles = json_data["articles"]
                for article in articles:
                    print(article["title"])
                    speak(article["title"])
            except Exception as e:
                print(e)
                speak("Sorry the headlines API is not responding")
        elif "top 20" in query:
            try:
                url = "https://api.themoviedb.org/3/movie/popular?api_key=a300e27e1b4a17e70eee7745e3e1da69&language=en-US&page=1"
                json_data = requests.get(url).json()
                movies = json_data["results"]
                for movie in movies:
                    print(movie["title"])
                    speak(movie["title"])
            except Exception as e:
                print(e)
                speak("Sorry the movies API is not responding")
        elif "forecast" in query:
            try:
                speak("What is the name of the city?")
                city = takeCommandMIC()
                speak("What is the name of the country?")
                country = takeCommandMIC()
                url = OW_API_LINK + city + "," + country + APPID
                json_data = requests.get(url).json()
                weather = json_data["weather"]
                for w in weather:
                    print(w["description"])
                    speak(w["description"])
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
                print(*get_trending_movies(), sep="\n")
            except Exception as e:
                print(e)
                speak("Sorry the trending movies API is not responding")
        elif "trending tv shows" in query:
            try:
                speak(f"Some of the trending tv shows are: {get_trending_tv_shows()}")
                speak("For your convenience, I am printing it on the screen.")
                print(*get_trending_tv_shows(), sep="\n")
            except Exception as e:
                print(e)
                speak("Sorry the trending tv shows API is not responding")
        elif "youtube" in query:
            try:
                speak("What do you want to play on Youtube?")
                video = takeCommandMIC().lower()
                play_on_youtube(video)
            except Exception as e:
                print(e)
                speak("Sorry youtube is not responding")
        elif "discord" in query:
            try:
                open_discord()
            except Exception as e:
                print(e)
                speak("Sorry discord is not responding")
        elif "notepad" in query:
            try:
                open_notepad()
            except Exception as e:
                print(e)
                speak("Sorry notepad is not responding")
        elif "calculator" in query:
            try:
                open_calculator()
            except Exception as e:
                print(e)
                speak("Sorry calculator is not responding")
        elif "wordpad" in query:
            try:
                open_wordpad()
            except Exception as e:
                print(e)
                speak("Sorry wordpad is not responding")
        elif "chrome" in query:
            try:
                open_chrome()
            except Exception as e:
                print(e)
                speak("Sorry chrome is not responding")
        elif "firefox" in query:
            try:
                open_firefox()
            except Exception as e:
                print(e)
                speak("Sorry firefox is not responding")
        elif "steam" in query:
            try:
                open_steam()
            except Exception as e:
                print(e)
                speak("Sorry Steam is not responding")
        elif "edge" in query:
            try:
                open_edge()
            except Exception as e:
                print(e)
                speak("Sorry Microsoft Edge is not responding")
        elif "prompt" in query:
            try:
                open_cmd()
            except Exception as e:
                print(e)
                speak("Sorry command prompt is not responding")
        elif "office" in query:
            try:
                open_office()
            except Exception as e:
                print(e)
                speak("Sorry office is not responding")
        elif "reason" in query:
            try:
                speak("Opening Reason")
                open_reason()
            except Exception as e:
                print(e)
                speak("Sorry Reason is not responding")
        elif "calendar" in query:
            try:
                speak("Opening Calendar")
                open_calendar()
            except Exception as e:
                print(e)
                speak("Sorry Calendar is not responding")
        elif "maps" in query:
            try:
                speak("Opening Maps")
                open_maps()
            except Exception as e:
                print(e)
                speak("Sorry Maps is not responding")
        elif "voice recorder" in query:
            try:
                speak("Opening Voice Recorder")
                open_voice_recorder()
            except Exception as e:
                print(e)
                speak("Sorry Voice Recorder is not responding")
        elif "snip and sketch" in query:
            try:
                speak("Opening Snip and Sketch")
                open_snip_sketch()
            except Exception as e:
                print(e)
                speak("Sorry Snip and Sketch is not responding")
        elif "microsoft store" in query:
            try:
                speak("Opening Microsoft Store")
                open_microsoft_store()
            except Exception as e:
                print(e)
                speak("Sorry Microsoft Store is not responding")

        elif "snipping tool" in query:
            try:
                speak("Opening Snipping Tool")
                open_snipping_tool()
            except Exception as e:
                print(e)
                speak("Sorry Snipping Tool is not responding")
        elif "check for updates" in query:
            try:
                speak("Checking for updates")
                open_check_for_updates()
            except Exception as e:
                print(e)
                speak("Sorry Check for updates is not responding")
        elif "vnc viewer" in query:
            try:
                speak("Opening VNC Viewer")
                open_vnc_viewer()
            except Exception as e:
                print(e)
                speak("Sorry VNC Viewer is not responding")
        elif "windscribe" in query:
            try:
                speak("Opening Windscribe")
                open_windscribe()
            except Exception as e:
                print(e)
                speak("Sorry Windscribe is not responding")
        elif "screenshot" in query:
            try:
                speak("Opening Screenshot")
                open_screenshot()
            except Exception as e:
                print(e)
                speak("Sorry Screenshot is not responding")
        elif "take a note" in query:
            try:
                open_take_a_note()
            except Exception as e:
                print(e)
                speak("Sorry Take a Note is not responding")
        elif "send sms text" in query:
            try:
                speak("Preparing to send SMS text")
                open_send_sms_text()
            except Exception as e:
                print(e)
                speak("Sorry SMS Text is not responding")
        elif "send text to" in query:
            try:
                speak("Preparing to Send Text")
                open_send_text_to()
            except Exception as e:
                print(e)
                speak("Sorry Text to is not responding")
        elif "check weather" in query:
            try:
                speak("Preparing to check weather")
                open_check_weather()
            except Exception as e:
                print(e)
                speak("Sorry Check weather is not responding")
        elif 'read selected text' in query:
            try:
                speak("Preparing to read selected text")
                open_read_selected_text()
            except Exception as e:
                print(e)
                speak("Sorry Read selected text is not responding")
        elif 'check news' in query:
            try:
                speak("Preparing to check news")
                open_check_news()
            except Exception as e:
                print(e)
                speak("Sorry news API is not responding")
        elif 'my documents' in query:
            try:
                speak("Preparing to open My Documents")
                open_my_documents()
            except Exception as e:
                print(e)
                speak("Sorry My Documents is not responding")
        elif 'remember' in query:
            try:
                speak("Preparing to remember")
                open_remember()
            except Exception as e:
                print(e)
                speak("Sorry Remember is not responding")
        elif 'generate a password' in query:
            try:
                speak("Preparing to generate a password")
                open_generate_password()
            except Exception as e:
                print(e)
                speak("Sorry Generate a password is not responding")
        elif 'flip a coin' in query:
            try:
                speak("Preparing to flip a coin")
                open_flip_a_coin()
            except Exception as e:
                print(e)
                speak("Sorry Flip a coin is not responding")
        elif 'roll dice' in query:
            try:
                speak("Preparing to roll dice")
                open_roll_dice()
            except Exception as e:
                print(e)
                speak("Sorry Roll dice is not responding")
        elif 'cpu usage' in query:
            try:
                speak("Preparing to check CPU usage")
                open_cpu_usage()
            except Exception as e:
                print(e)
                speak("Sorry CPU usage is not responding")
        elif 'ram usage' in query:
            try:
                speak("Preparing to check RAM usage")
                open_ram_usage()
            except Exception as e:
                print(e)
                speak("Sorry RAM usage is not responding")
        elif 'disk usage' in query:
            try:
                speak("Preparing to check disk usage")
                open_disk_usage()
            except Exception as e:
                print(e)
                speak("Sorry disk usage is not responding")
        elif 'battery status' in query:
            try:
                speak("Preparing to check battery status")
                open_battery_status()
            except Exception as e:
                print(e)
                speak("Sorry battery status is not responding")
        elif 'check internet connection' in query:
            try:
                speak("Preparing to check internet connection")
                open_check_internet_connection()
            except Exception as e:
                print(e)
                speak("Sorry internet connection is not responding")
    
    
    
            