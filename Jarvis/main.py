# # Importing Modules
# import speech_recognition as sr
# from webbrowser import *
# from pyttsx3 import *

# # Function that takes input from our microphone
# def take_cmd():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio)
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             return "Some error occured. Jarvis say sorry"

# if __name__ == "__main__":
#     print("Code is running...")
#     speak("Jarvis Welcomes you")
#     while True:
#         print("Listening...")
#         text = take_cmd()
#         sites = [["Youtube", "https://www.youtube.com"], ["Google", "https://www.google.com"], ["Python", "https://replit.com"], ["chat gpt", "https://chatgpt.com"], ["Cloud", "https://claude.ai/new"], ["color codes", "https://htmlcolorcodes.com"], ["Lead code", "https://leetcode.com"], ["Stack overflow", "https://stackoverflow.com/questions"], ["fonts page", "https://fonts.google.com"], ["My github", "https://github.com/Utkarsh110-uz"], ["Github", "https://github.com"]]
#         for site in sites:
#             if f"Open {site[0]}".lower() in text.lower():
#                 speak(f"Opening {site[0]} for you")
#                 open(f"{site[1]}")

import time
from pyttsx3 import *

current_time = time.strftime("%I:%M")

if current_time >= "12:00" and current_time < "5:00":
    speak("Its midnight why are you still awake sir do you need any help ?")
elif current_time >= "5:00" and current_time < "12:00":
    speak("Good morning sir i hope you have a good sleep")
elif current_time >= "12:00" and current_time < "5:00":
    speak("Good afternoon sir so whats the agenda today")
elif current_time >= "5:00" and current_time < "9:00":
    speak("Good evening sir its good to see you again")
elif current_time >= "9:00" and current_time < "12:00":
    speak("Its bed time sir you still awake any important task remaing")
else:
    speak("I can't understand your time for now")

print(current_time)