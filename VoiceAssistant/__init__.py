import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id) 
    print(engine.getProperty('rate'))
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 0.6)
    engine.say(text)
    engine.runAndWait()