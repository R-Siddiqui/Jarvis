import os
import time

import pyautogui
import pyttsx3
import speech_recognition as sr
import win32clipboard
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7, phrase_time_limit=10)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            return query

        except Exception as e:
            speak("say the again please...")
            return "None"
        return query

def translate_hi(query):
    speak("ok sir please wait ")
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    win32clipboard.OpenClipboard()
    Text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    translator = Translator()
    text_to_translate = translator.translate(Text, src="auto", dest="hi")
    out = text_to_translate.text
    try:
        speakgl = gTTS(text=out, lang="hi", slow= False)
        speakgl.save("voice.mp3")
        speak("done sir")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("unable to translate")

def translate_en(query):
    speak("ok sir please wait ")
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    win32clipboard.OpenClipboard()
    Text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    translator = Translator()
    text_to_translate = translator.translate(Text, src="auto", dest="en")
    out = text_to_translate.text
    try:
        speakgl = gTTS(text=out, lang="en", slow= False)
        speakgl.save("voice.mp3")
        speak("done sir")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("unable to translate")