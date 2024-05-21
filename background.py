import requests
import win32clipboard
import pyautogui
import os
from time import sleep
from jarvis import speak
from jarvis import takecommand


def bg():
    pyautogui.hotkey('ctrl', 'shift', 'c')
    win32clipboard.OpenClipboard()
    text1 = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    npath = text1
    os.startfile(npath)
    sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    win32clipboard.OpenClipboard()
    text2 = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    os.system("taskkill /f /IM PhotosApp.exe")
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(text2, 'rb')},

        data={'size': 'auto'},
        headers={'X-Api-Key': 'MYrqKsboush4m5z5WjqQgQF2'},
    )
    speak("sir what was the name of the image")
    name = takecommand().lower()
    print(name)
    if response.status_code == requests.codes.ok:
        with open(f'{name}.png', 'wb') as out:
            out.write(response.content)
            speak("result is this sir ")
            npath = (f"C:\\Users\\rihan\\OneDrive\\Pictures\\Removebg\\{name}.png") #8888
            os.startfile(npath)


    else:
        print("Error:", response.status_code, response.text)
