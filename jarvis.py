import speech_recognition as sr
import os

# create recognizer
r = sr.Recognizer()

# use microphone as input
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)

# recognize speech using Google API
try:
    text = r.recognize_google(audio)
    user = str(text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Could not request results, check internet")

os.system(user)