import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os,random
import smtplib
from gtts import gTTS
from time import ctime 
import time
import webbrowser
import pyttsx3
import subprocess
import bs4 as bs
import urllib.request
import pyautogui
import ssl
import certifi
import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_f = "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/MSMary"
engine.setProperty('voice', voice_f)
engine.say('Hello with my new voice')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def save(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"JARVIS: {audio_string}") # print what app said
    
     # remove audio file


def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss said: {query}\n")

    except Exception as e: 
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":

    wishMe()
    while True:
    
        query = takeCommand().lower()
        if 'jarvis' in query:
            speak('Yes Boss I am listening')
            if 'Note' in query:
                save('SPELL IT')
       


        
            
      