import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import texteditor
import time 
import subprocess
import threading
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_f = "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/MSMary"
engine.setProperty('voice', voice_f)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


no = ["no", "not yet", "wait rey" , "noooo"]
yes = ["yes","yeah","yea","s"]
note = ["write note","write this","write it","write this in notepad","write a note"]


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

def notepad(filename,content):

    result = texteditor.open(filename=filename,text=content)
    
    print(result)

def listfiles():
    textlist = [] 
    dirt = os.listdir()
    if not dirt: 
        speak("list is empty boss")
        
    for num in dirt:
        if ".txt" in num: 
            textlist.append(num)  
    return textlist 

notelist = listfiles()
print(notelist)
speak("which one you want to select ")
selection = "sample.txt"
for line in notelist: 
    if selection in line:
        with open(line, "a+") as edit:
             
            edit.write("\n")
            content = takeCommand()
            edit.write(content) 
        edit.close()


# if __name__ == "__main__":
#     def start():  
#         query = takeCommand()
#         for line in note: 
#             if line  in query: 
#                 speak("Okay boss ")
#                 content  = takeCommand()
#                 while (True): 
#                     speak(" are you done")
#                     command = takeCommand()
#                     for line in no:
#                         if line in command: 
#                             content = content + takeCommand()
#                     for line in yes:        
#                         if line in command: 
#                             speak("on which name i want to save it boss")
#                             filename = takeCommand()
#                             if ".txt" not in filename: 
#                                 filename = filename + ".txt"                    
#                                 x = threading.Thread(target=notepad, args=(filename, content,))
#                                 x.start()
#                                 time.sleep(3)
#                                 return start() 

            