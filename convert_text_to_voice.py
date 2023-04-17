import pyttsx3

engine = pyttsx3.init()
with open('script.txt', 'r') as f:
    script = f.read()
    
engine.say(script)
engine.runAndWait()