# python code to use openweatherAPI to get current weather and temperature in Fahrenheit:


# def open_check_weather():
#     try:
#         speak("What is your zip code?")
#         zip_code = takeCommandMIC()
#         url = OW_API_LINK + zip_code + APPID + "&units=imperial"
#         res = requests.get(url)
#         data = res.json()
#         weather = data["weather"][0]["main"]
#         temp = data["main"]["temp"]
#         temp = round(temp, 2)
#         description = data["weather"][0]["description"]
#         print(temp)
#         print(weather)
#         speak("The temperature is" + str(temp) + " degrees")
#         speak("The weather is " + description)
#     except Exception as e:
#         print(e)
#         print("Failed to check weather")

# import nltk

# nltk.download() # download the necessary packages

from nltk.tokenize import word_tokenize

sentence = "Hello Jarvis, how are you doing today? what is the current date?"

output = word_tokenize(sentence)
print(output)



