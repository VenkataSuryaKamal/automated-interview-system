import pyttsx3
from threading import Thread
def stt(stri):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(stri)
    engine.runAndWait()
