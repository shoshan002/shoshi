import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('rate', 170)  
    engine.setProperty('voice', voices[1].id)
    print(voices)
    engine.say(text)
    engine.runAndWait()


speak("hurray")