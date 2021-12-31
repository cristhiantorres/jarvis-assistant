import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
from functions.os_ops import open_notepad, open_cmd

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')


# Set rate
engine.setProperty('rate', 190)

# Set volume
engine.setProperty('volume', 1.0)

# Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos dias {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Buenas tardes {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Buenas Noches {USERNAME}")
    speak(f"Yo soy {BOTNAME}. Como puedo ayudarte?")

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='es-mx')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 12 and hour < 6:
                speak('Good night sir, take care!')
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        print('Error...')
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower
        

        if 'open notepad' in query:
            open_notepad()
        elif 'open terminal' in query:
            open_cmd()