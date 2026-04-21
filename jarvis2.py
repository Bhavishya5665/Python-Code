from email.mime import audio
from re import A
import re

import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import webbrowser
import datetime


engine = pyttsx3.init()


def speak (txt):
    print("Assistant: ", txt)
    engine.say(txt)
    engine.runAndWait()



def record_audio(duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    # print("Recording complete.")
    return audio, fs




def takeCommand():
    r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)

    try:
        audio_data, fs = record_audio()

        audio_bytes = audio_data.tobytes()
        audio = sr.AudioData(audio_bytes, fs, 2)
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print("You said: ", command)
        return command.lower()

    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    # return command

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube")

def open_google():
    webbrowser.open("https://www.google.com")
    speak("Opening Google")

def tell_joke():
    joke = "Why don't scientists trust atoms? Because they make up everything!" 
    speak(joke) 

# def write_email():
#     speak("What should be the subject?")
#     subject = takeCommand()
#     speak("What should i write in the email?")
#     body = takeCommand()

#     email_text = f"""
# Subject: {subject}

# {body}

def run_assistant():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        command = takeCommand().lower()

        if 'open youtube' in command:
            open_youtube()
        elif 'open google' in command:
            open_google()
        elif 'tell me a joke' in command:
            tell_joke()
        elif 'what time is it' in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")

run_assistant()