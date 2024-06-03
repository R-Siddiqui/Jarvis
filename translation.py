import os
import time
from deep_translator import GoogleTranslator
import pyautogui
import pyttsx3
import speech_recognition as sr
import win32clipboard
# from googletrans import Translator
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
    translated = GoogleTranslator(source='auto', target='hi').translate(Text) 

    try:
        speakgl = gTTS(text=translated, lang="hi", slow= False)
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
    translated = GoogleTranslator(source='auto', target='en').translate(Text) 
    try:
        speakgl = gTTS(text=translated, lang="en", slow= False)
        speakgl.save("voice.mp3")
        speak("done sir")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("unable to translate")