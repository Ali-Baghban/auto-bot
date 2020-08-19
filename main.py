import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import pyttsx3
import time
import sys


r = sr.Recognizer()
engine = pyttsx3.init()
mp3_fp = BytesIO()

voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice',voices[1].id)
while True:
    engine.say('Anything else with me ?')
    engine.runAndWait()
    with sr.Microphone() as source:
        print('Test Anything ...')
        #r.listen(source,timeout=1,phrase_time_limit=10)
        con = True
        while con:

            audio = r.listen(source,phrase_time_limit=2)
            #time.sleep(2)
            try:
                text = r.recognize_google(audio)
                print('You said : {}'.format(text))
                if text == 'ISA':
                    con = False
                
            except:
                pass
        engine.say("Yes I'm at your service What can I do for you ?")
        engine.runAndWait()
        time.sleep(0.3)
        audio = r.listen(source,phrase_time_limit=10)
        try:
            print('Your job ? ')
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))

            engine.say('OK I will dear Ali')
            engine.runAndWait()
        except:
            print('Error')