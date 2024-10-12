import pyttsx3
import datetime
import speech_recognition as sr
import datetime
from requests import get
import webbrowser
import sys
import smtplib
from time import sleep
import pyautogui
pyautogui.FAILSAFE = False
from time import sleep
import win32clipboard
import os
from playsound import playsound
from tkinter import simpledialog
import pyperclip as p
from groq import Groq
pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')
my_i = simpledialog.askstring("Input", "your email id")
p.copy(my_i)
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
sleep(6)
pyautogui.press('c')
sleep(4)
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
sleep(2)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'shift', '2')
sleep(1)
pyautogui.press('esc')
sleep(2)
pyautogui.write("Hello")
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
sleep(4)
pyautogui.hotkey('ctrl', 'enter')