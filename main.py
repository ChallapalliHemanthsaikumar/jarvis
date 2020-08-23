import speech_recognition as sr 
import playsound
import os
import random
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


r = sr.Recognizer()

class person:
    name = ''
    def setName(self, name):
        self.name = name
class asis:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
def jarvis_speak(text):
    text = str(text)
   
    engine.say(text)
   
    engine.runAndWait()
    


def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            jarvis_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            jarvis_speak('I did not get that')
        except sr.RequestError:
            jarvis_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

                                    


def respond(voice_data):

     # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        jarvis_speak(greet)
    
    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            jarvis_speak("whats with my name ")
        else:
            jarvis_speak("i dont know my name . what's your name?")
    if there_exists(["what is my name ","guess my name "]):
        if person_obj.name:
            jarvis_speak(" your name is " + person.name)
    if there_exists(["save this"]):
        text = record_audio(' spell it ')
        
        text_file = open("sample.txt", "w")
        text_file.write(text)
        text_file.close()


    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        jarvis_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        jarvis_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        jarvis_speak("I'm very well, thanks for asking " + person_obj.name)



    if 'what is your name' in voice_data:
        jarvis_speak('My name is Jarvis') 
    if 'what time is it' in voice_data:
        jarvis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("what do you want me to search")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarvis_speak('Here is what I found for ' + search )
    if 'location' in voice_data:
        location = record_audio('which location do you want ?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        jarvis_speak('Here is what I found for ' + location )
    if 'exit' in voice_data:
        jarvis_speak("bye Boss")
        exit()
       #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        jarvis_speak("The computer chose " + cmove)

      #14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                jarvis_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                jarvis_speak('here is what i found '+definitions[1])
            else:
                jarvis_speak('Here is what i found '+definitions[2])
        else:
                jarvis_speak("im sorry i could not find the definition for "+definition)
    
        

time.sleep(1)
person_obj = person()
asis_obj = asis()
asis_obj.name = 'Jarvis'
engine = pyttsx3.init()


jarvis_speak("How can I help you Boss")
while 1:
     voice_data = record_audio()
     respond(voice_data)