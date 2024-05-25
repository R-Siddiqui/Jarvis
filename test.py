# import pyttsx3
# import datetime
# import speech_recognition as sr
# import datetime
# import cv2
# from requests import get
# import wikipedia
# import webbrowser
# import sys
# import pyjokes
# import smtplib
# from time import sleep
# import pyautogui
# pyautogui.FAILSAFE = False
# from time import sleep
# import win32clipboard
import requests
# import json
# import os
# import glob
# from googletrans import Translator
# from playsound import playsound
# from dotenv import load_dotenv

# load_dotenv()
# from tkinter import simpledialog
# import pyperclip as p

# #engine

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)



# #text to voice

# def speak(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()

# #voice to text
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=100, phrase_time_limit=5)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")
#             return query

#         except Exception:
#             # speak("say the again please...")
#             return "None"
#         query = query.lower()
#         return query
    
def taskexecution():
        response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": f"Bearer sk-YpQrkEI53EbnG5dcyFvizXZcQq9yRt4Q8Zu2cU6cATDCke84",
                "accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": "dog wearing black glasses",
                "output_format": "webp",
            },
        )

        if response.status_code == 200:
            with open("./output/dog-wearing-glasses.webp", 'wb') as file:
                file.write(response.content)
        else:
            raise Exception(str(response.json()))

taskexecution()