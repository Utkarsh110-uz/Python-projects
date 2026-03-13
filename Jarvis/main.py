import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as py

recogniser = sr.Recognizer()
engine = py.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Welcome what do we do today")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source)

        print("Recognizing...")

        # recognize speech using Sphinx
        try:
            cmd = r.recognize_google(audio)
            print(cmd)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))