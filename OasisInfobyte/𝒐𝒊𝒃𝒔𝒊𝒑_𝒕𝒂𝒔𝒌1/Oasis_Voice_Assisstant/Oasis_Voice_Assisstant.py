#Basic
from os import system
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

def main():
    speak("Hello! How may I assist you today?")
    
    while True:
        command = Listen()

        if "hello" in command:
            speak("Hi!! I am here to help with anything you need.")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")

        elif "google" in command:
            speak("What would you like me to google for?")
            search_query = Listen()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
            else:
                speak("Sorry, I didn't quiet catch that. Please ask again.")

        elif "exit" in command:
            speak("Goodbye! Have a good day!")
            sys.exit(0)

        else:
            speak("Sorry, I don't understand that command. Please ask again.")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def Listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't quiet catch that.")
        return ""


if __name__ == "__main__":
    main()

