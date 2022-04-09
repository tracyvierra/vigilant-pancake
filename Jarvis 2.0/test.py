# https://api.openweathermap.org/data/2.5/weather?&units=standard&q=chelan&appid=cce9b0c81b54033cc50f4e071fc11360


# start logging file for session:
# x = datetime.datetime.now()
# file_name = x.strftime("%Y-%m-%d-%H-%M-%S")
# file_handler = logging.FileHandler(
#     filename="jarvis_error_log-" + file_name + ".log", mode="w"
# )
# handlers = [file_handler]

# logging.basicConfig(
#     level=logging.INFO,
#     format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
#     handlers=handlers,
# )

# logger = logging.getLogger("LOGGER_NAME")

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))