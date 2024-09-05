import pyttsx3
import speech_recognition as sr
import eel 
import time
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('rate', 170)  
    eel.DisplayMessage(text)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio= r.listen(source,10,6)
    try:
        print("recognizing")
        eel.DisplayMessage("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommands():  
    try:
        query = takecommand()
        print(query)

        if "open" in query:
                from engine.features import openCommand
                openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("not run")
    except:
        print("error")
    

    eel.ShowHood()
       